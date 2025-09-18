import socket

def scan_ports(host, ports):
    print(f"Scanning {host}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((host, port))
            print(f"[+] Port {port} is OPEN")
        except:
            pass
        s.close()

if __name__ == "__main__":
    target = input("Enter target host (e.g. 127.0.0.1): ")
    ports = [21, 22, 23, 25, 80, 443, 3306, 8080]  # common ports
    scan_ports(target, ports)
