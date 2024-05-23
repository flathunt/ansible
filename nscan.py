import subprocess
import re

def scan_network(network_range):
    # Run the Nmap ping scan using subprocess
    result = subprocess.run(['nmap', '-sn', network_range], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Check for errors
    if result.returncode != 0:
        print("Error running Nmap scan:", result.stderr)
        return []
    
    # Extract pingable devices from the Nmap output
    devices = []
    current_ip = None
    for line in result.stdout.splitlines():
        if "Nmap scan report for" in line:
            current_ip = re.search(r'Nmap scan report for ([\d.]+)', line)
            if current_ip:
                current_ip = current_ip.group(1)
        elif "Host is up" in line and current_ip:
            devices.append(current_ip)
            current_ip = None

    return devices

def format_devices(devices):
    # Create a formatted ASCII table for the list of devices
    table = "IP Address\n" + "-"*40 + "\n"
    for device in devices:
        table += f"{device}\n"
    return table

def main():
    network_range = '192.168.68.0/24'  # Adjust this to match your network range
    devices = scan_network(network_range)
    
    if devices:
        formatted_devices = format_devices(devices)
        # Display the formatted list of devices in ASCII table
        print(formatted_devices)
    else:
        print("No devices found or an error occurred.")

if __name__ == '__main__':
    main()

