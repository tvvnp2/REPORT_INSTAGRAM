import requests
import colorama
import time
rs = requests.session()
colorama.init()
B=colorama.Fore

nu,n = 0,0
print(B.RED+F'''

██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

██╗ ██████╗ 
██║██╔════╝ 
██║██║  ███╗
██║██║   ██║
██║╚██████╔╝
╚═╝ ╚═════╝ 
{B.CYAN}            
INSTAGRAM : FX_PY3
TELEGRAM :FX_PY

''')
username = input(f'{B.YELLOW}[{B.WHITE}+{B.YELLOW}]{B.WHITE} - YOUR USERNAME : {B.RED}')
password = input(f'{B.YELLOW}[{B.WHITE}+{B.YELLOW}]{B.WHITE} - YOUR PASSWORD : {B.RED}')
Target = input(f'{B.YELLOW}[{B.WHITE}+{B.YELLOW}]{B.WHITE} - TARGET USERNAME : {B.RED}')
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
    id=input(f'{B.YELLOW}[{B.WHITE}+{B.YELLOW}]{B.WHITE} - TARGET ID : {B.RED}')
    print(f"""
{B.YELLOW}[{B.WHITE}1{B.YELLOW}]{B.WHITE} -{B.YELLOW} spam
{B.YELLOW}[{B.WHITE}2{B.YELLOW}]{B.WHITE} -{B.YELLOW} violence
{B.YELLOW}[{B.WHITE}3{B.YELLOW}]{B.WHITE} -{B.YELLOW} Impersonation
{B.YELLOW}[{B.WHITE}4{B.YELLOW}]{B.WHITE} -{B.YELLOW} Sexual activity
{B.YELLOW}[{B.WHITE}5{B.YELLOW}]{B.WHITE} -{B.YELLOW} harassment
{B.YELLOW}[{B.WHITE}6{B.YELLOW}]{B.WHITE} -{B.YELLOW} Self-harm
{B.YELLOW}[{B.WHITE}7{B.YELLOW}]{B.WHITE} -{B.YELLOW} Hate on
    """)
    xx = int(input(f"{B.YELLOW}[{B.WHITE}+{B.YELLOW}]{B.WHITE} - Choose : {B.RED}"))
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
    P1= int(input(f'{B.YELLOW}[{B.WHITE}+{B.YELLOW}]{B.WHITE} - HOW MANY REPORT : {B.RED}'))
    tu = int(input(f'{B.YELLOW}[{B.WHITE}+{B.YELLOW}]{B.WHITE} - SECONDS : {B.RED}'))
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
     print(f"\r{B.GREEN}Done={nu} |{B.RED} Error={n}",end="")
      
else :
  print('bad login X ')
