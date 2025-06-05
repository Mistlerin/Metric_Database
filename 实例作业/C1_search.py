#第一章实例查询实现
from DataType import DataType as DT
from tools import Distance

#三角不等式查询
class Tri_Search:
    def __init__(self, data, distance_function):
        self.data = data
        self.d = distance_function
        self.count = 0
        self.results = []
        self.nearest_neighbor = None
        self.min_dist = float('inf')


    #重置结果记录
    def reset(self):
        self.count = 0
        self.results = []
        self.nearest_neighbor = None    #最近邻点
        self.min_dist = float('inf')        #最近距离

    #统计距离计算次数
    def compute(self, a, b):
        self.count += 1
        return self.d(a, b)

    #三角不等式搜索
    def search(self, query, pivot):
        self.reset()
        d_qp = self.compute(query, pivot)       #查询点与支撑点的距离

        for item in self.data:
            if item == pivot:               #支撑点已被排除
                continue

            d_ip = self.d(item, pivot)          # 不计入 count
            lower_bound = abs(d_qp - d_ip)
            upper_bound = abs(d_qp + d_ip)      #三角不等式上下界

            actual_distance = "-"       #若可以排除或包含则不需要计算实际距离
            if d_qp < lower_bound:
                judgement = "Y"         #包含
            elif d_qp > upper_bound:
                judgement = "N"         #排除
            #否则计算实际距离
            else:
                d_iq = self.compute(item, query)
                actual_distance = f"{d_iq:.3f}"
                judgement = "-"         #“-”表示无法判断
                if d_iq < self.min_dist:
                    self.min_dist = d_iq
                    self.nearest_neighbor = item.data_id

            self.results.append({
                "id": item.data_id,
                "d(i,q)范围": f"[{lower_bound:.3f}, {upper_bound:.3f}]",
                "判断结果": judgement,
                "实际d(i,q)": actual_distance
            })

    def display(self):
        if not self.results:        #没有找到结果
            print("No search results.")
            return

        # 表头
        headers = ["id", "Range d(i,q)", "Judgement", "Actual d(i,q)",]
        col_widths = [10, 20, 16, 12]

        def format_row(values):
            return "".join(str(v).ljust(w) for v, w in zip(values, col_widths))
        print(format_row(headers))
        print("-" * sum(col_widths))        # 分隔线

        for r in self.results:
            row = [
                r["id"],
                r["d(i,q)范围"],
                r["判断结果"],
                r["实际d(i,q)"],
            ]
            print(format_row(row))

        print(f"\n总距离计算次数: {self.count}")
        if self.nearest_neighbor is not None:
            print(f"查询点的最近邻是: {self.nearest_neighbor}，距离为: {self.min_dist:.3f}")
        else:
            print("查询点的最近邻无法确定（所有点都被排除）。")

# 查询并输出
def run_search(data_list, metric_func):
    print(f"\n=== 使用距离函数: {metric_func.name} ===\n")
    for query in data_list:
        searcher = Tri_Search(data=data_list, distance_function=metric_func)
        for p in data_list:
            if query == p:
                continue
            print(f"\n--- 查询点: {query.data_id} | 支撑点: {p.data_id} ---\n")
            searcher.search(query=query, pivot=p)
            searcher.display()

#查找示例
data_list= DT.VectorData.get_data("../Data/5dim.txt",3,3)

# 距离函数
euclidean = Distance.EuclideanD()
outlier = Distance.OutlierD()

# 执行查询
run_search(data_list, euclidean)
run_search(data_list, outlier)
