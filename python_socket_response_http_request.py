import socket

server = socket.socket()
server.bind(('0.0.0.0', 9992))
server.listen()

index_content = '''
HTTP/1.x 200 ok
Content-Type: text/html
<html>
    <head>
    </head>

    <body>
        <p>python socket response http request</p>
    </body>                         
</html> 
'''

while True:
    conn, addr = server.accept()
    request = conn.recv(1024).decode()
    if not request: continue
    method = request.split(' ')[0]
    locate = request.split(' ')[1]
    if method == 'GET' and locate == '/request':
        print('execute sync script')
        conn.sendall(index_content.encode('utf8'))
    conn.close()
