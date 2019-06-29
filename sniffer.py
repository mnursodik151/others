import socket
import struct
from scapy.all import *

print("mulai")
dict_syn = {}


def handle_packet(packet):
    if TCP in packet :
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        if packet[TCP].flags == "S" :
            if dst_port in dict_syn :
                dict_syn[dst_port]+=1
                if dict_syn[dst_port] >= 100 :
                    print("kemungkinan syn flood jumlah paket syn menuju port yang sama : "+ str(dict_syn[dst_port]))
                    print("Paket dari IP "+src_ip+" ke "+dst_ip+" src_port "+str(src_port)+" d_port "+str(dst_port))
            else :
                dict_syn[dst_port] = 0
                dict_syn[dst_port]+= 1
                print("Paket dari IP "+src_ip+" ke "+dst_ip+" src_port "+str(src_port)+" d_port "+str(dst_port))
    else :
        print("Bukan paket TCP")


sniff(filter="ip.addr==192.168.1.2 && tcp", prn=handle_packet)
