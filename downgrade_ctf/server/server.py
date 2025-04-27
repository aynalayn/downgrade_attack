import socket
import ssl
from threading import Thread

FLAG = "FLAG:{TLS_DOWNGRADE_MASTER_1337}"
HOST = '0.0.0.0'
PORT = 4433

def handle_client(conn):
    try:
        tls_version = conn.version()
        if tls_version == "TLSv1":
            conn.sendall(f"Success! Your flag: {FLAG}\n".encode())
        else:
            conn.sendall(b"Server requires TLS 1.0 connection to get the flag\n")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def start_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain('server.crt', 'server.key')
    context.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        print(f"[*] Server listening on {HOST}:{PORT} (TLS 1.0/1.3)")
        
        while True:
            client, addr = sock.accept()
            print(f"[+] Connection from {addr}")
            ssl_conn = context.wrap_socket(client, server_side=True)
            Thread(target=handle_client, args=(ssl_conn,)).start()

if __name__ == "__main__":
    start_server()