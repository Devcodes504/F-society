from colorama import Fore, Back, Style, init
import nmap
import os
import time
import requests
import secrets
import string
os.system("clear")
time.sleep(1.0)
print(f"{Style.BRIGHT}{Fore.GREEN} F-SOCIETY{Style.RESET_ALL}")
time.sleep(1.0)
print(f" {Style.BRIGHT}{Fore.GREEN}@CREATED BY NEXUS {Style.RESET_ALL}\n")
#info
print(f"{Style.BRIGHT}{Fore.MAGENTA}[*] Funciones:{Style.RESET_ALL}")
time.sleep(1.5)
print(f"{Style.BRIGHT}{Fore.GREEN}[1] Escanea red wifi{Style.RESET_ALL}")
time.sleep(1.0)
print(f"{Style.BRIGHT}{Fore.GREEN}[2] obtener informacion de un numero{Style.RESET_ALL}")
time.sleep(1.0)
print(f"{Style.BRIGHT}{Fore.GREEN}[3] Busca un usuario en varias redes sociales{Style.RESET_ALL}")
time.sleep(1.0)
print(f"{Style.BRIGHT}{Fore.GREEN}[4] Genera contraseñas seguras{Style.RESET_ALL}")

time.sleep(2.8)
os.system("clear")
banner = fr""" {Style.BRIGHT}{Fore.MAGENTA}
  ___       ___  ___  ___  _  ___  ___  _ _ 
 | __> ___ / __>| . ||  _>| || __>|_ _|| | |
 | _> |___|\__ \| | || <__| || _>  | | \   /
 |_|       <___/`___'`___/|_||___> |_|  |_| 
                                           {Style.RESET_ALL} """
#escanear red
def escanear_red():
    escaner = nmap.PortScanner()
    red = input(f"\n{Style.BRIGHT}{Fore.CYAN}[+] {Style.RESET_ALL}{Style.BRIGHT}{Fore.MAGENTA}Ingrese la ip: {Style.RESET_ALL}")
    time.sleep(1.0)
    print(f"{Style.BRIGHT}{Fore.GREEN}Escaneando  red... {Style.RESET_ALL}")
    try:
        escaner.scan(hosts=red,arguments='-sn')
        for host in escaner.all_hosts():
            print(f"\n{Style.BRIGHT}{Fore.CYAN}[+] IP: {host}{Style.RESET_ALL}") 
            print(f"{Style.BRIGHT}{Fore.CYAN}[+] Estado: {escaner[host].state()}{Style.RESET_ALL}") 
            if escaner[host].hostname(): 
            print(f"{Style.BRIGHT}{Fore.CYAN}[+] Nombre: {escaner[host].hostname()}{Style.RESET_ALL}")
            print("-" * 30)
    except:
      	 print(f"{Style.BRIGHT}{Fore.RED}¡ocurrio un error!{Style.RESET_ALL}")
#num info
def num_info():
    api = "2f6ba60a20ffe47f3d04f8ac4f465d9b"
    url = "http://apilayer.net/api/validate"
    params = {
    "access_key": api,
    "number": numero
}
    respuesta = requests.get(url, params=params)
    data = respuesta.json()
    if data.get("valid"):
             time.sleep(1.0)
             print(f"{Fore.MAGENTA}------------ Info -------------------------------------{Style.RESET_ALL}")
             print(f"{Fore.GREEN}\nvalido:{Style.RESET_ALL} {Fore.CYAN}si{Style.RESET_ALL}")
             print(f"{Fore.GREEN}numero:{Style.RESET_ALL} {Fore.CYAN}{data['international_format']}{Style.RESET_ALL}")
             
             print(f"{Fore.GREEN}pais:{Style.RESET_ALL} {Fore.CYAN}{data['country_name']}{Style.RESET_ALL}")
             
             print(f"{Style.BRIGHT}{Fore.GREEN}operador:{Style.RESET_ALL} {Fore.CYAN}{data['carrier']}{Style.RESET_ALL}")
             print(f"\n{Fore.MAGENTA}-------------------------------------------------------{Style.RESET_ALL}")
    else:
      print("Error:", data.get("Error"))

