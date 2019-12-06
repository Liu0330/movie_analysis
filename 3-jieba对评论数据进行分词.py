import pandas as pd
import jieba
from jieba import analyse
import matplotlib.pyplot as plt
import numpy as np
import wordcloud
from PIL import Image
if __name__ == '__main__':
    # 获取评论信息
    data = pd.read_csv('./climb.csv',sep = '\t')
    comments = ';'.join([str(c) for c in data['comment'].tolist()])

#     使用jieba库对文本内容进行分词
    gen = jieba.cut(comments)
    words = ' '.join(gen)

    # 对分好词，进行jieba分析
    tags = analyse.extract_tags(words,topK=500,withWeight=True)
    word_result = pd.DataFrame(tags,columns= ['词语','重要性'])
    word_result.sort_values(by = '重要性',ascending=False,inplace=True)#从大到下

    # 可视化，500个词语，选取其中最重要20个进行分析
    plt.barh(y = np.arange(0,20),width =word_result[:20]['重要性'][::-1],)#前20个获取，最重要20个
    plt.ylabel('Importance')
    plt.yticks(np.arange(0,20),labels=word_result[:20]['词语'][::-1],fontproperties = 'KaiTi')
    # 保存条形图,!!!保存代码一定要写到plt.show()之前
    plt.savefig('./条形图_20keywords.jpg',dpi = 200)
    plt.show()

    #词云操作，pip install wordcould
    mountain = np.array(Image.open('./山.jpg'))#词云图片
    #将tags，jieba分词提取出来数据，dict字典
    words = dict(tags)
    cloud = wordcloud.WordCloud(width=1200,height=968,font_path='./simkai.ttf',background_color='white',
                        mask=mountain,max_words=500,max_font_size=150)
    # 词云
    word_cloud = cloud.generate_from_frequencies(words)
    plt.figure(figsize=(12,12))
    plt.imshow(word_cloud)
    # 词云保存
    plt.savefig('./攀登者_词云.jpg',dpi = 200)
    plt.show()