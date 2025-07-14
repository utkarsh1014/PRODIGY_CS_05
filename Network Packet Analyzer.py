Run the following command in your command prompt to install Pillow:
pip install scapy
.
.
.
.
Once Scapy is installed, you can run the script:

 from scapy.all import sniff, IP, Raw

def packet_analysis(packet):
    # Check if packet is IPv4
    if packet.haslayer(IP):
        # Get source and destination IP addresses  
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        # Get protocol
        protocol = packet[IP].proto

        # Check if Raw layer exists
        if packet.haslayer(Raw):
            payload = packet[Raw].load
        else:
            payload = ""  # Set payload to an empty string if not present

        # Print packet information
        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {destination_ip}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {payload}")
        print("--------------------------------")

# Start sniffing
sniff(filter="ip", prn=packet_analysis) 
