import MetrixDB as M_DB
import numpy as np
#向量类型
class VectorData(M_DB.MetricData):
    def __init__(self,data_id,data):
        super().__init__(data_id)
        self.vector = np.array(data)

#从UMAD数据集中读取前l个数据，数据维度为d
    @staticmethod
    def get_data(filepath, l, d):
        vector_list = []
        with open(filepath, 'r') as f:
            for idx, line in enumerate(f):
                if idx > l:
                    break
                parts = line.strip().split()
                if len(parts) < d:
                    continue  # 若维度不够则跳过
                vector = list(map(float, parts[:d]))
                vector_list.append(VectorData(data_id="v"+str(idx), data=vector)) #将各数据命名为v1,v2......vn
        return vector_list
