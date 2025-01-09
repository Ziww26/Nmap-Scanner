import socket

def scan_ports(host):
    print(f"Scanning ports on {host}...\n")
    for port in range(1, 1025):  # On scanne les ports de 1 à 1024
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((host, port))  # connect_ex retourne 0 si le port est ouvert
                if result == 0:
                    print(f"Port {port} is OPEN")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    target = input("Enter the IP address to scan: ")
    scan_ports(target)
