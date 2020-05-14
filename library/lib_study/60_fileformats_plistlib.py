# 生成与解析 Mac OS X .plist 文件
import datetime
import plistlib
import time

pl = dict(
    aString="Doodah",
    aList=["A", "B", 12, 32.1, [1, 2, 3]],
    aFloat=0.1,
    anInt=728,
    aDict=dict(
        anotherString="<hello & hi there!>",
        aThirdString="M\xe4ssig, Ma\xdf",
        aTrueValue=True,
        aFalseValue=False,
    ),
    someData=b"<binary gunk>",
    someMoreData=b"<lots of binary gunk>" * 10,
    aDate=datetime.datetime.fromtimestamp(time.mktime(time.gmtime())),
)
with open("60_fileformats_plistlib.plist", 'wb') as fp:
    plistlib.dump(pl, fp)
with open("60_fileformats_plistlib.plist", 'rb') as fp:
    pl = plistlib.load(fp)
print(pl["anInt"])