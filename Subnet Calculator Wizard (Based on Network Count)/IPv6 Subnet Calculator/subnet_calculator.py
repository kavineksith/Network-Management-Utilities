import ipaddress
import math
import re
import sys

# Define custom exceptions
class InvalidNetworkCountError(Exception):
    def __init__(self, message="Number of networks must be at least 1."):
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

class SubnetCalculator:
    def __init__(self, network_ip, num_networks):
        self.network_ip = network_ip
        self.num_networks = num_networks
        self.validate_network_ip()
        self.prefix = self.calculate_prefix_for_networks(num_networks)
        self.network = ipaddress.IPv6Network(network_ip, strict=False)
        self.subnets = list(self.network.subnets(new_prefix=self.prefix))

    def validate_network_ip(self):
        """ Validate if the network IP and prefix form a valid network. """
        try:
            network = ipaddress.IPv6Network(self.network_ip, strict=False)
        except ValueError:
            raise InvalidIPError()
        
        if not (0 <= network.prefixlen <= 128):
            raise InvalidPrefixError()
        
        # Additional validation can be added here if needed
        if not validate_ipv6(self.network_ip.split('/')[0]):
            raise InvalidIPError()

    def calculate_prefix_for_networks(self, num_networks):
        """ Calculate the subnet prefix length required to accommodate the given number of networks. """
        if num_networks < 1:
            raise InvalidNetworkCountError()
        
        required_bits = math.ceil(math.log2(num_networks))
        current_prefix = self.network.prefixlen
        new_prefix = current_prefix + required_bits
        
        if new_prefix > 128:
            raise InvalidPrefixError("Not enough address space to create the requested number of networks.")
        
        return new_prefix

    def format_ip_mask(self, network):
        """ Return the subnet mask and host mask in a human-readable format. """
        subnet_mask = network.network_address
        host_mask = ipaddress.IPv6Address(int(~int(network.network_address)) & (2**128 - 1))
        return subnet_mask, host_mask

    def print_subnet_details(self):
        """ Print subnet details based on network IP and number of networks. """
        print("\nSummary of the Subnet Information:")
        subnet_mask = ipaddress.IPv6Network(f'::/{self.prefix}').network_address
        print(f"Number of Usable Networks: {len(self.subnets)}")
        print(f"Subnet Mask: {subnet_mask}")
        print(f"Prefix: /{self.prefix}")
        
        print("\nComplete List of Subnets:")
        for subnet in self.subnets:
            subnet_mask, host_mask = self.format_ip_mask(subnet)
            first_usable_ip = subnet.network_address + 1
            last_usable_ip = subnet.broadcast_address - 1
            print(f"\nSubnet: {subnet}")
            print(f"Network Address: {subnet.network_address}")
            print(f"First Usable IP: {first_usable_ip}")
            print(f"Last Usable IP: {last_usable_ip}")
            print(f"Broadcast Address: {subnet.broadcast_address}")
            print(f"Subnet Mask: {subnet_mask}")
            print(f"Host Mask: {host_mask}")

    def print_network_info(self):
        """ Display subnet mask and network information for the given IP address with its prefix. """
        subnet_mask, host_mask = self.format_ip_mask(self.network)
        print("\nSummary of the Network Information:")
        print(f"\nNetwork IP: {self.network_ip}")
        print(f"Subnet Mask: {subnet_mask}")
        print(f"Host Mask: {host_mask}")
        print(f"Network Address: {self.network.network_address}")
        print(f"Broadcast Address: {self.network.broadcast_address}")
        print(f"Number of Usable Hosts: {2**(128-self.network.prefixlen) - 2}")

def validate_ipv6(ip):
    """ Validate if the given IP address is a valid IPv6 address. """
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ValueError:
        return False

def main():
    """ Main function to handle user input and print subnet details. """
    try:
        network_ip = input("Enter the network IP address with prefix (e.g., 2001:db8::/32): ").strip()
        num_networks = int(input("Enter the number of networks required: ").strip())
        
        calculator = SubnetCalculator(network_ip, num_networks)
        calculator.print_subnet_details()
        calculator.print_network_info()

    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
        sys.exit(0)
    except ValueError:
        print("\nInvalid input. Please enter a valid number of networks.")
        sys.exit(1)
    except InvalidNetworkCountError as ince:
        print(ince)
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
