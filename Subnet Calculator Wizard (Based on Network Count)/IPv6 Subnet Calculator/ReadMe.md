# ** IPv6 Subnet Calculator (Based on Network Count) Documentation **

## Overview

The IPv6 Subnet Calculator is a Python script designed to assist network administrators and engineers in calculating IPv6 subnets. By inputting an IPv6 network address and the number of required subnets, users can obtain detailed information about the subnetting process. The tool helps in understanding the distribution of IPv6 addresses, subnet masks, and network configurations essential for designing and managing modern networks.

## Features

- **IPv6 Address Handling**: The script supports IPv6 addresses and provides accurate subnet calculations based on the provided network address and prefix.
- **Dynamic Subnet Calculation**: Calculates the necessary prefix length to accommodate a specified number of subnets.
- **Detailed Output**: Generates comprehensive details for each subnet, including network address, usable IP ranges, subnet mask, and host mask.
- **Validation**: Ensures the correctness of input data, including the validity of the IPv6 address format and prefix length.
- **User-Friendly**: Provides clear prompts for user input and formatted outputs to assist with subnet management.

## Dependencies

The script requires Python 3.x and the following built-in Python libraries:

- **`ipaddress`**: For handling and manipulating IPv6 addresses and networks.
- **`math`**: For performing mathematical operations required in subnet calculations.
- **`re`**: For regular expression operations used in IP address validation.
- **`sys`**: For handling system-specific parameters and exit operations.

These libraries are included with the standard Python distribution, so no additional installation is necessary.

## Usage

To use the IPv6 Subnet Calculator, follow these steps:

1. **Run the Script**: Execute the script using Python from your command line or terminal.
   ```bash
   python ipv6_subnet_calculator.py
   ```

2. **Input Data**:
   - **Network IP Address**: Enter the IPv6 network address along with its prefix (e.g., `2001:db8::/32`).
   - **Number of Networks**: Provide the number of subnets you wish to create.

3. **Review Output**: The script will display a summary of the subnet information and detailed data for each subnet.

## Interactive Commands

Upon running the script, the following interactive commands will be prompted:

1. **Enter Network IP Address**: Input the IPv6 network address with its prefix.
   ```plaintext
   Enter the network IP address with prefix (e.g., 2001:db8::/32):
   ```

2. **Enter Number of Networks**: Specify the number of subnets required.
   ```plaintext
   Enter the number of networks required:
   ```

## Special Commands

The script also handles the following special commands and scenarios:

- **Keyboard Interrupt**: If interrupted by the user (e.g., pressing Ctrl+C), the script will exit gracefully and display a message indicating that the operation was interrupted.
- **Invalid Input Handling**: If the user provides invalid input, such as a non-integer number of networks or an incorrectly formatted IPv6 address, the script will raise appropriate exceptions and provide error messages.

## Conclusion

The IPv6 Subnet Calculator is a powerful and efficient tool for managing and analyzing IPv6 subnets. With its ability to validate input, calculate necessary prefixes, and present detailed subnet information, it is an essential resource for network professionals. By leveraging this script, users can streamline their network design processes, ensuring accurate and effective allocation of IPv6 addresses.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.
