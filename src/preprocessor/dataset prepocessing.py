# 数据集预处理第3步，也是最后一步
# 本文件任务：根据第1步抽取的地区数据集基础上，对部分字段进行大小写转换等操作，便于后续的查询
# 需要处理的文件包括： extracted_CA中的business,review和user三个文件
# 处理完之后的数据集被保存在processed_CA中

import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem import WordNetLemmatizer

# # 1. 处理 business 文件，name 转成小写，categories 变成小写并去除标点符号
# business_infile = 'extract_CA/business.json'
# business_outfile= 'processed_data/business.json'
# with open(business_infile, 'r', encoding='utf-8') as infile:
#     data = json.load(infile)
#     for item in data:
#         # 将 name 转换为小写
#         item['name'] = item['name'].lower()
#         # 将 categories 转成小写并去除标点
#         if item['categories']:
#             item['categories'] = item['categories'].translate(str.maketrans('', '', string.punctuation)).lower()
# # 将 JSON 数据格式化输出到文件
# with open(business_outfile, 'w') as outfile:
#         json.dump(data, outfile, indent=4)  # 使用indent=4进行格式化输出


# # 2. 处理 review 文件，对 text 这个属性进行：大小写转换，去除标点符号，去除停用词，词形还原
# review_infile = 'extract_CA/review.json'
# review_outfile= 'processed_data/review.json'
# with open(review_infile, 'r', encoding='utf-8') as infile:
#         data=json.load(infile)
#         for item in data:
#                 text = item['text']
#                 # 进行文本分割
#                 tokens = word_tokenize(text)
#                 # 加载停用词
#                 stop_words = set(stopwords.words('english'))
#                 # 去除停用词
#                 filtered_texts = [word for word in tokens if word not in stop_words]
#                 # 获取标点符号
#                 punctuation = set(string.punctuation)
#                 # 去除标点符号
#                 clean_tokens = [word for word in filtered_texts if word not in punctuation]
#                 # 词形还原
#                 lemmatizer = WordNetLemmatizer()
#                 lemmatized_texts = [lemmatizer.lemmatize(word) for word in clean_tokens]
#                 # 统一大小写
#                 processed_texts = [word.lower() for word in clean_tokens]
#                 # 还原成 string 形式
#                 processed_texts = ' '.join(processed_texts)
#                 item['text'] = processed_texts
# # 将 JSON 数据格式化输出到文件
# with open(review_outfile, 'w') as outfile:
#         json.dump(data, outfile, indent=4)  # 使用indent=4进行格式化输出

# 3. 处理 user 文件，name 转成小写
user_infile = 'extract_CA/user.json'
user_outfile= 'processed_data/user.json'
with open(user_infile, 'r', encoding='utf-8') as infile:
    data = json.load(infile)
    for item in data:
        # 将 name 转换为小写
        item['name'] = item['name'].lower()
# 将 JSON 数据格式化输出到文件
with open(user_outfile, 'w') as outfile:
        json.dump(data, outfile, indent=4)  # 使用indent=4进行格式化输出









