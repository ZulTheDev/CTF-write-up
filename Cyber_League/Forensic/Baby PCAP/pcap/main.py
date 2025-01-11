from scapy.all import rdpcap, DNSQR

# Load the PCAP file
pcap_file_path = 'capture.pcap'  # Replace with the path to your file
packets = rdpcap(pcap_file_path)

# Filter DNS packets and check for the specific query
dns_queries = []
target_domain = "173.18.0.2"
for packet in packets:
    if packet.haslayer(DNSQR) and packet[DNSQR].qname.decode('utf-8').strip('.') == target_domain:
        dns_queries.append(packet)

# Print results
print(f"Number of packets matching the domain '{target_domain}': {len(dns_queries)}")
for pkt in dns_queries:
    pkt.show()


#GPT generated one hahahahaha