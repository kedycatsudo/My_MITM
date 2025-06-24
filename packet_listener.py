import scapy.all as scapy
from scapy_http import http

def listen_packets(youriface):
    scapy.sniff(iface=youriface,store=False,prn= analyze_packets)#store--> yakalanan
    # paketleri belleğe kaydetmek istemiyoruz çünkü bilgisayarı çok yorar. Bunun yerine paketler geldikçe işleyeceğiz. prn-->callback function
    #prn = callback function --> nereye göndereceğini gösteriyoruz.
def analyze_packets(packet):

    #packet.show()
    if(packet.haslayer(http.HTTPRequest)):#http katmanındaki
        if(packet.haslayer(scapy.Raw)):#Raw katmanındaki
            print("Paketler alınıyor...")
            print(packet[scapy.Raw].load)# load kısmını gösterir.


youriface = input("Dinlemek istediğiniz interface'i giriniz: ")

listen_packets(youriface)


