#setup
import time
import random
import colorama 
import ctypes
import os
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
#functions
ctypes.windll.kernel32.SetConsoleTitleW("wallet miner")

def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result

#interface
print("██╗    ██╗ █████╗ ██╗     ██╗     ███████╗████████╗    ███╗   ███╗██╗███╗   ██╗███████╗██████╗     ██╗   ██╗██████╗ ")
print("██║    ██║██╔══██╗██║     ██║     ██╔════╝╚══██╔══╝    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗    ██║   ██║╚════██╗")
print("██║ █╗ ██║███████║██║     ██║     █████╗     ██║       ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝    ██║   ██║ █████╔╝")
print("██║███╗██║██╔══██║██║     ██║     ██╔══╝     ██║       ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝ ")
print("╚███╔███╔╝██║  ██║███████╗███████╗███████╗   ██║       ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║     ╚████╔╝ ███████╗")
print(" ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝")                                                                                                                                                                                                                                                                                                                             
print("")       
print("color list: 'white', 'blue', 'red', 'green', 'cyan', 'purple', 'yellow' ")
print("")
print("         1st    2nd      1st")
print("format: 'type' |0x64| 'balence' ")
print("")
nn = input("enter the 1st color you want to use here:")
bb = input("enter the 2nd color you want to use here:")

n = nn.lower()
b = bb.lower()

if n == "blue":
	col_ur = colorama.Fore.BLUE
if n == "yellow":
	col_ur = colorama.Fore.YELLOW
if n == "white":
	col_ur = colorama.Fore.white
if n == "red":
	col_ur = colorama.Fore.RED
if n == "purple":
	col_ur = colorama.Fore.MAGENTA
if n == "cyan":
	col_ur = colorama.Fore.CYAN
if n == "green":
	col_ur = colorama.Fore.GREEN
#-----------------------------------------
if b == "blue":
	col_ur2 = colorama.Fore.BLUE
if b == "yellow":
	col_ur2 = colorama.Fore.YELLOW
if b == "white":
	col_ur2 = colorama.Fore.white
if b == "red":
	col_ur2 = colorama.Fore.RED
if b == "purple":
	col_ur2 = colorama.Fore.MAGENTA
if b == "cyan":
	col_ur2 = colorama.Fore.CYAN
if b == "green":
	col_ur2 = colorama.Fore.GREEN
	#-------------------------------------
print("")
print("===================================")
print("")
print("Bitcoin/Ethereum wallet miner")
print("What wallet type you want to check?")

tt = input("'btc'/'eth'/'both'\n>")

t = tt.lower()
if t == "btc":
	coin_co = "Bitcoin"
	short_co = "0.0000 BTC"
if t == "eth":
	coin_co =  "Ethereum"
	short_co = "0.0000 ETH"
if t == "both":
	coin_co = "Both"
	short_co = "0.0000 balance"
print("")
print("========================================================")
print("")
print("What is your wallet private key? (to send funds to)")
print("If you only want the wallet key, leave this feild empty.")
key = input(">")

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
while True:
	print(col_ur  + coin_co + col_ur2 +" |0x"+g(64) + "| " + col_ur + short_co)
