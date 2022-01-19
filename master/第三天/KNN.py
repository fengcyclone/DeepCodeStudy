import random
import csv
# 提供读取scv和写入scv
# -*- coding: UTF-8 -*-

with open("Prostate_Cancer.csv",'r') as file:
    # 打开文件
    reader = csv.DictReader(file)
    datas = [row for row in reader]
    # 将每一个ordereddict放到一个ordereddict列表里

random.shuffle(datas)
# 打乱顺序防止数据过于单一
n = len(datas) // 3
# 取得n

test_set = datas[0:n]
train_set = datas[n:]
# 前n个作为测试集，其余为训练集

# 求”距离“
def distance(d1,d2):
    res = 0.0
    for key in ("radius", "texture", "perimeter", "area", "smoothness", "compactness", "symmetry", "fractal_dimension"):
        res += (float(d1[key]) - float(d2[key]))**2
    return res ** 0.5
        #求欧几里得距离


K = 5
def knn(data):
    res = [
        {"result": train["diagnosis_result"],"distance":distance(data,train)}
        for train in train_set
    ]
    # res 存的是诊断结果和距离
    res = sorted(res,key = lambda item : item['distance']) # 升序排列
    res2 = res[0:K]
    # 取前K个数据
    result = {'B': 0, 'M': 0}
    sum = 0
    # 总距离
    for r in res2:
        sum +=r['distance']

    for r in res2:
        result[r['result']] += 1 - r['distance']/sum
        # 求出B和M的可能性
    if result['B'] > result['M']:
        return 'B'
    else:
        return 'M'
#运算部分结束
#开始测试

correct = 0
for test in test_set:
    result = test['diagnosis_result']
    result2 = knn(test)

    if result == result2:
        correct += 1

success = correct/len(test_set)
print(success)
#求出准确率，根据这里来改变k值提高准确率

'''
KNN
通用步骤：
    计算距离
    升序排序
    取前K个
    加权平均
K的选取
    K太大：分类模糊
    K太小：受个例影响严重
'''