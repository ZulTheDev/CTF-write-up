import pydicom 
source = pydicom.dcmread("challenge.dcm", force=True)
# print(source)

dicom_byte = [
    b'f\x00\x00\x00', b'6\x00\x00\x00', b'3\x00\x00\x00', b'a\x00\x00\x00', b'c\x00\x00\x00', b'd\x00\x00\x00',
    b'3\x00\x00\x00', b'b\x00\x00\x00', b'7\x00\x00\x00', b'8\x00\x00\x00', b'1\x00\x00\x00', b'2\x00\x00\x00',
    b'7\x00\x00\x00', b'c\x00\x00\x00', b'1\x00\x00\x00', b'd\x00\x00\x00', b'7\x00\x00\x00', b'd\x00\x00\x00',
    b'3\x00\x00\x00', b'e\x00\x00\x00', b'7\x00\x00\x00', b'0\x00\x00\x00', b'0\x00\x00\x00', b'b\x00\x00\x00',
    b'5\x00\x00\x00', b'5\x00\x00\x00', b'6\x00\x00\x00', b'6\x00\x00\x00', b'5\x00\x00\x00', b'3\x00\x00\x00',
    b'5\x00\x00\x00', b'4\x00\x00\x00']

dicom_array = [25, 10, 0, 3, 17, 19, 23, 27, 4, 13, 20, 8, 24, 21, 31, 15, 7, 29, 6, 1, 9, 30, 22, 5, 28, 18, 26, 11, 2, 14, 16, 12]

for i in dicom_array:
    base = dicom_byte[i].decode('utf-8').split('\x00')
    print(f"{"".join(base)}")