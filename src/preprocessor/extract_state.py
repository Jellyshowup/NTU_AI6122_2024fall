# 数据集预处理第1步
# 本文件任务：根据地区精简数据集，选取的是加州，即（CA）
# 需要处理的文件包括： business,review和user
# 处理完之后的数据集被保存在extracted_CA中

import json


# 1. 处理 business 文件: 筛选出CA这个州的店铺，并保留 business id
def create_business_dataset(business_file, state):
    business_data = []
    # 使用集合提高检索效率，避免元素重复
    business_id = set()
    with open(business_file, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            item = json.loads(line)
            if item['state'] == str(state):
                business_data.append(item)
                business_id.add(item['business_id'])
    # 将列表保存到 json 文件
    with open('extract_CA/business.json', 'w', encoding='utf-8') as f:
        json.dump(business_data, f, ensure_ascii=False, indent=4)  # ensure_ascii=False 保持非 ASCII 字符，indent=4 让输出美观
    return business_id


# 处理 review 文件：根据 business_id，在 review 文件中筛选出 CA 店铺的评价条目
def create_review_dataset(review_file, business_id):
    review_data = []
    review_user_id = set()
    with open(review_file, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            item = json.loads(line)
            if item['business_id'] in business_id:
                review_data.append(item)
                review_user_id.add(item['user_id'])
    with open('extract_CA/review.json', 'w', encoding='utf-8') as f:
        json.dump(review_data, f, ensure_ascii=False, indent=4)
    return review_user_id


# 处理 user 文件：根据user_id，在 user 文件中筛选评价过CA这些店铺的用户信息
def create_user_dataset(user_file, user_id):
    user_data = []
    with open(user_file, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            item = json.loads(line)
            if item['user_id'] in user_id:
                user_data.append(item)
    with open('extract_CA/user.json', 'w', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=4)  # ensure_ascii=False 保持非 ASCII 字符，indent=4 让输出美观


# 主程序
if __name__ == '__main__':
    # 加载json文件
    business_file = "E:\\NTU_Learn\\Text\\yelp_academic_dataset_business.json"
    review_file = "E:\\NTU_Learn\\Text\\yelp_academic_dataset_review.json"
    user_file = "E:\\NTU_Learn\\Text\\yelp_academic_dataset_user.json"
    # 处理 business 文件
    business_id = create_business_dataset(business_file, 'CA')
    # 处理 review 文件
    CA_user_id = create_review_dataset(review_file, business_id)
    print(len(CA_user_id)) # output:155949
    # 处理 user 文件
    create_user_dataset(user_file, CA_user_id)
