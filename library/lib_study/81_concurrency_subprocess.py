import sys
import subprocess

"""
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, 
cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
"""
# stdout 和 stderr 参数不应当与 capture_output 同时提供。
# run() 的返回值, 代表一个进程已经结束.
r1 = subprocess.run(["where", "cmd"], stdout=sys.stdout)
print(r1)
print(r1.args)

p1 = subprocess.Popen(["where", "cmd"])
print(p1)
# https://docs.python.org/zh-cn/3/library/subprocess.html#popen-objects
print(p1.wait())
with subprocess.Popen(["where", "cmd"], stdout=subprocess.PIPE) as proc:
    print(proc.stdout.read())

p2 = subprocess.Popen(["ls", "-l"], shell=True, stdout=subprocess.PIPE,stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
print(p2.stderr.read())
print("------------------")

def subprocess_Popen1():
    print("***通过communicate函数分别输出PopenObject对象的输出流和错误流***")
    args = [["adb", "devices"], ["adb", "devices11"]]
    for arg in args:
        popen_object = subprocess.Popen(arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        object_stdout, object_stderr = popen_object.communicate()
        output = {"popen_object": popen_object,
                  "object_stdout": object_stdout,
                  "object_stderr": object_stderr}
        print(output)
    """
    {'popen_object': <subprocess.Popen object at 0x0000000002212400>, 'object_stdout': b'List of devices attached \r\n106D111805005938\tdevice\r\n\r\n', 'object_stderr': b''}
    {'popen_object': <subprocess.Popen object at 0x0000000002577C18>, 'object_stdout': b'', 'object_stderr': b'Android Debug Bridge version 1.0.31\r\n\r\n -a .....}
    """

    print("***通过stdout和stderr方法输出PopenObject对象输出流和错误流***")
    p0 = subprocess.Popen(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    object_stdout = p0.stdout.read()
    p0.stdout.close()
    object_stderr = p0.stderr.read()
    p0.stderr.close()
    print(object_stdout)        # 结果：b'List of devices attached \r\n338b123f0504\tdevice\r\n\r\n'
    print(object_stderr)        # 结果：b''

    print("***Popen对象stdin写入功能：使用stdout和stderr输出")
    args = ["python", "python1"]
    for arg in args:
        p4 = subprocess.Popen([arg], shell=True, stdout=subprocess.PIPE,
                              stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        p4.stdin.write("print('hello')")
        p4.stdin.close()
        out = p4.stdout.read()
        p4.stdout.close()
        err = p4.stderr.read()
        p4.stderr.close()
        print("out：%s err：%s" % (out, err))
    """
    ***Popen对象stdin写入功能
    out：hello
    err：
    out： err：'python1' 不是内部或外部命令，也不是可运行的程序或批处理文件。
    """

    print("***Popen对象stdin写入功能：使用communicate输出")
    p4 = subprocess.Popen(["python"], stdout=subprocess.PIPE,
                          stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    p4.stdin.write("print('hello')")
    output = p4.communicate()
    print(output)       # 结果：('hello\n', '')

    print("***不含encoding参数***")
    p1 = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    out1 = p1.stdout.readlines()
    print(out1)         # 结果: [b'List of devices attached \r\n', b'106D111805005938\tdevice\r\n', b'\r\n']

    print("***含encoding参数***")
    p2 = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out2 = p2.stdout.readlines()
    print(out2)         # 结果: ['List of devices attached \n', '106D111805005938\tdevice\n', '\n']

    print("***Popen对象检查命令是否结束，等待进程结束")
    print(p2.poll())    # 结果: None
    print(p2.wait())    # 结果: 0
    print(p2.poll())    # 结果: 0

    print("***Popen对象communicate函数，它会阻塞父进程直至子进程完成")
    p3 = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    out = p3.communicate()[0]
    print(out)          # 结果：b'List of devices attached \r\n338b123f0504\tdevice\r\n\r\n'
    print(p3.poll())    # 结果：0
subprocess_Popen1()



def subprocess_Popen2():
    """
    1. 通过管道功能，实现adb shell ps | findstr top功能
    2. 直接为args赋值为一个字符串，实现adb shell ps | findstr top功能
    :return:
    """
    print("***通过管道方式***")
    p1 = subprocess.Popen(["adb", "shell", "ps"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["findstr", "top"], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p2.communicate()
    print(out, err)         # 结果：b'shell     8508  8504  2600   1044  c004e5f8 b6f40938 S top\r\r\n' b''
    print("***通过传一个字符串方式***")
    p3 = subprocess.Popen("adb shell ps | findstr top", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p3.communicate()
    print(out, err)         # 结果：b'shell     8508  8504  2600   1044  c004e5f8 b6f40938 S top\r\r\n' b''
subprocess_Popen2()





print("------")
print(subprocess.getoutput("where cmd"))
print(subprocess.call(["where", "cmd"]))

print(subprocess.check_output(["where", "cmd"]))

