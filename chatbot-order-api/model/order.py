import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))

from util.file_helper import FileReader

import pandas as pd

class OrderModel :
    def __init__(self) :
        self.reader = FileReader()

    def hook_process(self) :
        order = self.get_order()

    def get_order(self) :
        reader = self.reader
        reader.context = os.path.join(baseurl)
        reader.fname = 'order.csv'
        reader.new_file()
        order = reader.csv_to_dframe()
        print(f'{order.head()}')
        return order

    def set_corroef(self) :
        pass


    def get_csv(self):
        reader = self.reader
        reader.context = os.path.join(baseurl,'saved_data')
        reader.fname = 'order_data.csv'
        reader.new_file()
        order_data = pd.read_csv(reader.new_file(), encoding='utf-8', sep =',', index_col='구별')
        print(f'{order_data.head()}')
        return order_data





if __name__ == '__main__':
    order = OrderModel()
    order.hook_process()
    