#buscar usuarios
def osint_name(usuario,usuario_url, usuario_guion):
    sitios = {
    "Github": f"https://github.com/{usuario_url}",
    "Facebook": f"https://facebook.com/{usuario_url}",
    "Tik Tok": f"https://tiktok.com/@{usuario_url}",
    "Instagram": f"https://instagram.com/{usuario_url}",
    "Twitter/X": f"https://x.com/{usuario_url}",
    "YouTube": f"https://youtube.com/@{usuario_url}",
    "Reddit": f"https://reddit.com/user/{usuario_guion}",
    "Pinterest": f"https://pinterest.com/{usuario_url}",
    "Twitch": f"https://twitch.tv/{usuario_url}",
    "Telegram": f"https://t.me/{usuario_url}"
}
    
    print(f"{Style.BRIGHT}{Fore.GREEN}Buscando usuario:{Style.RESET_ALL} {Fore.GREEN}{usuario}{Style.RESET_ALL}\n")
    
    for nombre, url in sitios.items():
        try:
            rps = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
            if rps.status_code == 200:
                print(f"{Style.BRIGHT}{Fore.GREEN}[✓] Usuario encontrado en {nombre}: {Style.RESET_ALL} {Fore.CYAN}{url}{Style.RESET_ALL} ")
            else:
             print(f"{Style.BRIGHT}{Fore.RED}[!] usuario no encontrado: {nombre}{Style.RESET_ALL}")
        except:
               print(f"{Style.BRIGHT}[!]no encontrado{nombre}")

#generador de contraseñas
def contraseñas():
    print(f"\n{Style.BRIGHT}{Fore.GREEN}[+] Generador de Contraseñas Seguras{Style.RESET_ALL}")
    try:
        longitud = int(input(f"{Style.BRIGHT}{Fore.MAGENTA}[+] Cuantos caracteres? 8-32: {Style.RESET_ALL}"))
        if longitud < 8: longitud = 8
        if longitud > 32: longitud =32
    except:
        longitud = 12

    # Caracteres: letras may, minus, numeros y simbolos seguros
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    
    
    contra = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*")
    ]
    
    
    for _ in range(longitud - 4):
        contra.append(secrets.choice(caracteres))
    
   
    secrets.SystemRandom().shuffle(contra)
    
    contra_final = ''.join(contra)
    
    print(f"\n{Style.BRIGHT}{Fore.GREEN}[✓] Tu contraseña segura:{Style.RESET_ALL} {Fore.CYAN}{contra_final}{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.MAGENTA}[!] ¡Contraseña generada!{Style.RESET_ALL}\n")
    
    
    
    
while True:
	print(banner)
	print(f"{Fore.CYAN}[1] {Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}Escanear wifi{Style.RESET_ALL}")
	
	print(f"{Fore.CYAN}[2]{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN} Numero info{Style.RESET_ALL}")
	
	print(f"{Fore.CYAN}[3]{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN} Buscar usuarios OSINT{Style.RESET_ALL}")
	
	print(f"{Fore.CYAN}[4]{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN} Generar contraseñas {Style.RESET_ALL}")
	
	print(f"{Fore.CYAN}[5]{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN} Salir{Style.RESET_ALL}")
	try:
		opcion = int(input(f"\n{Fore.CYAN}[+]{Style.RESET_ALL}{Style.BRIGHT}{Fore.MAGENTA} Ingrese una opcion: {Style.RESET_ALL}"))
		
	except:
		print(f"{Style.BRIGHT}{Fore.RED}¡Ingrese una opcion valida!{Style.RESET_ALL}")
		
	if opcion == 1:
			print(f"\n{Style.BRIGHT}{Fore.GREEN}[*] ESCANEAR RED{Style.RESET_ALL}")
			time.sleep(1.0)
			escanear_red()
			
	elif opcion == 2:
		print(f"\n{Style.BRIGHT}{Fore.GREEN}[*] Numero Info {Style.RESET_ALL}")
		numero = input(f"\n{Style.BRIGHT}{Fore.CYAN}[+] {Fore.MAGENTA}Ingrese el numero sin espacios: {Style.RESET_ALL}")
		num_info()
		
	elif opcion == 3:
	      print(f"\n{Style.BRIGHT}{Fore.GREEN}[*] Buscar Usuarios{Style.RESET_ALL}")
	      usuario =  input(f"\n{Style.BRIGHT}{Fore.MAGENTA}[+]{Style.RESET_ALL} {Style.BRIGHT}{Fore.YELLOW}Ingrese el nombre: {Style.RESET_ALL}")
	      usuario_url = usuario.replace(" ", "")
	      usuario_guion = usuario.replace(" ", "_")
	      osint_name(usuario, usuario_url, usuario_guion)
	      osint_name(usuario, usuario_guion, usuario_url)
	
	elif opcion == 4:
		contraseñas()
		
	elif opcion== 5:
			time.sleep(1.0)
			print(f"\n{Style.BRIGHT}{Fore.GREEN}Saliendo...{Style.RESET_ALL}")
			time.sleep(1.3)
			exit()
	 
