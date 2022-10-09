#setup
import time
import random
import colorama 
import ctypes
import os
import sys
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
#functions
ctypes.windll.kernel32.SetConsoleTitleW("wallet miner")
#-----------------------------------------
def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00001)
#-----------------------------------------
kk = input("""██╗    ██╗ █████╗ ██╗     ██╗     ███████╗████████╗    ███╗   ███╗██╗███╗   ██╗███████╗██████╗     ██╗   ██╗██████╗ 
██║    ██║██╔══██╗██║     ██║     ██╔════╝╚══██╔══╝    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗    ██║   ██║╚════██╗
██║ █╗ ██║███████║██║     ██║     █████╗     ██║       ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝    ██║   ██║ █████╔╝
██║███╗██║██╔══██║██║     ██║     ██╔══╝     ██║       ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝ 
╚███╔███╔╝██║  ██║███████╗███████╗███████╗   ██║       ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║     ╚████╔╝ ███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝

========================================================

MADE BY WIL#2184 ON DISCORD
What is your product key?\n>""")              # Checking product key
k = kk.lower()

if k == "dev":
	os.system('cls')
	pass
else:
	ii = 1
	print(colorama.Fore.RED + "Product key not valid, console now closing.")
	time.sleep(5)
	exit()
#-----------------------------------------
ban = """██╗    ██╗ █████╗ ██╗     ██╗     ███████╗████████╗    ███╗   ███╗██╗███╗   ██╗███████╗██████╗     ██╗   ██╗██████╗ 
██║    ██║██╔══██╗██║     ██║     ██╔════╝╚══██╔══╝    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗    ██║   ██║╚════██╗
██║ █╗ ██║███████║██║     ██║     █████╗     ██║       ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝    ██║   ██║ █████╔╝
██║███╗██║██╔══██║██║     ██║     ██╔══╝     ██║       ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝ 
╚███╔███╔╝██║  ██║███████╗███████╗███████╗   ██║       ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║     ╚████╔╝ ███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝
color list: 'white', 'blue', 'red', 'green', 'cyan', 'purple', 'yellow'

         1st    2nd      1st
format: 'type' |0x64| 'balance'
"""
print(ban)
#-----------------------------------------
nn = input("enter the 1st color you want to use here:")  #asking for first color
n = nn.lower()
if n == "blue":
	col_ur = colorama.Fore.BLUE
elif n == "yellow":
	col_ur = colorama.Fore.YELLOW
elif n == "white":
	col_ur = colorama.Fore.WHITE
elif n == "red":
	col_ur = colorama.Fore.RED       #seclecting first color
elif n == "purple":
	col_ur = colorama.Fore.MAGENTA
elif n == "cyan":
	col_ur = colorama.Fore.CYAN
elif n == "green":
	col_ur = colorama.Fore.GREEN
else:
	print("Input not valid, defaulting to white.")
	col_ur = colorama.Fore.WHITE

bb = input("enter the 2nd color you want to use here:")   #asking for second color
b = bb.lower()
#-----------------------------------------
if b == "blue":
	col_ur2 = colorama.Fore.BLUE
elif b == "yellow":
	col_ur2 = colorama.Fore.YELLOW
elif b == "white":
	col_ur2 = colorama.Fore.WHITE
elif b == "red":
	col_ur2 = colorama.Fore.RED        #selecting second color
elif b == "purple":
	col_ur2 = colorama.Fore.MAGENTA
elif b == "cyan":
	col_ur2 = colorama.Fore.CYAN
elif b == "green":
	col_ur2 = colorama.Fore.GREEN
else:
	print("Input not valid, defaulting to white.")
	col_ur2 = colorama.Fore.WHITE
#-------------------------------------
os.system('cls')
ban1 = """██╗    ██╗ █████╗ ██╗     ██╗     ███████╗████████╗    ███╗   ███╗██╗███╗   ██╗███████╗██████╗     ██╗   ██╗██████╗ 
██║    ██║██╔══██╗██║     ██║     ██╔════╝╚══██╔══╝    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗    ██║   ██║╚════██╗
██║ █╗ ██║███████║██║     ██║     █████╗     ██║       ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝    ██║   ██║ █████╔╝
██║███╗██║██╔══██║██║     ██║     ██╔══╝     ██║       ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝ 
╚███╔███╔╝██║  ██║███████╗███████╗███████╗   ██║       ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║     ╚████╔╝ ███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝

========================================================

Bitcoin/Ethereum wallet miner
What wallet type you want to check?"""
print(ban1)

