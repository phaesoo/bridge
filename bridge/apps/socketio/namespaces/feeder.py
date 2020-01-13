from flask_socketio import Namespace, emit


"""
# client example
import socketio

client = socketio.Client()
namespace = "/feeder"
client.connect('http://localhost:8000', namespaces=[namespace])

# correspond with method 'on_message'
client.emit("message", {"foo": "bar"}, namespace=namespace)

client.disconnect()

# connection check
client.connected
"""


class FeederNamespace(Namespace):
    def on_connect(self):
        print ("on connect")

    def on_disconnect(self):
        print ("on disconnect")

    def on_message(self, data):
        print ("data: {}".format(data))
        # do something