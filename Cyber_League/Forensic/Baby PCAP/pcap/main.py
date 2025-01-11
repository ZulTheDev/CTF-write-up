import pyshark

shark = pyshark.FileCapture("capture.pcap", display_filter="dns")
print(shark)