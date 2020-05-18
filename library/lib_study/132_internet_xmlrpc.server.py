from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import datetime


def is_even(n):
    return n % 2 == 0


def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)


def python_logo():
    with open("python_logo.jpg", "rb") as handle:
        return xmlrpc.client.Binary(handle.read())


server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_introspection_functions()  # proxy.system.listMethods()
server.register_multicall_functions()
server.register_function(is_even, "is_even")
server.register_function(today, "today")


# server.register_function(python_logo, 'python_logo')
# Register a function under a different name
def adder_function(x, y):
    return x + y


server.register_function(adder_function, 'add')
server.register_function(lambda x, y: x + y, 'add3')


# class ExampleService:
#     def getData(self):
#         return '42'
#
#     class currentTime:
#         @staticmethod
#         def getCurrentTime():
#             return datetime.datetime.now()
#
#
# server.register_instance(ExampleService(), allow_dotted_names=True)


# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'mul').
class MyFuncs:
    def mul(self, x, y):
        return x * y


server.register_instance(MyFuncs())


@server.register_function(name='add2')
def adder_function(x, y):
    return x + y


# Register a function under function.__name__.
@server.register_function
def mul2(x, y):
    return x * y


server.serve_forever()
