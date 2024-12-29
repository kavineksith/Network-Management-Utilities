# IP Address Management Wizard Documentation

## Overview
The **IP Address Management Wizard** is a comprehensive Python script designed to facilitate the conversion, calculation, and validation of IP addresses and subnet information. This tool supports IPv4 addresses, allowing users to compute various details such as decimal and hexadecimal representations, binary formats, subnet addresses, and more. It features robust error handling and a user-friendly command-line interface for interaction. The script also includes functionality for screen management and data display, making it a versatile tool for network administrators and IT professionals.

## Features
- **IP Conversion**: Converts IPv4 addresses to decimal, hexadecimal, and binary formats.
- **Subnet Calculation**: Computes subnet details including network address, broadcast address, subnet mask, host mask, and CIDR notation.
- **Address Validation**: Validates the format and class of IPv4 addresses, and checks CIDR notation.
- **Usable Host Calculation**: Determines the range and count of usable hosts within a subnet.
- **Screen Management**: Clears the screen for better user experience.
- **Data Display**: Outputs results in a formatted JSON-like structure for easy readability.

## Dependencies
- **Python 3.x**: The script is compatible with Python 3.x.
- **`ipaddress`**: Provides utilities for working with IPv4 addresses and subnets.
- **`json`**: Used for formatting and displaying data in JSON format.
- **`os`**: Handles system-specific operations such as clearing the screen.
- **`sys`**: Manages command-line arguments and system exit operations.
- **`time`**: Provides functions for managing delays and pauses.

## Usage
1. **Run the Script**
   Execute the script from the command line:

   ```
   python ip_management_wizard.py
   ```

2. **Interactive Commands**
   - **Enter IP Address and CIDR Notation**: Input an IPv4 address and CIDR notation in the format `192.168.1.1/24` to process and display related information.
   - **Clear Screen**: Type `clear` to clear the screen and reset the view.
   - **Exit**: Type `exit` to terminate the script and exit the application.

3. **Special Commands**
   - **Clear Screen**: Input `clear` to clear the current terminal screen.
   - **Exit**: Input `exit` to end the script and close the application gracefully.

## Conclusion
The **IP Address Management Wizard** provides a powerful and user-friendly solution for managing and analyzing IPv4 addresses and subnets. Its functionality includes detailed conversions, subnet calculations, and address validations, all integrated into a seamless command-line interface. With robust error handling and clear data presentation, this tool is well-suited for educational purposes, network administration, and IT support tasks. While designed for educational and practical use, it is recommended to be utilized within its intended scope for optimal effectiveness.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.