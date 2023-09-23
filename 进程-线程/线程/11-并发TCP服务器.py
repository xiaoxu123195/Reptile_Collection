import socket
import threading


class HandleData(threading.Thread):
    def __init__(self, client_socket):
        super().__init__()  # 不覆盖父类的方法
        self.client_socket = client_socket

    def run(self):
        # 5.接收/发送数据
        while True:
            recv_content = self.client_socket.recv(1024)
            if len(recv_content) != 0:
                print(recv_content)
                self.client_socket.send(recv_content)
            else:
                self.client_socket.close()
                break


class TCPServer(threading.Thread):
    def __init__(self, port):
        super().__init__()
        # 1.创建套接字
        self.server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.绑定本地信息
        self.server_s.bind(("", port))
        # 3.将套接字由默认的主动链接模式改为被动模式（监听模块）
        self.server_s.listen(128)

    def run(self):
        while True:
            # 4.等待客户端的链接
            new_s, client_info = self.server_s.accept()
            # new_s就是新的套接字 client_info就是元组(刚刚链接的客户端的ip，port)
            print(client_info)
            # 创建一个新的线程， 专门为刚刚链接的客户端服务
            handle_data_thread = HandleData(new_s)
            handle_data_thread.start()

    def __del__(self):
        # 6.关闭套接字
        self.server_s.close()


tcp_server = TCPServer(7788)
tcp_server.start()
