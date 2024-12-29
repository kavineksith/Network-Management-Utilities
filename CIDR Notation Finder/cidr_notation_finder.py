import ipaddress
import sys

# Define custom exceptions
class SubnetMaskError(Exception):
    def __init__(self, message="Invalid subnet mask format."):
        self.message = message
        super().__init__(self.message)

class SubnetError(Exception):
    def __init__(self, message="Invalid subnet format."):
        self.message = message
        super().__init__(self.message)

class CIDRConverter:
    def __init__(self):
        pass

    def convert_subnet_mask(self, subnet_mask):
        """ Convert subnet mask to CIDR notation (prefix length). """
        try:
            # Create an IP network with the given subnet mask
            network = ipaddress.ip_network(f'0.0.0.0/{subnet_mask}', strict=False)
            return network.prefixlen
        except ValueError:
            raise SubnetMaskError()

    def convert_subnet(self, subnet):
        """ Extract CIDR notation from a given subnet. """
        try:
            # Parse the subnet to get the prefix length
            network = ipaddress.ip_network(subnet, strict=False)
            return network.prefixlen
        except ValueError:
            raise SubnetError()

def main():
    """ Main function to handle user input and display CIDR notation. """
    converter = CIDRConverter()
    
    print("CIDR Notation Finder")
    print("--------------------")
    
    print("1. Convert Subnet Mask to CIDR Notation")
    print("2. Convert Subnet to CIDR Notation")
    choice = input("Select an option (1 or 2): ").strip()
    
    try:
        if choice == '1':
            subnet_mask = input("Enter the subnet mask (e.g., 255.255.255.0): ").strip()
            prefix_len = converter.convert_subnet_mask(subnet_mask)
            print(f"CIDR Notation: /{prefix_len}")
        
        elif choice == '2':
            subnet = input("Enter the subnet (e.g., 192.168.1.0/24 or 2001:db8::/32): ").strip()
            prefix_len = converter.convert_subnet(subnet)
            print(f"CIDR Notation: /{prefix_len}")
        
        else:
            print("Invalid choice. Please select 1 or 2.")
    
    except SubnetMaskError as sme:
        print(f"Error: {sme}")
    except SubnetError as se:
        print(f"Error: {se}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        sys.exit(0)

if __name__ == "__main__":
    main()
