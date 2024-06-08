import subprocess
import re
import random

def get_random_mac():
    """Generate a random MAC address."""
    return "02:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def get_current_mac(interface):
    """Get the current MAC address of the specified interface."""
    try:
        output = subprocess.check_output(["ifconfig", interface], text=True)
        mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", output)
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print("Could not read MAC address.")
    except subprocess.CalledProcessError:
        print("Could not execute ifconfig.")

def change_mac(interface, new_mac):
    """Change the MAC address for the specified interface."""
    print(f"Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print(f"MAC address for {interface} has been changed to {new_mac}")

# Example usage:
# Replace 'eth0' with your network interface name
interface = "eth0"
current_mac = get_current_mac(interface)
print(f"Current MAC: {current_mac}")

new_mac = get_random_mac()
change_mac(interface, new_mac)
