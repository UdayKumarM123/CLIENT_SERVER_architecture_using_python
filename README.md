# CLIENT_SERVER Architecture using Python

This project demonstrates a simple **Client–Server communication system** built in **Python**.  
It uses **socket programming** to send and receive messages between a client and a server over TCP.

---

## Project Structure

CLIENT_SERVER_architecture_using_python/
│
├── client/                  # (Optional) Folder for client components
├── server/                  # (Optional) Folder for server components
├── logs/                    # Contains log files for chat messages
│
├── client.py                # Python script for client
├── server.py                # Python script for server
├── client_chat_log.txt      # Log file that records chat messages
├── pclient.png              # Screenshot of client terminal
├── pserver.png              # Screenshot of server terminal
├── logc.png, logp.png       # Log visualization images
└── README.md                # Project documentation

---

## Features

✅ Real-time message exchange between client and server  
✅ Uses Python’s built-in `socket` module (no external dependencies)  
✅ Logs all communication to `client_chat_log.txt`  
✅ Simple terminal-based interface  
✅ Works on both Windows and Linux  

---

## Concepts Used

- Socket programming (`socket`, `bind`, `listen`, `accept`, `connect`, `send`, `recv`)  
- Multi-threading for handling multiple clients  
- File handling and logging  
- Basic networking concepts (TCP/IP)  

---

## How to Run the Project

## Step 1 — Run the Server
Start the server first:

python server.py

 
## Step 2 — Run the Client
In a new terminal window:

python client.py


Now you can chat between the client and server in real time! 

---

## Screenshots

### Client Terminal
![Client Interface](pclient.png)

### Server Terminal
![Server Interface](pserver.png)

---

## Log Files

All chat messages are saved automatically to:

logs/client_chat_log.txt


---

## Future Improvements

- Support multiple clients simultaneously  
- Add authentication system (username/password)  
- Create a GUI using `tkinter` or `PyQt`  
- Encrypt chat messages using Python’s `cryptography` library  

---

## Author

**Uday Kumar M**  
📧 [udaykumarm.ai23@bmsce.ac.in]  
🌐 [https://github.com/UdayKumarM123](https://github.com/UdayKumarM123)

---

### 🏁 License
This project is open-source and free to use for educational or personal learning purposes.
