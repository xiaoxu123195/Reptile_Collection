import socket
import threading


def send_msg(udp_socket):
    while True:
        dest_ip = input("\n请输入对方的ip地址:")
        dest_port = int(input("\n请输入对方的post:"))
        while True:
            msg = input("\n请输入要发送的数据:")
            if msg:
                # 发送数据
                udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))
            else:
                break


def recv_msg(udp_socket):
    while True:
        # 接收数据
        recv_msg = udp_socket.recvfrom(1024)
        # 解码
        recv_ip = recv_msg[1]
        recv_msg = recv_msg[0].decode("utf-8")
        # 打印收到的数据
        print(">>>%s:%s" % (str(recv_ip), recv_msg))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    udp_socket.bind(("", 7890))
    # 线程
    send_msg_t = threading.Thread(target=send_msg, args=(udp_socket,))
    recv_msg_t = threading.Thread(target=recv_msg, args=(udp_socket,))
    send_msg_t.start()
    recv_msg_t.start()


if __name__ == "__main__":
    main()
