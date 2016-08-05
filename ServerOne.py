#import server
import SimpleHTTPServer
import SocketServer
PORT=8000

#set up simple IP Address
Handler =simpleHTTPServer.SimpleHTTPReuesthandler
httpd=SocketServer/TPServer(("",PORT),Handler)

#run forever
httpd.serve_forever()

