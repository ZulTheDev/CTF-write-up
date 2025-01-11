from scapy.all import rdpcap

# Load the PCAP file
pcap_file_path = 'capture.pcap'  # Replace with your file's path
packets = rdpcap(pcap_file_path)

# Extract and print hexadecimal data for each packet
with open("hex_dump.txt", "w") as f:
    for i, pkt in enumerate(packets):
        hex_data = bytes(pkt).hex()
        f.write(f"Packet {i + 1}:\n{hex_data}\n\n")
print("Hexadecimal data has been written to 'hex_dump.txt'")
