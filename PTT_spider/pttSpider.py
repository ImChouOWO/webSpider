import pandas as pd
import numpy as np
import jieba
import ast
import warnings
from Ivan_ptt import crawl_ptt_page

warnings.filterwarnings("ignore")

### 下載電影版資料 ###
# underwear = crawl_ptt_page(Board_Name ='movie',start =5001 ,page_num= 1)
# underwear.to_csv('PTT_電影_onepage資料.csv',encoding = 'utf-8')



### 資料處理 ###


ptt_data = pd.read_csv('PTT_電影_onepage資料.csv')


# 將重複與空白訊息去除
ptt_data = ptt_data.drop_duplicates()
ptt_data = ptt_data.dropna()


#改時間格式
ptt_data['時間'] = pd.to_datetime(ptt_data['時間'])


#計算留言總數
ptt_data['留言總數']=ptt_data['推推總數']+ptt_data['噓聲總數']+ptt_data['中立總數']

#將分類為【公告】的去除
ptt_data = ptt_data[ptt_data['類別'] != '公告']


# 將「內容」與「所有留言」文字內容合併，創造一欄位 - 「所有文」
ptt_data['所有文'] = ptt_data['標題'] + ptt_data['內容']

#去除無意義字元，先進行無意義字元列表，可以自行新增
removeword = ['span','class','f3','https','imgur','h1','_   blank','href','rel','nofollow','target','cdn','cgi','b4','jpg','hl','b1','f5','f4',
            'goo.gl','f2','email','map','f1','f6','__cf___','data','bbs''html','cf','f0','b2','b3','b5','b6','原文內容','原文連結','作者'
            '標題','時間','看板','<','>','，','。','？','—','閒聊','・','/',' ','=','\"','\n','」','「','！','[',']','：','‧','╦','╔','╗','║'
            ,'╠','╬','╬',':','╰','╩','╯','╭','╮','│','╪','─','《','》' ,'.','、','（','）','　','*','※','~','○','”','“','～','@','＋','\r'
            ,'▁',')','(','-','═','?',',','!','…','&',';','『','』','#','＝','＃','\\','\\n', '"', '的', '^', '︿','＠','$','＄','%','％',
            '＆','＊','＿','+',"'",'{','}','｛','｝','|','｜','．','‵','`','；','●','§','※','○','△','▲','◎','☆','★','◇','◆','□','■','▽',
            '▼','㊣','↑','↓','←','→','↖','XD','XDD','QQ','【','】'
            ]

for word in removeword:
    ptt_data['所有文'] = ptt_data['所有文'].str.replace(word,'')



# 解析每個留言內容，將其轉換成一個 list
ptt_data['留言內容'] = ptt_data['留言內容'].apply(ast.literal_eval)

# 建立一個空的 DataFrame
new_df = pd.DataFrame()

# 將每個留言內容轉換成一個 Series，並加入新的 DataFrame 中
for i in range(len(ptt_data)):
    comment_list = ptt_data['留言內容'][i]
    for comment in comment_list:
        new_df = new_df.append(pd.Series(comment), ignore_index=True)

new_df.to_csv('PTT_留言內容clear.csv',encoding = 'utf-8')

post = ptt_data[['標題','內容','所有文','推推總數','噓聲總數','中立總數','留言總數','時間','類別']]
post.to_csv('PTT_貼文內容clear.csv',encoding = 'utf-8')