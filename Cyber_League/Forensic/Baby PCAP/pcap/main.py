import pyshark

shark = pyshark.FileCapture("/capture.pcap")
print(shark)