import _thread
import time
import socket
import sys

def threadsend(sock,param):
	print("ThreadName is :",param)
	while True:
		try:
			data = sock.recv(20)  #接收数据
			time.sleep(1)
			print('param recive:',data.decode("utf8","ignore")) #打印接收到的数据
			sock.send(param.encode('utf-8')) #然后再发送数据
		except ConnectionResetError as e:
			print('关闭了正在占线的链接！')
			sock.close()
			break
				
		       
serversocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地主机名

host =socket.gethostname()
port =9999
serversocket.bind((host,port))

serversocket.listen(5)

while True:
	clientsocket,addr = serversocket.accept()
	print("连接地址：%s" %str(addr))
	
	msg = "欢迎访问菜鸟教程！" +str(addr)+str(clientsocket)+"\r\n"
	try:
	   _thread.start_new_thread( threadsend, (clientsocket, msg, ) )
	except:
	   print ("Error: 无法启动线程")	





'''
while 1:
   pass
'''