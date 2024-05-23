import nmap
from tabulate import tabulate

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
    # Create a list of lists to format the list of devices for tabulate
    formatted_devices = [["IP Address", "Hostname", "State"]]
    for device in devices:
        formatted_devices.append([device['IP Address'], device['Hostname'], device['State']])
    return formatted_devices

def main():
    network_range = '192.168.68.0/24'  # Adjust this to match your network range
    devices = scan_network(network_range)
    formatted_devices = format_devices(devices)
    
    # Display the formatted list of devices in ASCII table
    print(tabulate(formatted_devices, headers="firstrow", tablefmt="grid"))

if __name__ == '__main__':
    main()

