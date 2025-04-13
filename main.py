import subprocess

# Simple Banner
print("=" * 30)
print("  2-in-1 Vulnerability Scanner")
print("=" * 30)

print("1. Network Scanner")
print("2. Web Application Scanner")

while True:
    choice = input("Choose an option (1 or 2): ").strip()
    if choice in ["1", "2"]:
        break
    else:
        print("Invalid choice. Enter 1 for Network Scanner or 2 for Web Application Scanner.")

if choice == "1":
    target = input("Enter the target IP: ").strip()

    while True:
        try:
            beginning_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))
            if 1 <= beginning_port <= 65535 and 1 <= end_port <= 65535 and beginning_port <= end_port:
                break
            else:
                print("Invalid port range. Enter values between 1 and 65535.")
        except ValueError:
            print("Enter a valid number.")

    while True:
        try:
            max_threads = int(input("Enter the number of threads (0 for no threading): "))
            break
        except ValueError:
            print("Enter a valid number.")

    print("Launching Network Scanner...")
    subprocess.run(["python", "network_scanner.py", target, str(beginning_port), str(end_port), str(max_threads)], check=True)

elif choice == "2":
    target = input("Enter the target website's domain: ").strip()
    print("Launching Web Application Scanner...")
    subprocess.run(["python", "nikto.py", target], check=True)
