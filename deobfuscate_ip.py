#!/usr/bin/env python3
import argparse
import re

def obscured_ip(ip):
    nrofdots = -1
    print('[~] Deobfuscated IP:\n')

    for IPv6 in re.finditer(r'((?P<IPv6>((0{1,5}:){5}([f]{4}|(?P<IPdec>[0-9]{5'
                            '})):|::f{4}:|[0-9f]{24}))|)(?P<ip>[0-9A-Fa-fx.:]+'
                            ')', ip):
        for IPv4 in re.finditer(r'(?P<a>[0-9A-Fa-fx]+):(?P<b>[0-9A-Fa-fx]+)|(?'
                                'P<ip>[0-9A-Fa-fx.]+)', IPv6.group('ip')):
            if IPv4.group('a') and IPv4.group('b'):
                ip = '{}{}'.format(str(hex(int(IPv4.group('a')))),
                                   str(hex(int(IPv4.group('b'))))[2:]) \
                     if IPv6.group('IPdec') \
                     else '0x{}{}'.format(IPv4.group('a'), IPv4.group('b'))
                nrofdots += 1
            else:
                for match in re.finditer(r'(?P<a>([0-9A-Fa-fx]+))',
                                         IPv4.group('ip')):
                    nrofdots += 1
                if nrofdots == 0:
                    if IPv6.group('IPv6'):
                        ip = '0x'+IPv4.group('ip')
                    else:
                        ip = IPv4.group('ip')
                else:
                    ip = IPv4.group('ip')

    if nrofdots == 3:
        for match in re.finditer(r'(?P<a>([0-9A-Fa-fx]+))\.(?P<b>([0-9A-Fa-fx]'
                                 '+))\.(?P<c>([0-9A-Fa-fx]+))\.(?P<d>[0-9A-Fa-'
                                 'fx]+)', ip):
            a, b, c, d = match.group('a'), match.group('b'), \
                         match.group('c'), match.group('d')
            for value in re.finditer(r'(?P<a>^0x[0-9A-Fa-f]+)',
                                     match.group('a')):
                a = (str(int(value.group('a'), 16))) \
                    if int(value.group('a'), 16) < 256 else match.group('a')
            for value in re.finditer(r'(?P<a>^0[0-7]+)', match.group('a')):
                a = (str(int(value.group('a'), 8))) \
                    if int(value.group('a'), 8) < 256 else match.group('a')
            for value in re.finditer(r'(?P<b>^0x[0-9A-Fa-f]+)',
                                     match.group('b')):
                b = (str(int(value.group('b'), 16))) \
                    if int(value.group('b'), 16) < 256 else match.group('b')
            for value in re.finditer(r'(?P<b>^0[0-7]+)', match.group('b')):
                b = (str(int(value.group('b'), 8))) \
                    if int(value.group('b'), 8) < 256 else match.group('b')
            for value in re.finditer(r'(?P<c>^0x[0-9A-Fa-f]+)',
                                     match.group('c')):
                c = (str(int(value.group('c'), 16))) \
                    if int(value.group('c'), 16) < 256 else match.group('c')
            for value in re.finditer(r'(?P<c>^0[0-7]+)', match.group('c')):
                c = (str(int(value.group('c'), 8))) \
                    if int(value.group('c'), 8) < 256 else match.group('c')
            for value in re.finditer(r'(?P<d>^0x[0-9A-Fa-f]+)',
                                     match.group('d')):
                d = (str(int(value.group('d'), 16))) if int(value.group('d'),
                                                            16) < 256 \
                                                     else match.group('d')
            for value in re.finditer(r'(?P<d>^0[0-7]+)', match.group('d')):
                d = (str(int(value.group('d'), 8))) if int(value.group('d'),
                                                           8) < 256 \
                                                    else match.group('d')
            print('[+] '+a+'.'+b+'.'+c+'.'+d)
    elif nrofdots == 2:
        for match in re.finditer(r'(?P<a>([0-9A-Fa-fx]+))\.(?P<b>([0-9A-Fa-fx]'
                                 '+))\.(?P<c>[0-9A-Fa-fx]+)', ip):
            a, b, c = match.group('a'), match.group('b'), match.group('c')
            for value in re.finditer(r'(?P<a>^0[0-7]+)', match.group('a')):
                a = (str(int(value.group('a'), 8))) \
                    if int(value.group('a'), 8) < 256 else match.group('a')
            for value in re.finditer(r'(?P<a>^0x[0-9A-Fa-f]+)',
                                     match.group('a')):
                a = (str(int(value.group('a'), 16))) \
                    if int(value.group('a'), 16) < 256 else match.group('a')
            for value in re.finditer(r'(?P<b>^0[0-7]+)',
                                     match.group('b')):
                b = (str(int(value.group('b'), 8))) \
                    if int(value.group('b'), 8) < 256 else match.group('b')
            for value in re.finditer(r'(?P<b>^0x[0-9A-Fa-f]+)',
                                     match.group('b')):
                b = (str(int(value.group('b'), 16))) \
                    if int(value.group('b'), 16) < 256 else match.group('b')
            for value in re.finditer(r'(?P<c>^0[0-7]+)',
                                     match.group('c')):
                c = (str(int(value.group('c'), 8)))
            for value in re.finditer(r'(?P<c>^0x[0-9A-Fa-f]+)',
                                     match.group('c')):
                c = (str(int(value.group('c'), 16)))
            nr1 = int(int(c)/256)
            nr2 = int(c)-nr1*256
            print('[+] '+a+'.'+b+'.'+str(nr1)+'.'+str(nr2))
    elif nrofdots == 1:
        for match in re.finditer(r'(?P<a>([0-9A-Fa-fx]+))\.(?P<b>[0-9A-Fa-fx]+'
                                 ')', ip):
            a, b = match.group('a'), match.group('b')
            for value in re.finditer(r'(?P<a>^0x[0-9A-Fa-f]+)',
                                     match.group('a')):
                a = (str(int(value.group('a'), 16))) \
                    if int(value.group('a'), 16) < 256 else match.group('a')
            for value in re.finditer(r'(?P<a>^0[0-7]+)',
                                     match.group('a')):
                a = (str(int(value.group('a'), 8))) \
                    if int(value.group('a'), 8) < 256 else match.group('a')
            for value in re.finditer(r'(?P<b>^0x[0-9A-Fa-f]+)',
                                     match.group('b')):
                b = (str(int(value.group('b'), 16)))
            for value in re.finditer(r'(?P<b>^0[0-7]+)', match.group('b')):
                b = (str(int(value.group('b'), 8)))
            nr1 = int(int(b)/256**2)
            nr2 = int(b)-nr1*256**2
            nr3 = int(nr2/256)
            nr4 = nr2-nr3*256
            print('[+] '+a+'.'+str(nr1)+'.'+str(nr3)+'.'+str(nr4))
    elif nrofdots == 0:
        for match in re.finditer(r'(?P<a>([0-9A-Fa-fx]+))', ip):
            a = match.group('a')
            for value in re.finditer(r'(?P<a>^0[0-7]+)', match.group('a')):
                a = int(value.group('a'), 8)
            for value in re.finditer(r'(?P<a>^0x[0-9A-Fa-f]+)',
                                     match.group('a')):
                a = int(value.group('a'), 16)
            nr1 = int(int(a)/256**3)
            nr2 = int(a)-nr1*256**3
            nr3 = int(nr2/256**2)
            nr4 = nr2-nr3*256**2
            nr5 = int(nr4/256)
            nr6 = nr4-nr5*256
            print('[+] '+str(nr1)+'.'+str(nr3)+'.'+str(nr5)+'.'+str(nr6))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IP deobfuscator')
    parser.add_argument('ip_address', help='Obfuscated IP of any valid value (e.g.'
    ' \'0xd83ad424\')')
    args = parser.parse_args()
    if args.ip_address:
        obscured_ip(args.ip_address)
    else:
        parser.print_help()
