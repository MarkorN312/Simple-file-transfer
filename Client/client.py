import socket

# get "files/kkk.jpg"

HOST = 'localhost'
PORT = 18564

def write_into_file(file, data):
	r = open(file, 'wb')
	r.write(data)
	r.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
	command = input('#files/: ')
	if command == 'end':
		s.close()
		break
	if 'get' in command:
		s.send(bytes(command, 'utf-8'))
		full_data = b''
		while True:
			r = bytes(s.recv(65536))
			if '##end##' in str(r):
				full_data += r.replace(b'##end##', b'')
				break
			full_data += r
		write_into_file('files/' + command[4:len(command)], full_data)
		print('File sucesfully downloaded!')
	else:
		print('Controling the server...')