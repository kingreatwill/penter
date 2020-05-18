#! /usr/bin/env python
# encoding=utf8
import pstats
import profile
def func1():
    for i in range(1000):
        pass
def func2():
    for i in range(1000):
        func1()
p = profile.Profile()
p.run("func2()")

#profile.run("func2()")
s = pstats.Stats(p)
s.sort_stats("time", "name").print_stats()