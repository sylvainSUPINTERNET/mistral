class LoadBalancer:

    def __init__(self):
        self.servers = {}


    def add_server(self, server_id: int) -> None:
        self.servers[server_id] = True
        

    def get_server(self, timestamp: int) -> int:
        return self.servers.get(timestamp, -1)

    def report_result(
        self,
        server_id: int,
        success: bool,
        timestamp: int
    ) -> None:
        pass


if __name__ == "__main__":
    lb = LoadBalancer();
    lb.add_server(1)
    lb.add_server(2)
    print(lb.get_server(1))