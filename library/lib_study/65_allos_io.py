import io

# f = open("myfile.jpg", "rb", buffering=0) 非缓冲 I/O
# f = open("myfile.jpg", "rb")
# f = io.BytesIO(b"some initial binary data: \x00\x01")

# f = open("myfile.txt", "r", encoding="utf-8")
f = io.StringIO("some initial text data")
f.write("123")
f.seek(0)
print(f.readlines())


output = io.StringIO()
output.write('First line.\n')
print('Second line.', file=output)

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()
print(contents)

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()
