args = {
    "prototxt": r"E:\bigdata\ai\opencv-4.3.0\samples\dnn\face_detector\deploy.prototxt",
    "input": r"E:\openjw\penter\third\imagelib\lenna.jpg",
}


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def dict_to_object(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    inst = Dict()
    for k, v in dictObj.items():
        inst[k] = dict_to_object(v)
    return inst

print(dict_to_object(args).input)

n = int(input("请输入一个整数"))
s = "*"
for i in range(1, n, 2):
    print((s*i).center(n))
for i in reversed(range(1, n-2,2)):
    print((s * i).center(n))



