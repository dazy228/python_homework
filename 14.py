
string = b'r\xc3\xa9sum\xc3\xa9'
print(string)

string_decode_utf_8 = string.decode()
print(string_decode_utf_8)

string_encode_Latin1 = string_decode_utf_8.encode('Latin1')
print(string_encode_Latin1)

string_decode_Latin1 = string_encode_Latin1.decode('Latin1')
print(string_decode_Latin1)
