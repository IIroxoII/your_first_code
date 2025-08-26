import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

# === CONFIGURATION ===
base_password = "T9$gVlx7@QzL#r3mW2e^Np8s"

# === MACHINE ID BINDING ===
import platform
import uuid
from hashlib import sha256

def get_machine_id():
    raw_id = f"{platform.node()}_{uuid.getnode()}"
    return sha256(raw_id.encode()).hexdigest()

machine_id = get_machine_id()
final_password = base_password + machine_id

# === DRIVE DETECTION ===
def get_all_available_drives():
    return [f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]

# === FILE DECRYPTION ===
def decrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as f:
            raw_data = f.read()

        salt = raw_data[:16]
        iv = raw_data[16:32]
        ciphertext = raw_data[32:]

        key = PBKDF2(password, salt, dkLen=32, count=100000, hmac_hash_module=SHA256)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        decrypted_path = file_path.replace('.encrypted', '.decrypted')
        with open(decrypted_path, 'wb') as f:
            f.write(plaintext)

        print(f"[+] Decrypted: {decrypted_path}")
    except Exception as e:
        print(f"[!] Failed to decrypt {file_path}: {e}")

# === MAIN EXECUTION ===
def main():
    drives = get_all_available_drives()
    target_extensions = ('.encrypted',)

    for drive in drives:
        print(f"Scanning drive: {drive}")
        for foldername, subfolders, filenames in os.walk(drive):
            for filename in filenames:
                if filename.lower().endswith(target_extensions):
                    file_path = os.path.join(foldername, filename)
                    print(f"Decrypting: {file_path}")
                    decrypt_file(file_path, final_password)

if __name__ == "__main__":
    main()

