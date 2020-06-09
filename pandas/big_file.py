import pandas as pd

reader = pd.read_csv('data/servicelogs', iterator=True)
try:
    df = reader.get_chunk(100000000)
except StopIteration:
    print("Iteration is stopped.")

loop = True
chunkSize = 100000
chunks = []
while loop:
    try:
        chunk = reader.get_chunk(chunkSize)
        chunks.append(chunk)
    except StopIteration:
        loop = False
        print("Iteration is stopped.")
df = pd.concat(chunks, ignore_index=True)


"""
使用不同分块大小来读取再调用 pandas.concat 连接DataFrame，将chunkSize设置在1000万条左右。
"""