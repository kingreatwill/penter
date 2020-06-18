"""
用于构建和运行分布式应用程序的快速而简单的框架。
Ray与RLlib(一个可伸缩的强化学习库)和Tune(一个可伸缩的超参数调优库)打包在一起。
https://github.com/ray-project/ray
"""
import ray
ray.init()

@ray.remote
def f(x):
    return x * x

futures = [f.remote(i) for i in range(4)]
print(ray.get(futures))