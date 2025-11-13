import socket
import threading
from datetime import datetime
import os

# ---------- Caesar Cipher ----------
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# ---------- Logging ----------
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "client_chat_log.txt")

def log_message(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

# ---------- Receive messages ----------
def receive_messages(sock, shift):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\n[-] Server disconnected.")
                break

            encrypted_msg = data.decode()
            decrypted_msg = caesar_decrypt(encrypted_msg, shift)

            print(f"\n[Server encrypted]: {encrypted_msg}")
            print(f"[Server decrypted]: {decrypted_msg}\n> ", end="", flush=True)

            log_message(f"Received (encrypted): {encrypted_msg}")
            log_message(f"Received (decrypted): {decrypted_msg}")

        except Exception as e:
            print(f"[!] Error receiving: {e}")
            break

# ---------- Send messages ----------
def send_messages(sock, shift):
    while True:
        try:
            msg = input("> ")
            if msg.lower() == "exit":
                sock.close()
                print("[.] Client closed.")
                break
            encrypted = caesar_encrypt(msg, shift)
            sock.sendall(encrypted.encode())

            print(f"[Client encrypted]: {encrypted}")

            log_message(f"Sent (encrypted): {encrypted}")
            log_message(f"Sent (decrypted): {msg}")

        except Exception as e:
            print(f"[!] Error sending: {e}")
            break

# ---------- Main ----------
def main():
    host = "127.0.0.1"
    port = 65432
    shift = 3

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print(f"[+] Connected to {host}:{port}")
        print("Type messages to send. Type 'exit' to quit.\n")

        threading.Thread(target=receive_messages, args=(sock, shift), daemon=True).start()
        send_messages(sock, shift)

    except Exception as e:
        print(f"[!] Connection error: {e}")

if __name__ == "__main__":
    main()
