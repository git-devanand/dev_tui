import numpy
import os
import getpass  		#To take inputs from user invisiblly not in echo back .
import time
os.system("tput setab 17")
os.system('tput setaf 1')
print('\t\t\t***** Hey to my TUI that makes life simple *****')
os.system('tput setaf 7')
print("\n\n")

os.system("tput setaf 5")
print('\t\t.......................................................\n')
print('\t\t\t***********************************\n')
print('\t\t.......................................................\n')

os.system("tput setaf 9")
print('\n\n')

os.system("tput setaf 3")
print("""\t\t|^^^^^)  !----  \      /     ^^^^!^^^^   !     !    -!- 
                |     |  |____   \    /          !       !     !     !
                |     |  !        \  /           !       !     !     !
                |     )  !____     \/   ________ !       !*****!    -!-
                 ^^^^^            
""")

os.system("tput setaf 9")

# To give Authentication to this TUI project.
passwd = getpass.getpass("Enter Password : ")
apass = 'tui369'
if passwd != apass :
	os.system("tput setaf 1")
	print("Authentication is Incorrect !!!")
	exit()
	
print("\n\n")


print("Where you want to perform your job (local/remote) : " , end='')
location=input()
print("location")


if location == "remote" :
    remoteIP = input("Enter user IP : ")
    os.system("ping {0}".format(remoteIP))

while True:    

	os.system("tput setaf 6")

	
	print("""
	Press 1 : To see Date
	Press 2 : To check Cal
	Press 3 : To conf web server
	Press 4 : To create user
	Press 5 : To create file
	Press 6 : To reboot or shutdown pc
	Press 7 : To update or upgrade
	Press 8 : To install a software
	Press 9 : To run a program
	Press 10: To read manual
	Press 11: To run a CLI program/code on different CLI i.e. tty
	Press 12: To chane authentication password
	Press 13: To Exit
	""")    


	print("Enter your choice : " , end="")
	ch=input()
	print(ch)

	os.system("tput setaf 10")


	if location == "local" :
		if int(ch) == 1 :
			os.system("date")				
		elif int(ch) == 2 :
			os.system('cal')
		elif int(ch) == 3 :
			os.system('sudo apt install httpd')
		elif int(ch) == 4 :
			print('Can you plz username : ' , end='')
			create_user = input()
			os.system('sudo useradd {0}'.foramt(create_user))
		elif int(ch) == 5 :
			print('Create new file you want : ' , end='')
			create_file=input()
			os.system('touch {} '.format(create_file))
		elif int(ch) == 6 :
			rbt_sdn=input("Enter 'reboot' for rebooting or for 'shutdown' for shutdown your pc :  ")
			os.system('{} '.format(rbt_sdn))
		elif int(ch) == 7 :
			print("Enter 'update' for updating or 'upgrade' for upgrading " , end='')
			ud_ug=input()
			os.system('sudo apt {} '.format(ud_ug))
		elif int(ch) == 8 :
			print("Which software you want to install :" , end='')
			install = input()
			os.system('sudo apt install {0}'.format(install))
		elif int(ch) == 9 :
			os.system('tput setab 90')
			os.system('tput setaf 108')
			print("Which program you want to run : " , end='')
			program = input()
			os.system("{0}".format(program))
				
				
		elif int(ch) ==10 :
			manual=input("Enter the manual you want to read :  ")
			os.system("man {} ".format(manual))
			
		elif int(ch) ==11 :
			os.system("tput setaf 3")
			print("Your curent tty location !!!")
			os.system("tty")
			tty_n=input("Enter virtual terminal number 0-7 : ")	
			os.system("chvt {}".format(tty_n))
			pgm=input("Enter a program you want to run :  ")
			cli=input("Give destination on which you want to run program :  ")
			os.system("{0} > {1} ".format(pgm , cli))
				
		#To change authentication password.
		elif int(ch) ==12 :
			new_passwd = getpass.getpass("{}".format(apass))
			check_passwd = getpass.getpass("Check new password : ")
			if check_passwd != new_passwd :
				os.system("tput setaf 1")
				print("!!! Check password is not matching !!!")	
				check_passwd = getpass.getpass("Enter matched password with new password : ")
				if check_passwd == new_passwd :
					os.system('tput setaf 5')
					print("!!! Your Authentication Password has been successfully changed !!!")
			else:	
				os.system("tput setaf 5")
				print("!!! Your Authentication Password has been successfully changed !!!")
		elif int(ch) ==13 :
			exit()
		else:
			os.system('tput setaf 1')
			print('Option Not Supported ! Please choose a valid option.')
			
	
"""	
	elif location == "remote" :
		if int(ch) == 1 :
			os.system("ssh {0} date".format(remoteIP))
		elif int(ch) == 2 :
			os.system("ssh {0} cal".format(remoteIP))
		elif int(ch) == 3 :
			os.system("ssh {0} sudo apt install httpd".format(remoteIP))
		elif int(ch) == 4 :
			print("Can you plz username : ")
			create_user = input()
			os.system("ssh {0} sudo useradd {1}".format(remoteIP , create_user))
		else:
		    	print("Option Not Supported")
"""
