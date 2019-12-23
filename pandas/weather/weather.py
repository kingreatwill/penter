import json
from datetime import datetime

import demjson
import pandas as pd
import requests
from matplotlib import pyplot as plt
from dateutil.relativedelta import relativedelta

from city_code import city_to_code

# https://github.com/boydfd/weather/

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


rain = '雨'
rain_index = ' ' + rain
cloudy = '多云'
cloudy_index = ' ' + cloudy
overcast = '阴'
overcast_index = ' ' + overcast
sunny = '晴'
sunny_index = ' ' + sunny
month_index = 'month'
original_weather_index = 'tianqi'


class Weather:
    def __init__(self, city, log_flag=False):
        self.city = city
        self.city_code = city_to_code[city]
        self.log_flag = log_flag

    def log(self, *args):
        if self.log_flag:
            print(*args)

    def save_weather(self, start, end):
        df = self.read_weather(start, end).dropna().reset_index()
        df.to_csv('./resources/weather/{}.csv'.format(self.city))

    def plot_weather(self, start, end):
        df = self.read_weather(start, end).dropna().reset_index()
        df['weather'] = df.apply(self.weather_category, axis=1)

        from pylab import rcParams
        rcParams['figure.figsize'] = 40, 10
        rcParams.update({'font.size': 22})
        weather_df = df.groupby(['month', 'weather']).aqi.count().unstack().reset_index()
        weather_df.plot.bar(x='month', y=[rain_index, overcast_index, cloudy_index, sunny_index])
        plt.show()

    @classmethod
    def date_generate(cls, start, end):
        start = datetime.strptime(start, '%Y%m')
        end = datetime.strptime(end, '%Y%m')
        while True:
            next_start = start + relativedelta(months=1)
            yield start.strftime('%Y%m')
            if next_start > end:
                break
            start = next_start

    def read_weather(self, start, end):
        dates = self.date_generate(start, end)
        return pd.concat(map(self.get_weather, dates))

    def get_weather(self, date):
        url = self.get_url(date)
        weather = self.get_weather_json(url)
        df = pd.DataFrame(weather)
        df[month_index] = date
        return df

    def get_url(self, date):
        url = 'http://tianqi.2345.com/t/wea_history/js/{date}/{city_code}_{date}.js'.format(
            date=date, city_code=self.city_code)
        return url

    @classmethod
    def weather_category(cls, row):
        tianqi = row[original_weather_index]
        if tianqi.find(rain) != -1:
            return rain_index
        if tianqi.find(overcast) != -1:
            return overcast_index
        if tianqi.find(cloudy) != -1:
            return cloudy_index
        return sunny_index

    def get_weather_json(self, url):
        self.log(url)
        weather = requests.get(url).text.split('=')[1][:-1]
        self.log(weather)
        weather = demjson.decode(weather)['tqInfo']
        return weather


if __name__ == '__main__':
    Weather('深圳').plot_weather('201701', '201906')