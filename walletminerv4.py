#setup
import time
import random
import colorama 
import ctypes
import os
import sys
from colorama import Fore, Back, Style
from collections import namedtuple
colorama.init(autoreset=True)
#functions
ctypes.windll.kernel32.SetConsoleTitleW("wallet miner")
#-----------------------------------------
def g(rolls):
	return "".join(random.choice("qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM") for i in range(0, rolls+1))

#-----------------------------------------
k = input("""██╗    ██╗ █████╗ ██╗     ██╗     ███████╗████████╗    ███╗   ███╗██╗███╗   ██╗███████╗██████╗     ██╗   ██╗██████╗ 
██║    ██║██╔══██╗██║     ██║     ██╔════╝╚══██╔══╝    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗    ██║   ██║╚════██╗
██║ █╗ ██║███████║██║     ██║     █████╗     ██║       ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝    ██║   ██║ █████╔╝
██║███╗██║██╔══██║██║     ██║     ██╔══╝     ██║       ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝ 
╚███╔███╔╝██║  ██║███████╗███████╗███████╗   ██║       ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║     ╚████╔╝ ███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝

========================================================

MADE BY WIL#2184 ON DISCORD
What is your product key?\n>""").lower()              # Checking product key

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
n = input("enter the 1st color you want to use here:").lower()  #asking for first color

colorcodes = namedtuple('colorcodes', ['blue', 'yellow', 'white', 'red', 'purple', 'cyan', 'green'])
colors = colorcodes(colorama.Fore.BLUE, colorama.Fore.YELLOW, colorama.Fore.WHITE,
          colorama.Fore.RED, colorama.Fore.MAGENTA, colorama.Fore.CYAN, colorama.Fore.GREEN)
#-----------------------------------------
try:
	col_ur = getattr(colors, n)
except AttributeError:					# selecting scond color	
    print("Input not valid, defaulting to white.")
    col_u2 = colors.white
#-----------------------------------------

b = input("enter the 2nd color you want to use here:").lower()   #asking for second color

#-----------------------------------------
try:
    col_ur2 = getattr(colors, b)
except AttributeError:					# selecting second color
    print("Input not valid, defaulting to white.")
    col_ur2 = colors.white
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

t = input("'btc'/'eth'/'both'\n>").lower()

match t:
	case "btc":
		coin_co = "Bitcoin"
		short_co = "0.0000 BTC"
		false_co = "BTC"
	case "eth":
		coin_co =  "Ethereum"
		short_co = "0.0000 ETH"                # Selecting the type of wallet to mine
		false_co = "ETH"
	case "both":
		coin_co = "Both"
		short_co = "0.0000 balance"
		false_co = "BTC"
	case _:
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
print("\nValid adress found, privite key is below.")
print(col_ur  + coin_co + col_ur2 +" |0xKyx4csZSgXAEssUCtvS8fx1i7jSKD7Aw41cuVhXyTF89r8Ff3K5u| " + col_ur + "0.0000 " + false_co  + "  (VALID)")
print("The public address is;" + col_ur + " " + (random.choice(dawg)))
while True: pass
