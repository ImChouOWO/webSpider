import pandas as pd 
import jieba
import matplotlib.pyplot as plt

def data_clean():


    data = pd.read_csv('homework/PTT_運動內衣_所有資料.csv')
    data.drop_duplicates()
    data.dropna(inplace=True)

    data['ALL'] = data['標題']+data['內文']
    dataIndex = str(data['ALL'].sum())
    removeword = ['span','class','f3','https','imgur','h1','_   blank','href','rel',
                'nofollow','target','cdn','cgi','b4','jpg','hl','b1','f5','f4',
                'goo.gl','f2','email','map','f1','f6','__cf___','KoreaDrama','bbs'
                'html','cf','f0','b2','b3','b5','b6','原文內容','原文連結','作者'
                '標題','時間','看板','<','>','，','。','？','—','閒聊','・','/',
                ' ','=','\"','\n','」','「','！','[',']','：','‧','╦','╔','╗','║'
                ,'╠','╬','╬',':','╰','╩','╯','╭','╮','│','╪','─','《','》','_'
                ,'.','、','（','）','　','*','※','~','○','”','“','～','@','＋','\r'
                ,'▁',')','(','-','═','?',',','!','…','&',';','『','』','#','＝'
                ,'\l']



    for i in removeword:
        dataIndex=dataIndex.replace(i,"")
    words = jieba.lcut(dataIndex , cut_all = False)

    keyWord = ['Nike','Shock_Absorber','addidas','UA','Triumph','Mollifix','Uniqlo','Calvin_Klein']
    voice = {'Nike': 0, 'Shock_Absorber': 0, 'addidas': 0, 'UA': 0, 'Triumph': 0, 'Mollifix': 0, 'Uniqlo': 0, 'Calvin_Klein': 0}

    for  i in keyWord:
        tmp  = words.count(i)
        voice[i] +=tmp
    return voice

def linePlot(brandName, volumes):
    plt.plot(brandName, volumes, marker='o')
    plt.title('Brand Volume')
    plt.xlabel('Brand')
    plt.ylabel('Volume')
    plt.xticks(rotation=90)
    plt.show()
def piePlot(brandName, volumes):
    fig, ax = plt.subplots()
    ax.pie(volumes, labels=brandName, autopct='%1.1f%%', startangle=90, counterclock=False)
    ax.axis('equal')
    plt.title('Volume Proportion')
    plt.show()

if __name__ == "__main__":
    volumeDict = data_clean()
    # volumeDict = {'Nike': 91, 'Shock_Absorber': 0, 'addidas': 2, 'UA': 46, 'Triumph': 0, 'Mollifix': 6, 'Uniqlo': 37, 'Calvin_Klein': 0}
    brandName = list(volumeDict.keys())
    volumes = list(volumeDict.values())
    piePlot(brandName, volumes)
    linePlot(brandName, volumes)