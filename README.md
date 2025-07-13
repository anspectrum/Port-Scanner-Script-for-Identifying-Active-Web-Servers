Overview

This script is designed to scan a specified IP address range to check for open ports (80 and 443) commonly used for web traffic. It helps identify responsive IP addresses that are actively hosting web servers. Once the script detects an open port, it records the IP address in a file and attempts to open each of the discovered IP addresses in a web browser.

The tool leverages multi-threading for efficient scanning and supports Firefox for opening URLs.
Features

    Port Scanning: Scans IPs for open ports (HTTP on port 80 and HTTPS on port 443).

    Concurrency: Uses multi-threading for faster scanning with support for parallel execution.

    Browser Integration: Opens discovered IPs in a web browser (Firefox supported).

    Output: Saves found IPs in a text file (ips.txt).

Requirements

    Python 3.x

Usage

    Configure the IP Range:
    Define the range of IP addresses to scan by setting the start_ip and end_ip in the script.

    Set the Ports:
    The script is configured to check ports 80 and 443 by default, which are commonly used for HTTP and HTTPS traffic.

    Run the Script:
    Execute the script to scan the defined IP range for open ports. It will save any responsive IP addresses in ips.txt.

    python3 browser-web-port-scan-tabs.py

    Open Results in Browser:
    If any IPs are found to have open ports, the script will attempt to open each one in a new browser tab (Firefox is supported by default).

Example Output

If the script detects an open port, you might see output like this in the console:

Found open port 80 on 103.204.40.15
Found open port 443 on 103.204.40.20
Scanning complete! Found 2 active IPs.

The active IPs are saved to the ips.txt file, and new tabs will open in the browser for each found IP.
Customization

    Max Threads: You can adjust the max_threads variable to increase or decrease the number of concurrent threads for faster or slower scans.

    Browser Configuration: Modify the open_ips_in_firefox function to use a different browser if necessary (currently configured for Firefox).

Important Notes

Ethical Use: This script is intended for legitimate purposes, such as scanning your own network or obtaining public server information for research. Please ensure that you have permission to scan the IP ranges you are targeting.

Not for Malicious Use: Unauthorized port scanning can be considered illegal in certain jurisdictions. Always use this tool responsibly and with appropriate authorization.
