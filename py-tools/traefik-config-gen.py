import re

def main():
    repeat = 1
    while repeat == 1:

        lan = 'na'
        while lan != 'l' and lan != 'w' and lan != 'b':
            lan = input('lan wan or both?[l/w/b]')
            if lan != 'l' and lan != 'w' and lan != 'b':
                print('not l, w or b. ')
        subdom = input('subdomain name?')

        validport = 0
        while validport == 0:
            port = input('port?')
            if port.isdigit():
                if int(port) < 1 or  int(port) > 65535:
                    print('not valid port number')
                else: 
                    validport = 1
            else: 
                print('not a number')

        config = 'na'
        while config != 'c' and config != 'f':
            config = input('container or file?[c/f]')
            if config != 'c' and config != 'f':
                print('not c or f.')



        if config == 'c':
            ContainerName = input('container name?')
            container(lan,port,subdom,ContainerName)
        else:
            ip = 'na'
            IpCheck = ''
            IpRegex = re.compile(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$")
            while not IpCheck:
                ip = input('ip adress of service?')
                IpCheck = IpRegex.search(ip)
                if not IpCheck:
                    print('not a valid ip adress.')

            file(lan,port,ip,subdom)


        repeatf = 'na'
        while repeatf != 'y' and repeatf != 'n':
            repeatf = input('again?[y/n]')
            if repeatf != 'y' and repeatf != 'n':
                print('not y or n. ')
            if repeatf == 'y':
                repeat = 1
            else:
                if repeatf == 'n':
                    repeat = 0

def file(net, port, ip, subdomain):
    if net == 'l':
        print('\n\nhttp:\n  routers:')
        print('    '+ subdomain +'Lan80:',
            '\n      entrypoints: \"web\"',
            '\n      middlewares:',
            '\n      - \"https-redirect\"',
            '\n      rule: \"Host(`'+ subdomain +'.ian.lan`)\"',
            '\n      service: '+ subdomain +'',
            '\n    '+ subdomain +'Lan443:',
            '\n      entrypoints: \"websecure\"',
            '\n      rule: \"Host(`'+ subdomain +'.ian.lan`)\"',
            '\n      tls: \"true\"',
            '\n      service: '+ subdomain +'')

    if net == 'w':
        prod = 'na'
        while prod != 'p' and prod != 's':
            prod = input('production or staging?[p or s]')
            if prod == 'p':
                cert = 'production'
            else: 
                if prod == 's':
                    cert = 'staging'
                else:
                    print('not p or s. ')

        print('\n\nhttp:\n  routers:')
        print('    '+ subdomain +'Wan80:',
            '\n      entrypoints: \"web\"',
            '\n      middlewares:',
            '\n      - \"https-redirect\"',
            '\n      rule: \"Host(`'+ subdomain +'.ianb.be`)\"',
            '\n      service: '+ subdomain +'',
            '\n    '+ subdomain +'Wan443:',
            '\n      entrypoints: \"websecure\"',
            '\n      rule: \"Host(`'+ subdomain +'.ianb.be`)\"',
            '\n      tls:',
            '\n      certResolver: \"'+ cert +'\"',
            '\n      service: '+ subdomain +'')
    
    if net == 'b':
        prod = 'na'
        while prod != 'p' and prod != 's':
            prod = input('production or staging?[p or s]')
            if prod == 'p':
                cert = 'production'
            else: 
                if prod == 's':
                    cert = 'staging'
                else:
                    print('not p or s. ')
        
        print('\n\nhttp:\n  routers:')
        print('    '+ subdomain +'Lan80:',
            '\n      entrypoints: \"web\"',
            '\n      middlewares:',
            '\n      - \"https-redirect\"',
            '\n      rule: \"Host(`'+ subdomain +'.ian.lan`)\"',
            '\n      service: '+ subdomain +'',
            '\n    '+ subdomain +'Lan443:',
            '\n      entrypoints: \"websecure\"',
            '\n      rule: \"Host(`'+ subdomain +'.ian.lan`)\"',
            '\n      tls: \"true\"',
            '\n      service: '+ subdomain +'\n')
        print('    '+ subdomain +'Wan80:',
            '\n      entrypoints: \"web\"',
            '\n      middlewares:',
            '\n      - \"https-redirect\"',
            '\n      rule: \"Host(`'+ subdomain +'.ianb.be`)\"',
            '\n      service: '+ subdomain +'',
            '\n    '+ subdomain +'Wan443:',
            '\n      entrypoints: \"websecure\"',
            '\n      rule: \"Host(`'+ subdomain +'.ianb.be`)\"',
            '\n      tls:',
            '\n      certResolver: \"'+ cert +'\"',
            '\n      service: '+ subdomain +'')
    
    print('\n\n  services:',
          '\n    '+ subdomain +':',
          '\n      loadBalancer:',
          '\n        servers:',
          '\n        - url: http://'+ ip +':'+ port +'/')

def container(net, port, subdomain, cname):
    if net == 'l':
        print('        traefik.enable: \"true\"',
        '\n        traefik.http.routers.'+ subdomain +'80.entrypoints: \"web\"',
        '\n        traefik.http.routers.'+ subdomain +'80.rule: \"Host(`'+ subdomain +'.ian.lan`)\"',
        '\n        traefik.http.routers.'+ subdomain +'80.tls: \"false"',
        '\n        traefik.http.routers.'+ subdomain +'80.middlewares: \"'+ subdomain +'-https\"',
        '\n        traefik.http.middlewares.'+ subdomain +'-https.redirectscheme.scheme: \"https\"',
        '\n        traefik.http.routers.'+ subdomain +'.entrypoints: \"websecure\"',
        '\n        traefik.http.routers.'+ subdomain +'.rule: \"Host(`'+ subdomain +'.ian.lan`)\"',
        '\n        traefik.http.routers.'+ subdomain +'.tls: \"true\"',
        '\n        traefik.http.services.all_'+ cname +'.loadbalancer.server.port: \"'+ port +'\"')

    if net == 'w':
        prod = 'na'
        while prod != 'p' and prod != 's':
            prod = input('production or staging?[p or s]')
            if prod == 'p':
                cert = 'production'
            else: 
                if prod == 's':
                    cert = 'staging'
                else:
                    print('not p or s. ')

        print('        traefik.enable: \"true\"',
        '\n        traefik.http.routers.'+ subdomain +'80.entrypoints: \"web\"',
        '\n        traefik.http.routers.'+ subdomain +'80.rule: \"Host(`'+ subdomain +'.ianb.be`)\"',
        '\n        traefik.http.routers.'+ subdomain +'80.tls: \"false\"',
        '\n        traefik.http.routers.'+ subdomain +'80.middlewares: \"'+ subdomain +'-https\"',
        '\n        traefik.http.middlewares.'+ subdomain +'-https.redirectscheme.scheme: \"https\"',
        '\n        traefik.http.routers.'+ subdomain +'.entrypoints: \"websecure\"',
        '\n        traefik.http.routers.'+ subdomain +'.rule: \"Host(`'+ subdomain +'.ianb.be`)\"',
        '\n        traefik.http.routers.'+ subdomain +'.tls: \"true\"',
        '\n        traefik.http.routers.'+ subdomain +'.tls.certresolver: \"'+ cert +'\"',
        '\n        traefik.http.services.all_'+ cname +'.loadbalancer.server.port: \"'+ port +'\"')
    
    if net == 'b':
        prod = 'na'
        while prod != 'p' and prod != 's':
            prod = input('production or staging?[p or s]')
            if prod == 'p':
                cert = 'production'
            else: 
                if prod == 's':
                    cert = 'staging'
                else:
                    print('not p or s. ')

        print('        traefik.enable: \"true\"',
        '\n        traefik.http.routers.'+ subdomain +'80.entrypoints: \"web\"',
        '\n        traefik.http.routers.'+ subdomain +'80.rule: \"Host(`'+ subdomain +'.ian.lan`)\"',
        '\n        traefik.http.routers.'+ subdomain +'80.tls: \"false"',
        '\n        traefik.http.routers.'+ subdomain +'80.middlewares: \"'+ subdomain +'-https\"',
        '\n        traefik.http.middlewares.'+ subdomain +'-https.redirectscheme.scheme: \"https\"',
        '\n        traefik.http.routers.'+ subdomain +'.entrypoints: \"websecure\"',
        '\n        traefik.http.routers.'+ subdomain +'.rule: \"Host(`'+ subdomain +'.ian.lan`)\"',
        '\n        traefik.http.routers.'+ subdomain +'.tls: \"true\"',
        '\n\n        traefik.http.routers.'+ subdomain +'80r.entrypoints: \"web\"',
        '\n        traefik.http.routers.'+ subdomain +'80r.rule: \"Host(`'+ subdomain +'.ianb.be`)\"',
        '\n        traefik.http.routers.'+ subdomain +'80r.tls: \"false\"',
        '\n        traefik.http.routers.'+ subdomain +'80r.middlewares: \"'+ subdomain +'-https\"',
        '\n        traefik.http.routers.'+ subdomain +'r.entrypoints: \"websecure\"',
        '\n        traefik.http.routers.'+ subdomain +'r.rule: \"Host(`'+ subdomain +'.ianb.be`)\"',
        '\n        traefik.http.routers.'+ subdomain +'r.tls: \"true\"',
        '\n        traefik.http.routers.'+ subdomain +'r.tls.certresolver: \"'+ cert +'\"',
        '\n\n        traefik.http.services.all_'+ cname +'.loadbalancer.server.port: \"'+ port +'\"')

if __name__ == '__main__':
    main()