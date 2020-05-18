# 内存分析 https://docs.python.org/zh-cn/3/library/tracemalloc.html
import tracemalloc

tracemalloc.start()

# ... run your application ...

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
# 显示内存分配最多的10个文件：
print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)

# 获取两个快照并显示差异：
snapshot1 = tracemalloc.take_snapshot()
# ... call the function leaking memory ...
snapshot2 = tracemalloc.take_snapshot()

top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("[ Top 10 differences ]")
for stat in top_stats[:10]:
    print(stat)