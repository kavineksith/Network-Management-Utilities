# Subnet Calculator Documentation

## Overview

The `Subnet Calculator` is a Python script designed to assist network administrators and IT professionals in calculating and managing IP subnets. It provides functionalities to validate IP addresses, determine subnet masks, calculate required subnet prefixes for a given number of hosts, and generate detailed information about subnets. This tool is crucial for efficient network design and management, ensuring that subnets are appropriately sized and configured according to specific requirements.

## Features

- **IP Address and Prefix Validation**: Ensures the provided IP address and subnet prefix are valid and form a proper network.
- **Subnet Calculation**: Computes the subnet prefix required to accommodate a specified number of hosts.
- **Subnet Details**: Provides detailed information about each subnet, including network address, host range, broadcast address, subnet mask, and host mask.
- **Network Information**: Displays summary details of the provided network, including network address, broadcast address, subnet mask, and usable hosts.

## Dependencies

This script requires the following Python modules:
- `ipaddress`: To handle and manipulate IP addresses and networks.
- `math`: For mathematical operations such as logarithms.
- `re`: For regular expressions used in IP validation.
- `sys`: For handling system-specific parameters and functions.

Ensure these modules are available in your Python environment. The script is compatible with Python 3.x.

## Usage

To use the `Subnet Calculator`, follow these steps:

1. **Run the Script**: Execute the script in a Python environment.
   ```bash
   python subnet_calculator.py
   ```

2. **Provide Inputs**: When prompted, enter the network IP address in CIDR notation (e.g., `192.168.1.0/24`) and the number of hosts required per subnet.

3. **Review Output**: The script will print detailed information about the subnets and network based on your inputs.

### Example

```bash
Enter the network IP address with prefix (e.g., 192.168.1.0/24): 192.168.1.0/24
Enter the number of hosts required per subnet: 50

Summary of the Subnet Information:
Number of Usable Hosts per Subnet: 62
Subnet Mask: 255.255.255.192
Prefix: /26

Complete List of Subnets:

Subnet: 192.168.1.0/26
Network Address: 192.168.1.0
Host Range: 192.168.1.1 - 192.168.1.62
Broadcast Address: 192.168.1.63
Subnet Mask: 255.255.255.192
Host Mask: 0.0.0.63

...

Summary of the Network Information:

Network IP: 192.168.1.0/24
Subnet Mask: 255.255.255.0
Host Mask: 0.0.0.255
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
Number of Usable Hosts: 254
```

## Interactive Commands and Special Commands

- **Interactive Commands**:
  - **Input Network IP Address**: Enter the IP address in CIDR format.
  - **Input Number of Hosts**: Specify the number of hosts required per subnet.

- **Special Commands**:
  - **Ctrl+C**: Interrupt the script. The script handles `KeyboardInterrupt` gracefully and exits with a message.
  - **Invalid Inputs**: The script will prompt error messages and exit if invalid data is entered, such as an incorrect IP address format, an invalid subnet prefix, or a non-numeric host count.

## Conclusion

The `Subnet Calculator` script is a robust tool for calculating and managing IP subnets. It simplifies the process of subnetting by validating inputs, calculating necessary prefixes, and providing comprehensive subnet information. This tool is essential for network configuration tasks, helping ensure optimal network performance and efficient use of IP addresses. Proper usage of this script will aid in effective network design and management, catering to varying requirements of host counts and subnet structures.