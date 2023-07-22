#!/usr/bin/env python
import random
import re
from subprocess import call

'''
    38 is a maximum :( have no idea why I can read 1025 bytes from file via `cat | xargs`

    to reproduce: set NUMBER_OF_HOSTS like 50 and 
        cat my_web_sites.txt | xargs -I {} sh -c "echo {}; openssl s_client -connect {}:443 2>/dev/null | openssl x509 -noout -subject -nameopt lname | echo -n" | wc -l
        cat my_web_sites.txt | xargs -I {} sh -c "echo {}; openssl s_client -connect {}:443 2>/dev/null | openssl x509 -noout -subject -nameopt lname | echo -n" | wc -c
'''
NUMBER_OF_HOSTS = 38
TLD = 'vsfi.org'
KNOWN_HOSTS = [
    'w.who.blue.734.' + TLD,
    't.let.cyan.318.' + TLD,
    'h.the.sky.945.' + TLD,
    'g.dogs.teal.283.' + TLD,
    'e.out.woof.woof.566.' + TLD
]
COLORS = [
    'red',
    'blue',
    'green',
    'purple',
    'pink',
    'brown',
    'black',
    'white',
    'gray',
    'gold',
    'navy',
    'sky',
    'lime',
    'teal',
    'khaki',
    'plum',
    'olive',
    'cyan',
    'beige',
]

WORDS = [
    'empty',
    'floor',
    'grass',
    'issue',
    'enemy',
    'fluid',
    'great',
    'irony',
    'enjoy',
    'focus',
    'green',
    'juice',
    'enter',
    'force',
    'gross',
    'joint',
    'judge',
    'metal',
    'media',
    'newly',
    'known',
    'local',
    'might',
    'noise',
    'label',
    'logic',
    'minor',
    'north',
    'large',
    'loose',
    'minus',
    'noted',
    'laser',
    'lower',
    'mixed',
    'novel',
    'later',
    'lucky',
    'model',
    'nurse',
    'laugh',
    'lunch',
    'money',
    'occur',
    'layer',
    'lying',
    'month',
    'ocean',
    'learn',
    'magic',
    'moral',
    'offer',
    'lease',
    'major',
    'motor',
    'often',
    'least',
    'maker',
    'mount',
    'order',
    'leave',
    'march',
    'mouse',
    'other',
    'legal',
    'music',
    'mouth',
    'ought',
    'level',
    'match',
    'movie',
    'paint',
    'light',
    'mayor',
    'needs',
    'paper',
    'limit',
    'meant',
    'never',
    'party',
    'peace',
    'power',
    'radio',
    'round',
    'panel',
    'press',
    'raise',
    'route',
    'phase',
    'price',
    'range',
    'royal',
    'phone',
    'pride',
    'rapid',
    'rural',
    'photo',
    'prime',
    'ratio',
    'scale'
]


def get_random_host():
    return '.'.join([random.choice(['w', 't', 'h', 'g', 'e']), random.choice(WORDS), random.choice(COLORS), str(random.randint(100, 999)), TLD])


def write_list(arr, filename):
    with open(filename, 'w') as f:
        f.write('\n'.join(arr))
        f.write('\n')


def write_etc_hosts(arr):
    with open('etc_hosts.txt', 'w') as f:
        f.write("\n\n# my sites\n")
        for idx, host in enumerate(arr, start=2):
            ip = '127.0.0.' + str(idx)
            f.write(ip + '  ' + host + "\n")


def write_nginx_conf(arr):
    with open('nginx.conf', 'w') as f:
        for host in arr:
            conf = '''
            server {
            listen MYHOST:80;
            listen MYHOST:443 ssl;
                ssl_certificate        /etc/nginx/certs/MYHOST.cert;
                ssl_certificate_key    /etc/nginx/certs/MYHOST.key;
            }'''
            f.write(re.sub(r"MYHOST", host, conf))


def ca_gen():
    call(['openssl', 'genrsa', '-out', './rootCA.key', '4096'])
    call([
        'openssl',
        'req',
        '-x509',
        '-new',
        '-nodes',
        '-key', './rootCA.key',
        '-sha256',
        '-days',
        '1024',
         '-subj',
         '/CN=Fluffy Kitten',
         '-reqexts',
         'v3_req',
         '-extensions',
         'v3_ca',
         '-out',
         './rootCA.crt'
         ])


def cert_gen(host, country, state, location, org, days):
    call(['openssl',
          'req',
          '-x509',
          '-nodes',
          '-days',
          str(days),
          '-CA',
          'rootCA.crt',
          '-CAkey',
          'rootCA.key',
          '-newkey',
          'rsa:1024',
          '-keyout',
          './{host}.key'.format(host=host),
          '-out',
          './{host}.cert'.format(host=host),
          '-subj',
          '/C={country}/ST={state}/L={location}/O={org}/CN={host}'.format(
              country=country, state=state, location=location, org=org, host=host)
          ])


def cert_gen_arr(arr):
    for host in arr:
        cert_gen(host=host,
                 country='RU',
                 state='Samara',
                 location='Zarechie',
                 org='VSFI Samara',
                 days=random.randint(30, 400)
                 )


if __name__ == '__main__':
    ca_gen()
    hosts = KNOWN_HOSTS.copy()
    for _ in range(0, max(NUMBER_OF_HOSTS - len(KNOWN_HOSTS), 0)):
        hosts.append(get_random_host())

    random.shuffle(hosts)
    write_list(hosts, 'all_hosts.txt')
    write_etc_hosts(hosts)
    write_nginx_conf(hosts)
    cert_gen_arr(hosts)
    # make solvable
    for days, host in enumerate(KNOWN_HOSTS, start=11):
        cert_gen(host, 'RU', 'Samara', 'Ozerki', 'VSFI Samara', days)
