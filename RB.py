import requests
import colorama
import time
rs = requests.session()
colorama.init()
B=colorama.Fore
nu,n = 0,0
print(B.RED+F'''

    ____  __________  ____  ____  ______
   / __ \/ ____/ __ \/ __ \/ __ \/_  __/
  / /_/ / __/ / /_/ / / / / /_/ / / /   
 / _, _/ /___/ ____/ /_/ / _, _/ / /    
/_/ |_/_____/_/    \____/_/ 

    __________
   /  _/ ____/
   / // / __  
 _/ // /_/ /  
/___/\____/   

INSTAGRAM : FX_PY3
TELEGRAM :FX_PY

''')
username = input(f'[+] - YOUR USERNAME : ')
password = input(f'[+] - YOUR PASSWORD : ')
Target = input(f'[+] - TARGET USERNAME : ')
url = 'https://www.instagram.com/accounts/login/ajax/'
headers = {
     'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '275',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'bc3d5af829ea',
    'x-requested-with': 'XMLHttpRequest'
    }
data = {
         'username': f'{username}',
         'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
         'queryParams': '{}',
         'optIntoOneTap': 'false'
    }    
r = rs.post(url, headers=headers, data=data)
if  'authenticated":true' in r.text or 'userId' in r.text:
    rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
    print(F'{B.GREEN}LOGIN : {B.WHITE}'+username)
    id=input(f'[+] - TARGET ID : ')
    print('''
[1] - spam
[2] - violence
[3] - Impersonation
[4] - Sexual activity
[5] - harassment
[6] - Self-harm
[7] - Hate on
    ''')
    xx = int(input(f"[+] - Choose : "))
    if xx == 1 :
     q=1
    elif xx == 2 :
     q=5
    elif xx == 3 :
     w=8
    elif xx == 4 :
     q=4
    elif xx == 5 :
     q=7
    elif xx == 6 :
     q=2
    elif xx == 7 :
     q=6
    P1= int(input(f'[+] - HOW MANY REPORT : '))
    tu = int(input(f'[+] - SECONDS : '))
    print('\n\n')
    print(B.CYAN+'='*5+'start'+'='*5)
    print('\n\n')
    for i_1 in range(P1):
     url_1=f'https://www.instagram.com/users/{id}/report/'
     data_1={'source_name':'','reason_id':q,'frx_context':''}
     report_1=rs.post(url_1,data=data_1)
     if '"status":"ok"' in report_1.text:
      nu += 1
     else:
      n += 1
     time.sleep(tu)
     print(f"\rDone={nu} | Error={n}",end="")
      
else :
  print('bad login X ')
