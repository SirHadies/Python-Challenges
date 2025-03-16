import random
import ipaddress

#let's make a bunch of random IP's. 
def generate_random_ipv4():
    while True:
        ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 155)}"
        if not ipaddress.IPv4Address(ip).is_reserved:
            return ip

random_ip = generate_random_ipv4()
#print(random_ip * 10)

#add IP's to a blank list. 
def list_addition():
    blank_list = []
    place_holder = 0
    while place_holder <= 20:
        ip = f"10.15.{random.randint(0, 255)}.{random.randint(0, 155)}"
        blank_list.append(ip)
        place_holder += 1
    return blank_list

ip_list = list_addition()
ip_list.sort()
print(ip_list)

test = type(ip_list[0])
print(test)