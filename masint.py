#Funcionamiento
import os,argparse,subprocess
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
		command0 = "nslookup "+ domain +" | awk '/^Name:/ {c=2;N=$2} !--c {print N,$2}'|column -s ' ' -t -N DOMINIO:,IP: -o '||'"
		p0 = subprocess.Popen(command0, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		a, b = p0.communicate()
		a.split(b"\n")
		print(a.decode("utf-8"))
		print("------------------------------------------WHOIS-------------------------------------------")
		command1 = "whois -H "+ domain +" | egrep -v "+"'PRIVACY|above|Please|Whois|update|unsigned|:$'| sed 's/: /;/g' | column -s ';' -t -N PARAMETRO:,RESULTADO: -o '||'"
		p1 = subprocess.Popen(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		c, d = p1.communicate()
		c = c.split(b"\n")
		for x in c:
			if x!=b'':
				print(x.decode("utf-8"))					
		print("----------------------------------------SUBLIST3R-----------------------------------------")
		print(os.system('python3 $(find ~ -name sublist3r.py) -d ' +domain))
		print("----------------------------------------FAVIHASH------------------------------------------")
		print(os.system('python3 $(find ~ -name favihash.py) -u https://www.' +domain))
		print("----------------------------------------AQUATONE------------------------------------------")
		print(os.system('aquatone-discover --domain ' +domain))
try:
	masint()
except:
	print(x)
	#print("ERROR: Dominio no disponible,\nFavor ingresar la opcion -d [dominio] e intente nuevamente")
