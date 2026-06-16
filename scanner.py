import socket
import sys
import argparse
from datetime import datetime

# ==========================================
# 1. GESTION DES ARGUMENTS CLI (argparse)
# ==========================================
parser = argparse.ArgumentParser(
    description="Scanner de ports TCP simple en ligne de commande.",
    add_help=False
)

parser.add_argument("-t", "--target", help="Adresse IP ou nom d'hôte de la cible")

if len(sys.argv) == 1:
    print("Erreur : Veuillez spécifier une adresse IP cible avec l'option -t.")
    sys.exit(1)

args = parser.parse_args()

if not args.target:
    print("Erreur : Veuillez spécifier une adresse IP cible avec l'option -t.")
    sys.exit(1)

cible = args.target

# ==========================================
# 2. CONFIGURATION DE LA CIBLE
# ==========================================
try:
    ip_cible = socket.gethostbyname(cible)
except socket.gaierror:
    print(f"\n[-] Erreur : Impossible de résoudre le nom d'hôte ou l'IP '{cible}'.")
    sys.exit(1)

print("-" * 50)
print(f"[*] Scan de la cible : {ip_cible}")
print(f"[*] Heure de début : {datetime.now()}")
print("-" * 50)

# ==========================================
# 3. BOUCLE DE SCAN (TCP Connect Scan)
# ==========================================
try:
    for port in range(20, 10001):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2) 
        
        resultat = sock.connect_ex((ip_cible, port))
        
        if resultat == 0:
            print(f"[+] Le port {port} est OUVERT")
            
        sock.close()

except KeyboardInterrupt:
    print("\n[-] Scan interrompu par l'utilisateur (Ctrl+C).")
    sys.exit()
except socket.error:
    print("\n[-] Impossible de se connecter au serveur.")
    sys.exit()

print("-" * 50)
print("[*] Scan terminé.")
