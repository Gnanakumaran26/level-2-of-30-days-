import socket
from datetime import datetime

# -------------------------------
# Common ports & services
# -------------------------------
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}

# -------------------------------
# Port Scanner Function
# -------------------------------
def scan_ports(target):
    print("=" * 50)
    print(f"Scanning Target: {target}")
    print(f"Scan started at: {datetime.now()}")
    print("=" * 50)

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("❌ Invalid host name")
        return

    print(f"Target IP: {target_ip}\n")

    open_ports = []

    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown Service")
            print(f"✅ Port {port} OPEN ({service})")
            open_ports.append(port)

        sock.close()

    print("\n" + "-" * 50)
    print("Scan completed.")
    print(f"Total open ports found: {len(open_ports)}")
    print("-" * 50)


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    print("🔐 PYTHON PORT SCANNER 🔐")
    target = input("Enter IP address or domain: ")
    scan_ports(target)
