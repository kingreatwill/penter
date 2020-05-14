import lzma

data = b"Insert Data Here"
with lzma.open("file.xz", "w") as f:
    f.write(data)

# with open("file.xz", "wb") as f:
#     f.write(b"This data will not be compressed\n")
#     with lzma.open(f, "w") as lzf:
#         lzf.write(b"This *will* be compressed\n")
#     f.write(b"Not compressed\n")

with lzma.open("file.xz") as f:
    file_content = f.read()
    print(file_content)
