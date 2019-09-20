import socket
import sys

# Cria o socket TCP/IP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'       # hostname para ser vinculado
port = 2019              # porta a ser usada

print('Server iniciado no ip ' + host + ', porta ' + str(port))
sock.bind((host, port))

# se prepara para conexoes
sock.listen(1)

while True:
    # espera uma conexao
    print('Esperando uma conexao...')
    connection, client_address = sock.accept()

    try:
        print('Conexao de ' + str(client_address))

        # recebe os dados e salva na pasta do servidor
        file_data = bytes(0)
        while True:
            data = connection.recv(4096)
            if data:
                file_data += data
                print('Recebido ' + str(len(data)) +' bytes')
                # connection.sendall(data)
            else:
                print('Não há mais dados de ' + str(client_address) + '. Total de bytes recebidos: ' + str(len(file_data)))
                break    
    finally:
        print('Salvando dados.')
        file_name = str(client_address) + "_file"
        write_file = open(file_name, 'wb')
        write_file.write(file_data)
        write_file.close() 

        connection.close() # finaliza a conecxao
