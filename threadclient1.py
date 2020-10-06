import socket# 客户端 发送一个数据，再接收一个数据
import time
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# 获取本地主机名
host = socket.gethostname() 

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))
while True:
    # addr = s.accept()
    # print '连接地址：', addr
	msg = '欢迎xuexi python thread client1222222222！'  #strip默认取出字符串的头尾空格
	s.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
	time.sleep(1)
	print("client send data is running ")
	data = s.recv(20) #接收一个信息，并指定接收的大小 为1024字节
	print('recv:',data.decode("utf8","ignore")) #输出我接收的信息
s.close() #关闭这个链接