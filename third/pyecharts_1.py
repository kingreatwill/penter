# https://pyecharts.org/#/zh-cn/quickstart
# https://github.com/pyecharts/pyecharts
from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()

"""
bar.render_notebook()#在Notebook中进行渲染图像
#bar.render("1.html")#在本地生成静态网页
#make_snapshot(snapshot, bar.render(), "bar.png")#在本地生成图表截图
"""

# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# )
# bar.render()
