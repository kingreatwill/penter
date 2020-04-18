"""
pip3 install pytest-html -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

pytest --html=report.html # 会在当前目录下创建一个report.html的测试报告
# 上面命令生成的报告，css是独立的，分享报告的时候样式会丢失，为了更好的分享发邮件展示报告，可以把css样式合并到html里
pytest --html=report.html --self-contained-html
"""