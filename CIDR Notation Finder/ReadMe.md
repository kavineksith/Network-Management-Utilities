# CIDR Notation Finder Documentation

## Overview

The CIDR Notation Finder is a Python script designed to assist users in determining the CIDR (Classless Inter-Domain Routing) notation for IPv4 and IPv6 addresses. This tool provides two main functionalities: converting subnet masks to CIDR notation and extracting CIDR notation from given subnets. By leveraging Object-Oriented Programming (OOP) principles and custom exceptions, this script ensures robust, clear, and user-friendly operations for network professionals and administrators.

## Features

- **Subnet Mask Conversion**: Converts a given subnet mask into its corresponding CIDR notation, which represents the network prefix length.
- **Subnet Conversion**: Extracts the CIDR notation from a specified subnet, displaying the network prefix length directly.
- **Custom Error Handling**: Utilizes custom exceptions to provide clear and specific error messages for invalid inputs.
- **Interactive Interface**: Offers an intuitive command-line interface that prompts users for input and displays results in a user-friendly format.
- **Supports IPv4 and IPv6**: Handles both IPv4 and IPv6 addresses, accommodating a wide range of network configurations.

## Dependencies

This script requires Python 3.x and uses the following standard libraries:

- **`ipaddress`**: For handling and manipulating IP addresses and networks, both IPv4 and IPv6.
- **`sys`**: For handling system-specific parameters and exit operations.

These libraries are included with Python's standard library, so no additional installation is necessary.

## Usage

To use the CIDR Notation Finder script, follow these steps:

1. **Execute the Script**:
   Run the script using Python from the command line or terminal.
   ```bash
   python cidr_notation_finder.py
   ```

2. **Select Functionality**:
   Choose between converting a subnet mask or a subnet by entering the corresponding option (1 or 2).

3. **Provide Input**:
   - For subnet mask conversion: Enter the subnet mask (e.g., `255.255.255.0`).
   - For subnet conversion: Enter the subnet (e.g., `192.168.1.0/24` or `2001:db8::/32`).

4. **View Results**:
   The script will display the CIDR notation corresponding to the input provided.

## Interactive Commands

Upon running the script, you will interact with the following commands:

1. **Select an Option**:
   ```plaintext
   1. Convert Subnet Mask to CIDR Notation
   2. Convert Subnet to CIDR Notation
   Select an option (1 or 2):
   ```

2. **Enter Subnet Mask or Subnet**:
   Depending on the selected option, you will be prompted to input a subnet mask or a subnet.

3. **Results**:
   The script will output the CIDR notation for the provided input.

## Special Commands

The script also handles special scenarios:

- **Invalid Input Handling**:
  - If an invalid subnet mask or subnet format is provided, custom exceptions (`SubnetMaskError` or `SubnetError`) will be raised, and the script will display appropriate error messages.

- **Unexpected Errors**:
  - General exceptions are caught to handle unforeseen errors, ensuring that the script exits gracefully with an error message.

- **Keyboard Interrupt**:
  - If the script is interrupted by the user (e.g., pressing Ctrl+C), it will exit gracefully, ensuring no partial results are left.

## Conclusion

The CIDR Notation Finder script is a versatile tool for network professionals, providing efficient and accurate conversion of subnet masks and subnets to CIDR notation. With its object-oriented design and robust error handling, it offers a reliable solution for network configuration and analysis. This script supports both IPv4 and IPv6, making it suitable for a wide range of networking tasks. By utilizing this tool, users can streamline their network management processes and ensure precise address planning.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.
