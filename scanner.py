import socket
import sys
from datetime import datetime

# ==========================================
# 1. CONFIGURATION DE LA CIBLE
# ==========================================
cible = "127.0.0.1"
ip_cible = socket.gethostbyname(cible)

print("-" * 50)
print(f"[*] Scan de la cible : {ip_cible}")
print(f"[*] Heure de début : {datetime.now()}")
print("-" * 50)

# ==========================================
# 2. BOUCLE DE SCAN (TCP Connect Scan)
# ==========================================
try:
    # On scanne jusqu'au port 10000 pour intercepter ton serveur du TP précédent
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
