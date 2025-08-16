import os
import platform
import psutil
import socket

print(f"Sistema Operacinal: {platform.system()} {platform.release()}.")
print(f"Nome do Usuário: {os.environ.get("USERNAME")}.")
print(f"IPv4: {socket.gethostbyname(socket.gethostname())}.")

#Coleta Informações Sobre as Portas TCP e UDP.
print(f"Portas Abertas:/n")
connetall = psutil.net_connections(kind="inet")
only_udp = [conn for conn in psutil.net_connections(kind="inet") if conn.type == socket.SOCK_DGRAM]

# Separar as Informações Sobre as Portas
only_tcp_listenig_ports = [conn.laddr.port for conn in connetall if conn.status == psutil.CONN_LISTEN] # TCP
only_udp_listenig_ports = [conn.laddr.port for conn in only_udp] # UDP

# Remover as Portas da Lista
only_tcp_listenig_ports = list(set(only_tcp_listenig_ports))
only_udp_listenig_ports = list(set(only_udp_listenig_ports))

# Organizar as Portas
only_tcp_listenig_ports.sort()
only_udp_listenig_ports

# Mostrar as Portas TCP
print("Portas TCP:\n")
for port in only_tcp_listenig_ports:
    print(f"Porta TCP: {port} Aberta")

#Mostra as Portas UDP
print("Portas UDP:\n")
for port in only_udp_listenig_ports:
    print(f"Porta UDP: {port} Aberta")