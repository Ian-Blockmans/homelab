
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

    container = input('container name?')

    if lan == 'l':
        print('        traefik.enable: \"true\"',
        '\n        traefik.http.routers.'+ subdom +'80.entrypoints: \"web\"',
        '\n        traefik.http.routers.'+ subdom +'80.rule: \"Host(`'+ subdom +'.ian.lan`)\"',
        '\n        traefik.http.routers.'+ subdom +'80.tls: \"false"',
        '\n        traefik.http.routers.'+ subdom +'80.middlewares: \"'+ subdom +'-https\"',
        '\n        traefik.http.middlewares.'+ subdom +'-https.redirectscheme.scheme: \"https\"',
        '\n        traefik.http.routers.'+ subdom +'.entrypoints: \"websecure\"',
        '\n        traefik.http.routers.'+ subdom +'.rule: \"Host(`'+ subdom +'.ian.lan`)\"',
        '\n        traefik.http.routers.'+ subdom +'.tls: \"true\"',
        '\n        traefik.http.services.all_'+ container +'.loadbalancer.server.port: \"'+ port +'\"')

    if lan == 'w':
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
        '\n        traefik.http.routers.'+ subdom +'80.entrypoints: \"web\"',
        '\n        traefik.http.routers.'+ subdom +'80.rule: \"Host(`'+ subdom +'.ianb.be`)\"',
        '\n        traefik.http.routers.'+ subdom +'80.tls: \"false\"',
        '\n        traefik.http.routers.'+ subdom +'80.middlewares: \"'+ subdom +'-https\"',
        '\n        traefik.http.middlewares.'+ subdom +'-https.redirectscheme.scheme: \"https\"',
        '\n        traefik.http.routers.'+ subdom +'.entrypoints: \"websecure\"',
        '\n        traefik.http.routers.'+ subdom +'.rule: \"Host(`'+ subdom +'.ianb.be`)\"',
        '\n        traefik.http.routers.'+ subdom +'.tls: \"true\"',
        '\n        traefik.http.routers.'+ subdom +'.tls.certresolver: \"'+ cert +'\"',
        '\n        traefik.http.services.all_'+ container +'.loadbalancer.server.port: \"'+ port +'\"')
    
    if lan == 'b':
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
        '\n        traefik.http.routers.'+ subdom +'80.entrypoints: \"web\"',
        '\n        traefik.http.routers.'+ subdom +'80.rule: \"Host(`'+ subdom +'.ian.lan`)\"',
        '\n        traefik.http.routers.'+ subdom +'80.tls: \"false"',
        '\n        traefik.http.routers.'+ subdom +'80.middlewares: \"'+ subdom +'-https\"',
        '\n        traefik.http.middlewares.'+ subdom +'-https.redirectscheme.scheme: \"https\"',
        '\n        traefik.http.routers.'+ subdom +'.entrypoints: \"websecure\"',
        '\n        traefik.http.routers.'+ subdom +'.rule: \"Host(`'+ subdom +'.ian.lan`)\"',
        '\n        traefik.http.routers.'+ subdom +'.tls: \"true\"',
        '\n\n        traefik.http.routers.'+ subdom +'80r.entrypoints: \"web\"',
        '\n        traefik.http.routers.'+ subdom +'80r.rule: \"Host(`'+ subdom +'.ianb.be`)\"',
        '\n        traefik.http.routers.'+ subdom +'80r.tls: \"false\"',
        '\n        traefik.http.routers.'+ subdom +'80r.middlewares: \"'+ subdom +'-https\"',
        '\n        traefik.http.routers.'+ subdom +'r.entrypoints: \"websecure\"',
        '\n        traefik.http.routers.'+ subdom +'r.rule: \"Host(`'+ subdom +'.ianb.be`)\"',
        '\n        traefik.http.routers.'+ subdom +'r.tls: \"true\"',
        '\n        traefik.http.routers.'+ subdom +'r.tls.certresolver: \"'+ cert +'\"',
        '\n\n        traefik.http.services.all_'+ container +'.loadbalancer.server.port: \"'+ port +'\"')
    
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


