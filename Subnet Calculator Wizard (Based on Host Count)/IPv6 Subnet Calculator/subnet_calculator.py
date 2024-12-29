import ipaddress
import math
import re
import sys

# Define custom exceptions
class InvalidHostCountError(Exception):
    def __init__(self, message="Number of hosts must be at least 1."):
        self.message = message
        super().__init__(self.message)

class InvalidIPError(Exception):
    def __init__(self, message="Invalid IP address format."):
        self.message = message
        super().__init__(self.message)

class InvalidPrefixError(Exception):
    def __init__(self, message="Invalid subnet prefix. Prefix must be between 0 and 128."):
        self.message = message
        super().__init__(self.message)

class InvalidNetworkError(Exception):
    def __init__(self, message="The IP address and prefix do not form a valid network."):
        self.message = message
        super().__init__(self.message)

class SubnetCalculatorIPv6:
    def __init__(self, network_ip, num_hosts):
        self.network_ip = network_ip
        self.num_hosts = num_hosts
        self.validate_network_ip()
        self.prefix = self.calculate_prefix_for_hosts(num_hosts)
        self.network = ipaddress.IPv6Network(network_ip, strict=False)
        self.subnets = list(self.network.subnets(new_prefix=self.prefix))

    def validate_network_ip(self):
        """ Validate if the network IP and prefix form a valid network. """
        if not validate_ipv6(self.network_ip.split('/')[0]):
            raise InvalidIPError()
        
        try:
            network = ipaddress.IPv6Network(self.network_ip, strict=False)
        except ValueError:
            raise InvalidNetworkError()
        
        if not (0 <= network.prefixlen <= 128):
            raise InvalidPrefixError()

    def calculate_prefix_for_hosts(self, num_hosts):
        """ Calculate the subnet prefix length required to accommodate the given number of hosts. """
        if num_hosts < 1:
            raise InvalidHostCountError()
        
        # For IPv6, calculate prefix to accommodate the given number of hosts.
        prefix = 128 - math.ceil(math.log2(num_hosts + 2))
        return min(max(prefix, 0), 128)

    def format_ip_mask(self, network):
        """ Return the subnet mask in a human-readable format. """
        # IPv6 doesn't have a "host mask" like IPv4, so we only return the prefix length
        return network.network_address

    def print_subnet_details(self):
        """ Print subnet details based on network IP and number of hosts per subnet. """
        num_hosts_per_subnet = 2**(128 - self.prefix) - 2
        print("\nSummary of the Subnet Information:")
        print(f"Number of Usable Hosts per Subnet: {num_hosts_per_subnet}")
        print(f"Prefix: /{self.prefix}")
        
        print("\nComplete List of Subnets:")
        for subnet in self.subnets:
            subnet_mask = self.format_ip_mask(subnet)
            print(f"\nSubnet: {subnet}")
            print(f"Network Address: {subnet.network_address}")
            print(f"Host Range: {subnet.network_address + 1} - {subnet.broadcast_address - 1}")
            print(f"Broadcast Address: {subnet.broadcast_address}")
            print(f"Subnet Mask: {subnet_mask}")

    def print_network_info(self):
        """ Display subnet mask and network information for the given IP address with its prefix. """
        subnet_mask = self.format_ip_mask(self.network)
        num_hosts = 2**(128 - self.network.prefixlen) - 2
        print("\nSummary of the Network Information:")
        print(f"\nNetwork IP: {self.network_ip}")
        print(f"Subnet Mask: {subnet_mask}")
        print(f"Network Address: {self.network.network_address}")
        print(f"Broadcast Address: {self.network.broadcast_address}")
        print(f"Number of Usable Hosts: {num_hosts}")

def validate_ipv6(ip):
    """ Validate if the given IP address is a valid IPv6 address. """
    # Regular expression pattern for IPv6
    pattern = re.compile(r'^(?:[0-9a-fA-F]{1,4}:){7}(?:[0-9a-fA-F]{1,4}|[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}|::)$|^(?:[0-9a-fA-F]{1,4}:){1,7}:$|^(?:[0-9a-fA-F]{1,4}:){1,6}:(?:[0-9a-fA-F]{1,4}|[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}|::)$|^(?:[0-9a-fA-F]{1,4}:){1,5}:(?:[0-9a-fA-F]{1,4}|[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}|::)$|^(?:[0-9a-fA-F]{1,4}:){1,4}:(?:[0-9a-fA-F]{1,4}|[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}|::)$|^(?:[0-9a-fA-F]{1,4}:){1,3}:(?:[0-9a-fA-F]{1,4}|[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}|::)$|^(?:[0-9a-fA-F]{1,4}:){1,2}:(?:[0-9a-fA-F]{1,4}|[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}|::)$|^(?:[0-9a-fA-F]{1,4}:)(?:[0-9a-fA-F]{1,4}|[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}|::)$|^(::)(?:[0-9a-fA-F]{1,4}|[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4})$')
    return pattern.match(ip) is not None

def main():
    """ Main function to handle user input and print subnet details. """
    try:
        network_ip = input("Enter the network IP address with prefix (e.g., 2001:db8::/32): ")
        num_hosts = int(input("Enter the number of hosts required per subnet: "))
        
        calculator = SubnetCalculatorIPv6(network_ip, num_hosts)
        calculator.print_subnet_details()
        calculator.print_network_info()

    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
        sys.exit(0)
    except ValueError:
        print("\nInvalid input. Please enter a valid number of hosts.")
        sys.exit(1)
    except InvalidHostCountError as ihce:
        print(ihce)
        sys.exit(1)
    except InvalidIPError as ipe:
        print(ipe)
        sys.exit(1)
    except InvalidPrefixError as ipxe:
        print(ipxe)
        sys.exit(1)
    except InvalidNetworkError as ine:
        print(ine)
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)
