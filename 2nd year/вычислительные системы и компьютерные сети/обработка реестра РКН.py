import socket
from urllib.parse import urlparse

def get_dom(url):
    return urlparse(url).netloc

def get_ip(dom):
    try:
        ip = socket.gethostbyname(dom)
    except:
        return 'Not found'
    return ip
    
def check_block():
    site_url = str(input('Введите ссылку для проверки: '))
    blocked = False
    with open('blockedlist (1).txt', 'r', encoding='utf-8') as file:
        txt = file.readline()
        # print(txt)
        for lines in txt:
            elem = lines.strip().split(', ')
            url = elem[0].split(',')
            if site_url == url:
                blocked = True
                break
    if blocked:
        print(f'{site_url} заблокирован, к сожалению' )
    else:
        print(f'{site_url} нетронут, можно заходить на него')

check_block()