# 中国体育彩票

from bs4 import BeautifulSoup  as bs
import requests
import os

# 爬取数据+预测测试 https://blog.csdn.net/weixin_42062762/article/details/87658044
def Crawling_data():
    data_1 = []
    # 截止到2020.07.06总共100页 range(1,101)
    for i in range(1, 101):
        url = 'http://www.lottery.gov.cn/historykj/history_' + str(i) + '.jspx?_ltype=dlt'
        data = requests.get(url).text
        data = bs(data, 'lxml')
        data = data.find('tbody').find_all('tr')
        for content in data:
            number = content.get_text().strip().replace('\r', '').replace('\t', '').replace('\n', ' ')
            with open('data_recent', 'a') as f:
                f.write(number + '\n')
    f.close()

# 清洗数据

if __name__ == '__main__':
    Crawling_data()
