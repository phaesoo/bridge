import socketio
import time


class Provider:
    __host = "http://localhost"
    __port = 8000

    def __init__(self):
        self.__client = socketio.Client()
        self.__ns = "/feeder"
        self.__client.connect("{}:{}".format(Provider.__host, Provider.__port), namespaces=[self.__ns])

    def __del__(self):
        self.__client.disconnect()

    def main(self, loop):
        self.__client.emit("message", {"foo":"bar{}".format(loop)}, namespace=self.__ns)


if __name__ == "__main__":
    provider = Provider()
    for i in range(100):
        time.sleep(1)
        provider.main(i)
