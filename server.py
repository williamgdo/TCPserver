import socket
import sys

# cria o socket TCP/IP 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'       # hostname para ser vinculado
port = 2019              # porta a ser usada

print('Server iniciado no ip ' + host + ', porta ' + str(port))
sock.bind((host, port))

sock.listen(1)          # se prepara para conexoes

while True:
    # espera uma conexao
    print('Esperando uma conexao...')
    connection, client_address = sock.accept()

    try:
        print('Conexao de ' + str(client_address))
        file_data = bytes(0)

        # data = connection.recv(1)   # recebe "opcao" do cliente (enviar ou receber arquivo)

        # if int(data) == 1:      # cliente envia um arquivo
            # recebe de 0 a 4096 enquanto o arquivo nao for vazio 
            
        while True: 
            data = connection.recv(4096)    
            if data:
                file_data += data
                print('Recebido ' + str(len(data)) +' bytes')
            else:
                print('Não há mais dados de ' + str(client_address) + '. Total de bytes recebidos: ' + str(len(file_data)))
                break    
        # se o arquivo nao for vazio, salva com o nome {ip do cliente, socket#}_file
        if len(file_data) > 0:   
            print('Salvando dados...')
            file_name = str(client_address) + "_file"
            write_file = open(file_name, 'wb')
            write_file.write(file_data)
            write_file.close() 

        # elif int(data) == 2:    # cliente recebe um arquivo
        #     connection.sendall(data)
        # else:
        #     print('Opcao invalida.')

    finally:
        connection.close() # finaliza a conecxao
