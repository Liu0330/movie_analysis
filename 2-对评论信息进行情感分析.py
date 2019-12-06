import pandas as pd
from snownlp import SnowNLP
pd.set_option('display.max_columns',5)
# 该方法的作用将评论，进行情感分析
def convert(comment):
    snow = SnowNLP(str(comment))
    sentiments = snow.sentiments#0（消极） ~ 1(积极)
    return sentiments
if __name__ == '__main__':
    # pandas python data analysis lib
    # DataFrame(行，列)行样本，列属性
    data = pd.read_csv('./climb.csv','\t')
    # 获取评论数据，进行情感分析，DataFrame新增加一列
    # 属性名：情感评分
    data['情感评分'] = data.comment.apply(convert)
    data.sort_values(by = '情感评分',ascending=False,inplace=True)
    # 保存数据
    data.to_csv('./climb_snownlp.csv',sep = '\t',index = False,encoding='utf-8')
    # 积极评论
    print(data[:10])

    # 消极评论
    print(data[-10:])