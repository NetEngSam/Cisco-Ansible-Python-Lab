import re

def parse_hostname(config):
    match = re.search(r'^hostname (\S+)', config, re.MULTILINE)
    return match.group(1) if match else "Unknown"

def parse_interfaces(config):
    interfaces = re.findall(r'^interface (\S+)', config, re.MULTILINE)
    interface_data = []

    for intf in interfaces:
        # Get interface IP and mask
        ip_match = re.search(rf'{intf}\n(?: .*\n)* ip address (\S+) (\S+)', config)
        ip = ip_match.group(1) if ip_match else "unassigned"
        mask = ip_match.group(2) if ip_match else "unassigned"

        # Check interface status (shutdown or no shutdown)
        shut_match = re.search(rf'{intf}\n(?: .*\n)* shutdown', config)
        status = "Administratively Down" if shut_match else "Up"

        interface_data.append((intf, ip, mask, status))

    return interface_data

def parse_ospf_neighbors(config):
    neighbors = re.findall(r'neighbor (\S+)', config)
    return neighbors if neighbors else ["No neighbors found"]

backup_files = ["./backups/CSR1-backup.cfg", "./backups/CSR2-backup.cfg"]

for file in backup_files:
    with open(file, "r") as f:
        config = f.read()

    print(f"\n{'-'*40}")
    print(f"Parsing config: {file}")
    print(f"{'-'*40}")

    hostname = parse_hostname(config)
    print(f"Hostname: {hostname}\n")

    interfaces = parse_interfaces(config)
    print("Interfaces:")
    for intf, ip, mask, status in interfaces:
        print(f" - {intf}: IP {ip}, Mask {mask}, Status: {status}")

    ospf_neighbors = parse_ospf_neighbors(config)
    print("\nOSPF Neighbors:")
    for neighbor in ospf_neighbors:
        print(f" - {neighbor}")

print(f"\n{'-'*40}\nParsing complete!\n{'-'*40}")