# Subnet Calculator IPv6 Documentation

## Overview

The `Subnet Calculator IPv6` is a Python script designed for network administrators and IT professionals to assist in calculating and managing IPv6 subnets. It provides functionalities to validate IPv6 addresses, compute necessary subnet prefixes for a given number of hosts, and generate detailed information about subnets. This tool facilitates efficient IPv6 network design and management, ensuring that subnets are correctly sized and configured.

## Features

- **IPv6 Address Validation**: Checks if the provided IPv6 address and prefix are valid.
- **Subnet Calculation**: Determines the prefix length needed to accommodate a specified number of hosts in an IPv6 network.
- **Subnet Details**: Outputs comprehensive information about each subnet, including network address, host range, broadcast address, and subnet mask.
- **Network Information**: Displays summary details about the given network, such as network address, broadcast address, subnet mask, and usable hosts.

## Dependencies

The script relies on the following Python modules:

- **`ipaddress`**: Provides functions for creating and manipulating IPv6 networks and addresses.
- **`math`**: Used for mathematical calculations, specifically logarithms.
- **`re`**: Facilitates regular expression operations for IPv6 address validation.
- **`sys`**: Handles system-specific parameters and functions.

Ensure these modules are available in your Python environment. The script is compatible with Python 3.x.

## Usage

To use the `Subnet Calculator IPv6`, follow these steps:

1. **Run the Script**: Execute the script from the command line or your preferred Python environment.
   ```bash
   python subnet_calculator.py
   ```

2. **Provide Inputs**: Enter the network IP address in IPv6 format with prefix (e.g., `2001:db8::/32`) and specify the number of hosts required per subnet when prompted.

3. **Review Output**: The script will print detailed information about the subnets and network based on your inputs.

### Example

```bash
Enter the network IP address with prefix (e.g., 2001:db8::/32): 2001:db8::/32
Enter the number of hosts required per subnet: 100

Summary of the Subnet Information:
Number of Usable Hosts per Subnet: 126
Prefix: /120

Complete List of Subnets:

Subnet: 2001:db8::/120
Network Address: 2001:db8::
Host Range: 2001:db8::1 - 2001:db8::126
Broadcast Address: 2001:db8::127
Subnet Mask: 2001:db8::

...

Summary of the Network Information:

Network IP: 2001:db8::/32
Subnet Mask: 2001:db8::
Network Address: 2001:db8::
Broadcast Address: 2001:db8::ffff:ffff:ffff:ffff
Number of Usable Hosts: 281474976710654
```

## Interactive Commands and Special Commands

- **Interactive Commands**:
  - **Input Network IP Address**: Provide the IPv6 address in CIDR notation.
  - **Input Number of Hosts**: Enter the number of hosts needed per subnet.

- **Special Commands**:
  - **Ctrl+C**: Interrupts the script. The script handles `KeyboardInterrupt` gracefully and exits with a notification.
  - **Invalid Inputs**: The script handles various exceptions, including invalid IPv6 addresses, incorrect subnet prefixes, or non-numeric host counts, and provides appropriate error messages.

## Conclusion

The `Subnet Calculator IPv6` script is a valuable tool for IPv6 network management. It streamlines the process of subnetting by validating input data, calculating required prefixes, and providing detailed subnet and network information. This tool aids in effective network design, helping to ensure optimal use of IPv6 addressing and efficient network configuration. By using this script, users can confidently manage IPv6 subnets and support various networking needs.