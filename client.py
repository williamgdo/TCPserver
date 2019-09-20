import socket
import sys

# cria o socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# recebe o arquivo pelo nome passado na linha de comando
try:
    file_name = sys.argv[1]
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()
except Exception:
    print('Erro: ' + Exception.__name__)


host = '127.0.0.1'    	# configura o ip hospedeiro para a conexao
port = 2019             # porta de comunicacao (a mesma que a do servidor)
print('Se conectando a ' + host + ', porta ' + str(port))

sock.connect((host, port)) # conecta o socket na porta em que o server esta escutando

try:
    print('Enviando arquivo "' + file_name + '"...')
    sock.sendall(bytes(file_data))

    # Look for the response
    # amount_received = 0
    # amount_expected = len(message)
    
    # while amount_received < amount_expected:
    #     data = sock.recv(16)
    #     amount_received += len(data)
    #     print('received "' + str(data) + '"')

finally:
    sock.close()
    print('Socket fechado.')
