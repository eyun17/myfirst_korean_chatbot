import socket


class BotServer:
    def __init__(self, srv_port, listen_num):
                      # 소켓 서버 포트번호 # 수락할 클라이언트 수
        self.port = srv_port
        self.listen = listen_num
        self.mySock = None

    # sock 생성
    # wrapper function
    def create_sock(self):
        self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySock.bind(("0.0.0.0", int(self.port)))
        self.mySock.listen(int(self.listen))
        return self.mySock

    # client 대기 후 연결 수락
    def ready_for_client(self):
        return self.mySock.accept()
                # 반환값 (conn-클라이언트와 데이터 송수신할 수있는 클라이언트소켓, address-클라 소켓의 바인드된 주소)

    # sock 반환
    def get_sock(self):
        return self.mySock