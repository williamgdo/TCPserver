import socket
import sys

# cria o socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'    	# configura o ip hospedeiro para a conexao
port = 2019             # porta de comunicacao (a mesma que a do servidor)
print('Se conectando a ' + host + ', porta ' + str(port))

sock.connect((host, port))  # conecta o socket na porta em que o server esta escutando

try:
    opcao = int(input("Digite 1 para enviar um arquivo ou 2 para baixar o ultimo enviado: "))
    if opcao == 1:       # enviar
        # sock.sendall(bytes(1))      # avisa o servidor que o cliente vai ENVIAR um arquivo

        # recebe o nome do arquivo e carrega os bytes para "file_data"
        try:
            file_name = str(input("Digite o nome do arquivo: "))
            file = open(file_name, "rb")
            file_data = file.read()
            file.close()
            print('Enviando arquivo "' + file_name + '"...')
            sock.sendall(bytes(file_data))      # envia todos os bytes de "file_data" para o socket
        except Exception as ex:
            print(ex)
    elif opcao == 2:     # receber
        # sock.sendall(bytes(2))      # avisa o servidor que o cliente vai RECEBER um arquivo
        
        # recebe de 0 a 4096 enquanto o arquivo nao for vazio 
        while True:
            data = sock.recv(4096)  
            if data:
                file_data += data
                print('Recebido ' + str(len(data)) +' bytes')
            else:
                print('Não há mais dados de ' + str(host) + '. Total de bytes recebidos: ' + str(len(file_data)))
                break  

         # se o arquivo nao for vazio, salva com o nome server_file
        if len(file_data) > 0:     
            print('Salvando dados...')
            file_name = "server_file"
            write_file = open(file_name, 'wb')
            write_file.write(file_data)
            write_file.close() 
    else:   
        print("Opcao invalida.")

finally:
    sock.close()
    print('Socket fechado.')
