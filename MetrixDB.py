import numpy as np

#度量空间数据父类
class MetricData:
    def __init__(self,data_id):
        self.data_id = data_id

    def __str__(self):
        return self.data_id

#度量空间距离函数父类
class MetricDistance:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name



