"""
binhex --- 对binhex4文件进行编码和解码
源代码: Lib/binhex.py

此模块以binhe4格式对文件进行编码和解码，该格式允许Macintosh文件以ASCII格式表示。仅处理数据分支。

binhex 模块定义了以下功能：

binhex.binhex(input, output)
将带有文件名 输入 的二进制文件转换为binhex文件 输出 。输出参数可以是文件名或类文件对象（ write() 和 close() 方法的任何对象）。

binhex.hexbin(input, output)
解码binhex文件输入。 输入 可以是支持 read() 和 close() 方法的文件名或类文件对象。生成的文件将写入名为 output 的文件，除非参数为 None ，在这种情况下，从binhex文件中读取输出文件名。
"""