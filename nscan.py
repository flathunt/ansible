import nmap
import pandas as pd

def scan_network(network_range):
    # Initialize the Nmap PortScanner
    nm = nmap.PortScanner()
    
    # Scan the network range for live hosts
    nm.scan(hosts=network_range, arguments='-sn')
    
    # Extract the list of pingable devices
    devices = []
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            devices.append({
                'IP Address': host,
                'Hostname': nm[host].hostname(),
                'State': nm[host].state()
            })
    
    return devices

def format_devices(devices):
    # Create a DataFrame to format the list of devices
    df = pd.DataFrame(devices)
    return df

def main():
    network_range = '192.168.68.0/24'  # Adjust this to match your network range
    devices = scan_network(network_range)
    formatted_devices = format_devices(devices)
    
    # Display the formatted list of devices
    print(formatted_devices.to_string(index=False))

if __name__ == '__main__':
    main()

