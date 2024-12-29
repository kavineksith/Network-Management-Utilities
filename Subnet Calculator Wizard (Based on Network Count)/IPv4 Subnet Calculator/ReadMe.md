# ** IPv4 Subnet Calculator (Based on Network Count) Documentation**

## **Overview**

The **Subnet Calculator** is a Python utility designed to assist network administrators and IT professionals in managing and subdividing IPv4 networks. It provides functionality to calculate and display subnet details based on the number of required networks within a given IP address range. This tool supports the creation of subnets from a specified network and delivers detailed information, including network addresses, broadcast addresses, and usable IP ranges.

## **Features**

- **Network Subnetting**: Calculates and generates subnets based on a specified number of required networks.
- **Detailed Output**: Provides comprehensive details for each subnet, including:
  - Network Address
  - First Usable IP Address
  - Last Usable IP Address
  - Broadcast Address
  - Subnet Mask
  - Host Mask
- **Validation**: Ensures input correctness by validating IP addresses, network prefixes, and required network counts.
- **Error Handling**: Includes custom exceptions to handle invalid input gracefully, including invalid IP formats, prefix lengths, and network counts.

## **Dependencies**

The script relies on the following Python standard libraries:

- `ipaddress`: For managing and manipulating IP addresses and networks.
- `math`: For mathematical operations, particularly logarithmic calculations.
- `re`: For regular expression operations, used for IP address validation.
- `sys`: For system-specific parameters and functions, particularly for handling script exit and errors.

To run the script, ensure you have Python 3.6 or later installed.

## **Usage**

1. **Run the Script**: Execute the script from the command line using:
   ```bash
   python subnet_calculator.py
   ```

2. **Input Prompts**:
   - **Network IP Address with Prefix**: Provide the network IP address and prefix (e.g., `192.168.1.0/24`). This defines the original network range from which subnets will be created.
   - **Number of Networks Required**: Enter the number of subnets you need.

3. **Output**:
   - The script will display detailed information for each created subnet, including addresses and masks.

## **Interactive Commands and Special Commands**

- **Interactive Commands**:
  - Input commands are handled interactively, allowing users to specify the network address and the number of required subnets directly.
  
- **Special Commands**:
  - **Keyboard Interrupt**: Pressing `Ctrl+C` will interrupt the operation and exit the script gracefully with a message indicating that the operation was interrupted by the user.

## **Conclusion**

The **Subnet Calculator** is a powerful and user-friendly tool for network professionals who need to manage and organize IP address space efficiently. By automating the calculation and display of subnet details, it simplifies the process of subnetting, reducing potential errors and saving time. The script's comprehensive validation and error handling ensure reliable and accurate results, making it a valuable addition to any network administrator's toolkit.

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.
