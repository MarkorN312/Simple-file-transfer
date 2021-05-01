import socket
import os
from os import listdir
from os.path import isfile, join, isdir

HOST = 'localhost'
PORT = 18564

def get_files_in_directory(path):
	files = []
	for f in listdir(path):
		if(isfile(path + f)):
			files.append(path + "/" + f)
	return files

def read_file(file):
	r = open(file, 'rb')
	text = r.read()
	r.close()
	return text

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Listening...')
client, address = s.accept()
print('Connected from: ', address)

while True:
	command = client.recv(1024).decode('utf-8')
	if('get' in command):
		try:
			name_of_file = command[4:len(command)]
			files = get_files_in_directory('files/')
			final_file = ''
			for i in files:
				if(name_of_file in i):
					final_file = i
					break
			client.sendall(bytes(read_file(final_file)))
			client.send(b'##end##')
			#client.close()
			print('File sent!')
		except Exception as e:
			print(e)
			print('Invalid syntax')