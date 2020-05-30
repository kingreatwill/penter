# Markdown to HTML
https://github.com/Python-Markdown/markdown  2.2k
## HTML to Markdown
https://github.com/gaojiuli/tomd   0.466k 最近更新一年前
https://github.com/aaronsw/html2text 2k 好像8年没有更新了

```
python html2md.py "https://www.cnblogs.com/kingreatwill/p/9865945.html" "https://segmentfault.com/a/1190000022777293"
python html2md.py "https://www.cnblogs.com/kingreatwill/p/9865945.html" -n filename
python html2md.py "https://www.cnblogs.com/kingreatwill/p/9865945.html" -s ".css"
```
打包成exe:pyinstaller -F html2md.py

-F, –onefile 打包dao成一个exe文件。
-D, –onedir 创建一个目录，包含exe文件，但会依赖很多文件（默认回选项）。
-c, –console, –nowindowed 使用控制台，无界面(默认)
-w, –windowed, –noconsole 使用窗答口，无控制台
