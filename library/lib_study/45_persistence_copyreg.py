# 注册配合 pickle 模块使用的函数
import copyreg, copy, pickle
class C(object):
    def __init__(self, a):
        self.a = a

def pickle_c(c):
    print("pickling a C instance...")
    return C, (c.a,)


copyreg.pickle(C, pickle_c)
c = C(1)

d = copy.copy(c) # "pickling a C instance..."
p = pickle.dumps(c) # "pickling a C instance..."

