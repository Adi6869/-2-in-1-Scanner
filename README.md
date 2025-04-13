
# 2-in-1 Vulnerability Scanner

A simple yet powerful command-line tool that combines a **Network Scanner** and **Web Application Vulnerability Scanner**

## Features

- **Network Scanner**
  - Port scanning over a specified range
  - Optional multithreaded scanning for performance
  - Identifies open ports on the target host

- **Web Application Scanner**
  - Uses Nikto to perform a basic vulnerability scan on web servers
  - Identifies common misconfigurations and known issues

## How It Works
### Main Menu
Upon running `main.py`, the user is prompted to select one of two options:
1. **Network Scanner**: Asks for an IP address, port range, and threading preference, then launches the network scanner.
2. **Web Application Scanner**: Asks for a domain name, then launches the Nikto-based scanner inside Kali Linux (via WSL).

## 🛠Requirements

- Python 
- Kali Linux via WSL (for running Nikto)
- Nikto installed inside WSL
- Windows Subsystem for Linux (WSL) enabled and set up
---

## How to Run

```bash
python main.py
```

Future Improvements
 - Add CVE/Exploit-DB auto lookup
 - Integrate Shodan API for threat intelligence
 - Add real-time progress bars and logging



