import os
def ty():
	if os.name == 'nt':
		_ = os.system ('cls')
	else:
		_ = os.system ('clear')
b='\033[36m'
j='\033[33m'
z='\033[32m'
k='\033[31m'
s='\033[34m'
f='\033[35m'
n='\033[37m'
def kek():
	print('Выполнено.......Termux Cod\nАвторы..........',k,'W',b,'o',f,'l',z,'F',j,'a',s,'k','...',k,'T',b,'o',j,'p',b,'o',s,'1',z,'u',f,'s',n,'\nСообщество вк...https://m.vk.com/termux_cod\n')
	lol= input('Ваш ник: ')
	print('\n\033[37m[1] Белый\n\033[36m[2] Бирюзовый\n\033[33m[3] Желтый\n\033[32m[4] Зеленый\n\033[31m[5] Красный\n\033[34m[6] Синий\n\033[35m[7] Фиолетовый\n\033[30m[8] Черный',n,'(Черный)\n')
	
	color=input('Выберите цвет: ')

	if color=='1':
            to='37m' 
	if color=='2':
	    to='36m' 
	if color=='3':
	    to='33m' 
	if color=='4':
	    to='32m' 
	if color=='5':
	    to='31m' 
	if color=='6':
	    to='34m' 
	if color=='7':
	    to='35m' 
	if color=='8':
	    to='30m' 

	with open ('/data/data/com.termux/files/usr/etc/bash.bashrc', 'w+') as file:
		try:
			file = file.write (r"PS1='\[\e[{0}\]{1}~ \[\e[0m\]'".format (to,lol))
			print ('\033[32mNick изменен :)')
		except:
			print ('\033[31mЛол, что-то не так, обратись в тех.поддержку группы')
ty()
kek()
