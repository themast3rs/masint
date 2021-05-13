#Funcionamiento
import os,argparse
Banner="""
 █████║ ██████║██████║██████║███   ██║██████║
██╔█═██║██╔═██║███║     ██║  ████  ██║  ██║  
██║█ ██║██████║██████║  ██║  ██╔██ ██║  ██║  
██║  ██║██╔═██║  ║███║  ██║  ██║ ████║  ██║  
██║  ██║██║ ██║██████║██████║██║  ███║  ██║   
╚═╝  ╚═╝╚═╝ ╚═╝╚═════╝╚═════╝╚═╝   ╚═╝  ╚═╝
--------------------->> MASTER INVESTIGATION
--------------------->> By TheMast3rs
"""
#Parametro -d domain
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", help="Dominio sin 'www'")
args = parser.parse_args()
domain = args.domain
def masint():
	print(Banner)
	if domain==None:
		print("ERROR: Dominio no disponible,\nFavor ingresar la opcion -d [dominio] e intente nuevamente")
	else:	
		print("----------------------------------------NSLOOKUP------------------------------------------")
		print(os.system('nslookup ' +domain))
		print("------------------------------------------WHOIS-------------------------------------------")
		print(os.system('whois ' +domain))
		print("----------------------------------------SUBLIST3R-----------------------------------------")
		print(os.system('python3 $(find ~ -name sublist3r.py) -d ' +domain))
		print("----------------------------------------FAVIHASH------------------------------------------")
		print(os.system('python3 $(find ~ -name favihash.py) -u https://www.' +domain))
		print("----------------------------------------AQUATONE------------------------------------------")
		print(os.system('aquatone-discover --domain ' +domain))
try:
	masint()
except:
	print("ERROR: DOMINIO no disponible, por favor intente nuevamente")
