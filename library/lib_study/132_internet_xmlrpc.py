# XML-RPC 是一种远程过程调用方法，它使用通过 HTTP 传递的 XML 作为载体。 有了它，客户端可以在远程服务器上调用带参数的方法（服务器以 URI 命名）并获取结构化的数据。
import datetime
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print(vars(proxy))
    print(dir(proxy))
    # Print list of available methods
    print(proxy.system.listMethods())

    print("3 is even: %s" % str(proxy.is_even(3)))
    print("100 is even: %s" % str(proxy.is_even(100)))

    today = proxy.today()
    # convert the ISO8601 string to a datetime object
    converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
    print("Today: %s" % converted.strftime("%d.%m.%Y, %H:%M"))

    # with open("fetched_python_logo.jpg", "wb") as handle:
    #     handle.write(proxy.python_logo().data)

    multicall = xmlrpc.client.MultiCall(proxy)
    multicall.is_even(3)
    multicall.is_even(100)
    result = multicall()
    print(tuple(result))
    # try:
    #     proxy.add(2, 5)
    # except xmlrpc.client.Fault as err:
    #     print("A fault occurred")
    #     print("Fault code: %d" % err.faultCode)
    #     print("Fault string: %s" % err.faultString)