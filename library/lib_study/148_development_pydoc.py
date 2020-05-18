# pydoc sys
# pydoc -n <hostname>
# pydoc -p 1234

# python -m pydoc -p 1234
#
# python -m pydoc 模块名
# python -m pydoc -w 148_development_pydoc   -w 选项，该选项代表 write，表明输出 HTML 文档。

def display(add):
    '''
    这是一个函数
    '''
    print(add)


class my_cla:
    '''
    这是一个类
    '''

    def say(self, add):
        '''
        这是一个类实例方法
        '''
        print(add)