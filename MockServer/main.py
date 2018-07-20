import time
from http.server import HTTPServer

from get_server import Get_Server
from post_server import Post_Server

HOST_NAME = 'localhost'
PORT_NUMBER = 9007

if __name__ == '__main__':
    print('Starting server, use <Ctrl-C> to stop')
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), Post_Server)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
    print('^C received, shutting down server')