tt = input("'btc'/'eth'/'both'\n>")

t = tt.lower()
if t == "btc":
	coin_co = "Bitcoin"
	short_co = "0.0000 BTC"
	false_co = "BTC"
elif t == "eth":
	coin_co =  "Ethereum"
	short_co = "0.0000 ETH"                # Selecting the type of wallet to mine
	false_co = "ETH"
elif t == "both":
	coin_co = "Both"
	short_co = "0.0000 balance"
	false_co = "BTC"
else:
	print("Input not valid, defaulting to BTC.")
	coin_co = "Bitcoin"
	short_co = "0.0000 BTC"	
	false_co = "BTC"
#-----------------------------------------
ban2 = """
========================================================

What is your wallet pubic key? (to send funds to)
If you only want the wallet key, leave this feild empty."""
print(ban2)
key = input(">")
print("\nWallet not valid, proceeding in key only mode.")
time.sleep(3)
os.system('cls')
print(col_ur  + " █     █░ ▄▄▄       ██▓     ██▓    ▓█████▄▄▄█████▓" + col_ur2 + "  ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  ")
print(col_ur  + "▓█░ █ ░█░▒████▄    ▓██▒    ▓██▒    ▓█   ▀▓  ██▒ ▓▒" + col_ur2 + " ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒")
print(col_ur  + "▒█░ █ ░█ ▒██  ▀█▄  ▒██░    ▒██░    ▒███  ▒ ▓██░ ▒░" + col_ur2 + " ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒")
print(col_ur  + "░█░ █ ░█ ░██▄▄▄▄██ ▒██░    ▒██░    ▒▓█  ▄░ ▓██▓ ░ " + col_ur2 + " ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ")
print(col_ur  + "░░██▒██▓  ▓█   ▓██▒░██████▒░██████▒░▒████▒ ▒██▒ ░ " + col_ur2 + " ▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒")
print(col_ur  + "░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░ ▒ ░░   " + col_ur2 + " ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░")
print(col_ur  + "  ▒ ░ ░    ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░   ░    " + col_ur2 + " ░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░")
print(col_ur  + "  ░   ░    ░   ▒     ░ ░     ░ ░      ░    ░      " + col_ur2 + " ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ ")
print(col_ur  + "    ░          ░  ░    ░  ░    ░  ░   ░  ░        " + col_ur2 + "         ░    ░           ░    ░  ░   ░    ")
time.sleep(1.25)
for en in range(1, (random.randint(2000000, 20000000))):
	print(col_ur  + coin_co + col_ur2 +" |0x"+g(52) + "| " + col_ur + short_co + "  (INVALID)")
	time.sleep(0.01)
#-----------------------------------------
dawg = ['13vha36jMwcxzLvogef1QKdyHUsnwSrSyi', '1KYGfzr2RrvbT3wjtnWhksUcrPtatZgki6', '16r1hJDrXgHcZWymwFpaLrriqRzxqUA8Vm', '1MFxWN1fvMicg8XFZaEr5EkEs4qWZb59bp', '1BRf6HNxL5riFCuCeYJ3wuSyjjWeLynHQQ']
derg = ['L3TFkGWsVnherhkq6Qy9j3kr1TjCZzbn1u4sWa3Jag9dBDTsCnCh', 'KxnYWCXyqaArve6hiQ4e3igN6RUbWsSEA1MmWMXip21JCVYoCjt4', 'L5GTYtR2zWvtA6T8jNe9XtnXNHcYMDBGeXMAaPUQ84dnNYRAxLFW']
print("\nValid adress found, privite key is below.")
print(col_ur  + coin_co + col_ur2 +" |0xKyx4csZSgXAEssUCtvS8fx1i7jSKD7Aw41cuVhXyTF89r8Ff3K5u| " + col_ur + "0.0000 " + false_co  + "  (VALID)")
print("The public address is;" + col_ur + " " + (random.choice(dawg)))
while True: pass
