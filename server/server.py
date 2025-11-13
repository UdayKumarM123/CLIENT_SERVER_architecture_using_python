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
LOG_FILE = os.path.join(LOG_DIR, "server_chat_log.txt")

def log_message(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

# ---------- Handle client ----------
def handle_client(conn, addr, shift):
    print(f"[+] Connected with {addr}")

    # Send welcome message
    welcome_plain = "Welcome to the secure server!"
    welcome_encrypted = caesar_encrypt(welcome_plain, shift)
    conn.sendall(welcome_encrypted.encode())

    print(f"[Server encrypted]: {welcome_encrypted}")
    print(f"[Server decrypted]: {welcome_plain}")
    log_message(f"Sent welcome (encrypted): {welcome_encrypted}")
    log_message(f"Sent welcome (decrypted): {welcome_plain}")

    # ---- Receive Thread ----
    def receive_thread():
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    print(f"[-] Client {addr} disconnected.")
                    break

                encrypted_msg = data.decode()
                decrypted_msg = caesar_decrypt(encrypted_msg, shift)

                print(f"\n[Client encrypted]: {encrypted_msg}")
                print(f"[Client decrypted]: {decrypted_msg}\n> ", end="", flush=True)

                log_message(f"From {addr} (encrypted): {encrypted_msg}")
                log_message(f"From {addr} (decrypted): {decrypted_msg}")

                # Send ACK (encrypted)
                ack_plain = f"ACK: {decrypted_msg}"
                ack_encrypted = caesar_encrypt(ack_plain, shift)
                conn.sendall(ack_encrypted.encode())

                log_message(f"Sent ACK (encrypted): {ack_encrypted}")
                log_message(f"Sent ACK (decrypted): {ack_plain}")

            except Exception as e:
                print(f"[!] Error with {addr}: {e}")
                break

    # ---- Send Thread ----
    def send_thread():
        while True:
            try:
                msg = input("> ")
                if msg.lower() == "exit":
                    conn.close()
                    print("[.] Connection closed.")
                    break

                encrypted = caesar_encrypt(msg, shift)
                conn.sendall(encrypted.encode())

                print(f"[Server encrypted]: {encrypted}")
                print(f"[Server decrypted]: {msg}")

                log_message(f"Sent to {addr} (encrypted): {encrypted}")
                log_message(f"Sent to {addr} (decrypted): {msg}")

            except Exception as e:
                print(f"[!] Error sending: {e}")
                break

    threading.Thread(target=receive_thread, daemon=True).start()
    send_thread()

# ---------- Main ----------
def main():
    host = "0.0.0.0"
    port = 65432
    shift = 3

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[+] Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr, shift)).start()

if __name__ == "__main__":
    main()
