
# 启动方法(需要先启动):  python -m visdom.server 或者直接敲 visdom
# http://localhost:8097

def demo01():
    import visdom
    import numpy as np
    vis = visdom.Visdom()
    vis.text('Hello, world!')
    vis.image(np.ones((3, 10, 10)))

def demo02():
    import torch as t
    import visdom as vis
    v=vis.Visdom(env='linetest')
    x=t.arange(1,30,0.01)
    y=t.sin(x)
    v.line(X=x,Y=y,win='sinx',opts={'title':'y.sin(x)'})

demo01()