import requests
from lxml import etree
import time
url = 'https://movie.douban.com/subject/30413052/comments?start=%d&limit=20&sort=new_score&status=F'
# 请求头就创建好了
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'_ga=GA1.2.557027477.1504366471; _vwo_uuid_v2=938EB395FEDF0DA9E9D90650DE9042F0|e0a43720af285a1e9923074545b60ff1; gr_user_id=d044fe6a-3a16-4f08-ad14-cc71033b6767; __utmv=30149280.16469; douban-fav-remind=1; bid=uZG6zNr6IdM; __yadk_uid=l4ZlS88dSS6QGaomSBmqi5XqNAaUQv5r; viewed="21477429_24703171_24746415_10769749_3288908_5377669_2201479_27055214_30203973_1088812"; acw_tc=2760823015682940060847273e162d65a7cec22e493c6aa10f371b90c5086c; ll="118092"; trc_cookie_storage=taboola%2520global%253Auser-id%3Da1a11787-6229-4357-a25a-b869f8653388-tuctb0db9e; push_doumail_num=0; push_noty_num=0; __utmz=30149280.1569503634.36.32.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1569587035%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E8%25B1%2586%25E7%2593%25A3%26rsv_spt%3D1%26rsv_iqid%3D0x8468d5c7001ff955%26issp%3D1%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_dl%3Dtb%26rsv_sug3%3D8%26rsv_sug1%3D1%26rsv_sug7%3D100%26rsv_sug2%3D0%26inputT%3D1297%26rsv_sug4%3D2192%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.557027477.1504366471.1569503634.1569587035.37; __utma=223695111.557027477.1504366471.1568873724.1569587035.34; __utmb=223695111.0.10.1569587035; __utmz=223695111.1569587035.34.31.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; __utmb=30149280.2.10.1569587035; dbcl2="164698173:AM/bSYaNPzk"; ck=oih5; __utmc=30149280; __utmc=223695111; _pk_id.100001.4cf6=b6270075d3f0f249.1516866774.36.1569588688.1568873723.',
'Host':'movie.douban.com',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Site':'none',
'Sec-Fetch-User':'?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',}
if __name__ == '__main__':
    # 0,20,40,480,……，490
    fp = open('./climb.csv',mode = 'w',encoding='utf-8')
    fp.write('author\tcomment\tvote\n')
    for i in range(26):#左闭右开
        if i == 25:#最后一页
            url_climb = url%(490)
        else:# 0,1,2……，24
            url_climb = url%(i*20)
        response = requests.get(url_climb,headers = headers)
        response.encoding = 'utf-8'
        text = response.text
        html = etree.HTML(text)
        comments = html.xpath('//div[@id="comments"]/div[@class="comment-item"]')
        for comment in comments:
            # 作者
            author = comment.xpath('./div[@class="avatar"]/a/@title')[0].strip()
            # 短评
            p = comment.xpath('.//span[@class="short"]/text()')[0].strip()
            # 点赞
            vote = comment.xpath('.//span[@class="votes"]/text()')[0].strip()
            fp.write('%s\t%s\t%s\n'%(author,p,vote))
        print('第%d页数据保存成功'%(i+1))
        time.sleep(1)
    fp.close()
