# This script scan ports 80/443 against a range of IPs and if found open
# adds the IP in a file and opens in the browser tab
import socket
import webbrowser
from concurrent.futures import ThreadPoolExecutor

# Define the IP range to scan
start_ip = "x.x.x.x"
end_ip = "y.y.y.y"
ports = [80, 443]  # Ports to scan
max_threads = 50  # Number of concurrent threads

# Output file for responsive IPs
file_path = "ips.txt"

def ip_range(start_ip, end_ip):
    """Generate IP addresses from start to end."""
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    current = start[:]
    
    while current <= end:
        yield ".".join(map(str, current))
        for i in range(3, -1, -1):
            if current[i] < 255:
                current[i] += 1
                break
            current[i] = 0

def is_port_open(ip):
    """Check if a given IP has an open port (80 or 443)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        for port in ports:
            if sock.connect_ex((ip, port)) == 0:
                print(f"Found open port {port} on {ip}")
                return ip  # Return IP if any port is open
    return None

def scan_ips():
    """Scan IPs using multi-threading and save responsive IPs."""
    responsive_ips = []
    
    print("Scanning IP range...")
    with ThreadPoolExecutor(max_threads) as executor:
        results = executor.map(is_port_open, ip_range(start_ip, end_ip))

    # Collect results
    responsive_ips = [ip for ip in results if ip]

    # Write to file
    with open(file_path, "w") as file:
        file.writelines(f"{ip}\n" for ip in responsive_ips)

    return responsive_ips

def open_ips_in_firefox(ip_list):
    """Open found IPs in Firefox."""
    if ip_list:
        firefox_path = "/media/E/software/firefox-linux-portable/firefox %s"
        browser = webbrowser.get(firefox_path)
        for ip in ip_list:
            browser.open_new_tab(f"http://{ip}")
    
    print(f"Scanning complete! Found {len(ip_list)} active IPs.")

# Run the scanning and open tabs
found_ips = scan_ips()
open_ips_in_firefox(found_ips)
