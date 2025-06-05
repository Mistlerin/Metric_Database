import MetrixDB as M_DB
import numpy as np
#欧几里得距离
class EuclideanD(M_DB.MetricDistance):
    def __init__(self):
        super().__init__("Euclidean Distance")

    def __call__(self, data1, data2):
        return np.linalg.norm(data1.vector - data2.vector)

#孤点空间距离函数
class OutlierD(M_DB.MetricDistance):
    def __init__(self):
        super().__init__("Outlier Distance")

    def __call__(self, data1, data2):
        return np.max(np.abs(data1.vector - data2.vector))
