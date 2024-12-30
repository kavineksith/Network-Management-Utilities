# Network Management Python Scripts

This repository contains several Python scripts designed for network administrators and IT professionals. These scripts provide functionalities for managing and analyzing IP addresses, subnets, and network ports. They utilize Object-Oriented Programming (OOP) principles and custom error handling to ensure robust, user-friendly operations.

---

## Contents

1. **CIDR Notation Finder (IPv4 & IPv6)**
2. **IPv4 Address Management Wizard**
3. **IPv6 Address Management Wizard**
4. **Port Analyzer**
5. **Subnet Calculator for IPv4 (Based on Host Count)**
6. **Subnet Calculator for IPv6 (Based on Host Count)**
7. **Subnet Calculator for IPv4 (Based on Network Count)**
8. **Subnet Calculator for IPv6 (Based on Network Count)**

---

## CIDR Notation Finder (IPv4 & IPv6)

### Overview

The CIDR Notation Finder is a Python script designed to assist users in determining the CIDR (Classless Inter-Domain Routing) notation for IPv4 and IPv6 addresses. This tool provides two main functionalities: converting subnet masks to CIDR notation and extracting CIDR notation from given subnets. It is built using Object-Oriented Programming (OOP) principles and custom exceptions for robust, clear, and user-friendly operations.

### Features
- **Subnet Mask Conversion**: Converts a given subnet mask into its corresponding CIDR notation.
- **Subnet Conversion**: Extracts CIDR notation from a specified subnet.
- **Custom Error Handling**: Provides clear and specific error messages for invalid inputs.
- **Interactive Interface**: Command-line interface with user-friendly prompts and results.
- **Supports IPv4 and IPv6**: Works with both IPv4 and IPv6 addresses.

---

## IPv4 Address Management Wizard

### Overview

The IP Address Management Wizard is a comprehensive Python script designed to facilitate the conversion, calculation, and validation of IPv4 addresses and subnet information. It supports multiple address formats and provides detailed information about subnets, network prefixes, and IP address details.

### Features
- **IP Conversion**: Converts IPv4 addresses to decimal, hexadecimal, and binary formats.
- **Subnet Calculation**: Computes network details like network address, broadcast address, subnet mask, host mask, and CIDR notation.
- **Address Validation**: Validates the format, class, and CIDR notation of IPv4 addresses.
- **Usable Host Calculation**: Determines the range and count of usable hosts within a subnet.
- **Screen Management**: Clears the screen for better user experience.
- **Data Display**: Outputs results in a structured, JSON-like format.

---

## IPv6 Address Management Wizard

### Overview

The IPv6 Address Management Wizard is an advanced Python script for analyzing and managing IPv6 addresses. It allows users to convert IPv6 addresses to various formats, perform subnet calculations, and determine details about the address space.

### Features
- **IPv6 Conversion**: Converts IPv6 addresses to hexadecimal, binary, and decimal formats.
- **Subnet Calculation**: Computes network details including network address, broadcast address, subnet mask, and host mask.
- **Address Validation**: Identifies the type and characteristics of the IPv6 address.
- **Address Range Calculation**: Determines the range of usable host IP addresses within a subnet.
- **Screen Management**: Provides functionality to clear the terminal screen.
- **Formatted Output**: Displays results in a structured, JSON-like format.

---

## Port Analyzer

### Overview

The Port Analyzer is a Python script designed to scan TCP, UDP, and ICMP ports on a specified IP address within a given range. It utilizes socket programming to establish connections and retrieve information about the status of ports, services running on those ports, and banners when available.

### Features
- **Port Scanning**: Scans open ports on the specified host for TCP, UDP, and ICMP protocols.
- **Banner Grabbing (TCP)**: Attempts to grab banners for TCP ports by establishing a connection and retrieving service information.

---

## Subnet Calculator for IPv4 (Based on Host Count)

### Overview

The Subnet Calculator is a Python script designed to assist network administrators and IT professionals in calculating and managing IP subnets. It validates IP addresses, computes necessary subnet prefixes, and generates detailed subnet information.

### Features
- **IP Address and Prefix Validation**: Ensures the provided IP address and subnet prefix are valid.
- **Subnet Calculation**: Computes the subnet prefix for a given number of hosts.
- **Subnet Details**: Provides detailed information about each subnet, including network address, host range, broadcast address, subnet mask, and host mask.
- **Network Information**: Displays summary details about the network.

---

## Subnet Calculator for IPv6 (Based on Host Count)

### Overview

The Subnet Calculator IPv6 is a Python script designed to calculate and manage IPv6 subnets. It validates IPv6 addresses, computes necessary subnet prefixes, and generates detailed subnet information.

### Features
- **IPv6 Address Validation**: Checks if the IPv6 address and prefix are valid.
- **Subnet Calculation**: Determines the prefix length needed for a specified number of hosts.
- **Subnet Details**: Outputs detailed information about each subnet, including network address, host range, and subnet mask.
- **Network Information**: Displays summary details about the IPv6 network.

---

## Subnet Calculator for IPv4 (Based on Network Count)

### Overview

The Subnet Calculator for IPv4 is a Python utility that helps network administrators in managing IPv4 networks. It calculates and displays subnet details based on the number of required networks within a given IP address range.

### Features
- **Network Subnetting**: Calculates subnets based on the specified number of networks.
- **Detailed Output**: Provides comprehensive details for each subnet, including network address, first usable IP, last usable IP, broadcast address, subnet mask, and host mask.
- **Validation**: Validates input for IP addresses, network prefixes, and network counts.
- **Error Handling**: Includes custom exceptions for invalid inputs such as incorrect IP formats.

---

## Subnet Calculator for IPv6 (Based on Network Count)

### Overview

The IPv6 Subnet Calculator is a Python script that helps network administrators and engineers calculate IPv6 subnets. By inputting an IPv6 network address and the required number of subnets, users can obtain detailed information about the subnetting process.

### Features
- **IPv6 Address Handling**: Supports IPv6 addresses and calculates subnets based on the network address and prefix.
- **Dynamic Subnet Calculation**: Calculates the necessary prefix length for the required number of subnets.
- **Detailed Output**: Generates detailed subnet information including network address, usable IP ranges, subnet mask, and host mask.
- **Validation**: Ensures the correctness of input data and format.
- **User-Friendly**: Provides prompts and formatted output for better usability.

---

## Installation

**To use any of the scripts, simply clone this repository or download the relevant Python file. Ensure that you have Python 3.x installed on your system. You can install any required dependencies using `pip`.**

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.

