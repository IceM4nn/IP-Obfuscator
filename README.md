# IP Obfuscator
Simple script you can use to convert and obscure any IP address of any host.

Example: https://www.google.com --> http://172.217.24.174

## Usage
```
usage: obfuscate_ip.py [-h] ip_address

positional arguments:
  ip_address  IP address to be obfuscate.

optional arguments:
  -h, --help  show this help message and exit
```

## Example
```
$ ./obfuscate_ip.py 172.217.24.174
[~] Obfuscated IPs:

[+] http://2899908782
[+] http://0xacd918ae
[+] http://025466214256

[+] http://0254.0331.030.0256
[+] http://00000000254.00000000331.0000000030.00000000256
[+] http://0xac.0xd9.0x18.0xae
[+] http://0x00000000ac.0x00000000d9.0x0000000018.0x00000000ae

[+] http://0xac.0xd9.0x18.174
[+] http://0xac.0xd9.24.174
[+] http://0xac.217.24.174
[+] http://172.0xd9.0x18.0xae
[+] http://172.217.0x18.0xae
[+] http://172.217.24.0xae

[+] http://0254.0331.030.174
[+] http://0254.0331.24.174
[+] http://0254.217.24.174
[+] http://172.0331.030.0256
[+] http://172.217.030.0256
[+] http://172.217.24.0256

[+] http://0xac.0xd9.6318
[+] http://0xac.14227630
[+] http://0254.0331.6318
[+] http://0254.14227630
[+] http://0xac.0331.6318
[+] http://0254.0xd9.6318

IPv4 mapping into IPv6 - not resolving as IPv4 do
[+] http://::ffff:acd918ae
[+] http://0:0:0:0:0:ffff:acd918ae
[+] http://0000:0000:0000:0000:0000:ffff:acd918ae
[+] http://0000:0000:0000:0000:0000:ffff:172.217.24.174

```
