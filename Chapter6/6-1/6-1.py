
# 初始化字典
def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}

# 查找人员
def lookup(data,label,name):
    return data[label].get(name)

# 存储人员信息
def store(data,full_name):
    names = full_name.split() # 拆分全名，分割出first，middle，last
    if len(names) == 2: names.insert(1, '') # 如果没有中间名，则将中间名设置为空
    labels = 'first', 'middle', 'last' # 创建元组
    for label, name in zip(labels, names):   # 将标签和对应的名字合并
        people = lookup(data, label, name)  # 人员查找
        if people: # 成功找到人员列表
            people.append(full_name) # 追加人员列表
        else: # 没有成功找到人员列表
            data[label][name] = [full_name] # 新建人员序列

# 测试代码
MyNames={}
init(MyNames);
store(MyNames,'Magnus Lie Hetland')
print(lookup(MyNames, 'middle', 'Lie'))