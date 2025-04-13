import socket
import concurrent.futures
import re
import os
import sys

def port_scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            sock.settimeout(3)
            service = get_service_info(port)
            banner, service_detected, detected_version = banner_grab(target, port)
            print(f"Port {port} is open ({service})")
            print(f"Banner: {banner}")
        sock.close()
    except Exception as e:
        print(f"Failed to Scan port {port}: {e}")

def target_scan(target, beginning_port, end_port, max_threads=None):
    if max_threads is None or max_threads <= 0:
        max_threads = os.cpu_count() * 2

    print(f"Scanning target {target} from {beginning_port} to {end_port} with {max_threads} threads...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(lambda port: port_scan(target, port), range(beginning_port, end_port + 1))

def load_services(filename="common_services.txt"):
    services = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    port, service = parts
                    services[int(port)] = service
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Using default services.")
    return services

SERVICES = load_services()

def get_service_info(port):
    return SERVICES.get(port, "Unknown")

def extract_service_version(banner):
    match = re.search(r"([a-zA-Z\-\_]+)\s?([\d]+\.[\d]+\.[\d]+)?", banner)
    if match:
        service_name = match.group(1)
        version = match.group(2) if match.group(2) else "Unknown"
        return service_name, version
    return "Unknown", "Unknown"

def banner_grab(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target, port))

        if port in [80, 443, 8080]:
            sock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
        elif port == 21:
            sock.send(b"USER anonymous\r\n")
        elif port == 22:
            sock.send(b"SSH-2.0-Scanner\r\n")
        elif port in [25, 587, 465]:
            sock.send(b"EHLO example.com\r\n")

        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()
        if banner:
            service, version = extract_service_version(banner)
            return banner, service, version
        else:
            return "No banner received", "Unknown", "Unknown"
    except:
        return "No banner received", "Unknown", "Unknown"

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python network_scanner.py <target> <start_port> <end_port> <max_threads>")
        sys.exit(1)

    target = sys.argv[1]
    beginning_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    max_threads = int(sys.argv[4])

    target_scan(target, beginning_port, end_port, max_threads)
