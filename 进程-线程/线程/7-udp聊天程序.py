import socket


def send_msg(udp_socket):
    msg = input("\n请输入要发送的数据:")
    dest_ip = input("\n请输入对方的ip地址:")
    dest_port = int(input("\n请输入对方的post:"))
    # 发送数据
    udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
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
    while True:
        print("="*30)
        print("1:发送消息")
        print("2:接收消息")
        print("="*30)
        op_num = input("请输入要操作的功能顺序序号:")

        if op_num == "1":
            send_msg(udp_socket)
        elif op_num == "2":
            recv_msg(udp_socket)
        else:
            print("输入错误，请重新输入...")


if __name__ == "__main__":
    main()
