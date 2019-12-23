import pandas as pd
import re
pat=re.compile("shenfenzheng = (.*?);")
###果树财富
class RongShang360():
    def __init__(self):
        pass

    def fetch(self):
        new_df = pd.DataFrame()
        for i in range(1, 2):
            df = pd.read_html(f"http://www.ronxinton.com/blacklist/yuqi/{i}.html", encoding='utf-8',header=0)[0]
            new_df = pd.concat([new_df, df], ignore_index=True)
        new_df["身份证号码"]=new_df["身份证号码"].apply(lambda x:pat.findall(x)[0])
        results = new_df.T.to_dict().values()
        return results


if __name__ == '__main__':
    rs = RongShang360()
    res = rs.fetch()
    print(res)