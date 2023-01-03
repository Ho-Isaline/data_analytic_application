import pandas as pd
import plotly.express as px
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import numpy as np

class CLEAN_DATA():

    def __init__(self):
        self.comic = pd.read_csv('manhua_rank.csv')
         
    
    def mk_df1(self, mode:str):
        global comic_dic
        comic_dic = {} 
        comment_dic = {}
        score_dic = {}
        lastest_chapter_list = []

        index_num1 = 0
        
        for catagories in self.comic.iloc[ :, 6]:
            index_num2 = 0

            #4 -> comment ammount sum
            #5 -> score ammount sum
            #7 -> latest chapter
            score_amount = self.comic.iloc[index_num2, 4]
            comment_amount = self.comic.iloc[index_num2, 5]
            lastest_chapter = self.comic.iloc[index_num1, 7]
                  
            for catagory in catagories.strip('[').strip(']').split(','):
                catagory = catagory.strip().strip("'")
                lastest_chapter_list.append([catagory, lastest_chapter])
                if catagory in comment_dic.keys():
                    comment_dic[catagory]+=comment_amount
                    score_dic[catagory]+=score_amount          
                
                else:
                    comment_dic[catagory]=comment_amount
                    score_dic[catagory]=score_amount
            index_num1 += 1
            index_num2 += 1 
            
        comic_dic['comment_amount'] = comment_dic
        comic_dic['score_amount'] = score_dic
        comic_df = pd.DataFrame(comic_dic)
        comic_df3 = pd.DataFrame(lastest_chapter_list, columns=['catg','last_chapter']).fillna(0)

        if mode == 'box':
            return comic_df3  
        else:
            return comic_df
        
        
    def mk_df2(self):#第二個df
        publish_dic = {}
        try:
            x = sorted(comic_dic['comment_amount'].items(), key=lambda catagory:catagory[1])
            
        except:
            df = CLEAN_DATA()
            df.mk_df1('')
            x = sorted(comic_dic['comment_amount'].items(), key=lambda catagory:catagory[1])
        
        top_three = x[-3:]
        top_three_category = []
        
        for catagory_type, amout in top_three:
            top_three_category.append(catagory_type) #取得評論數最多的漫畫類別

        for top in ['热血', '魔幻', '冒险']:
            index_num = 0
            each_year_publish_count = {} 

            for catagories in self.comic.iloc[ :, 6]:
                if top in catagories:
                    if self.comic.iloc[index_num, 2] in each_year_publish_count:
                            each_year_publish_count[self.comic.iloc[index_num, 2]] += 1
                    else:
                        each_year_publish_count[self.comic.iloc[index_num, 2]] = 1  
                index_num += 1
            publish_dic[top] = each_year_publish_count
        comic_df2 = pd.DataFrame(publish_dic).fillna(0)
        return comic_df2.sort_index(ascending=True)#年份從小到大



class DRAW_PIC():
    
    def __init__(self):
        self.data = CLEAN_DATA()

    def send_bar(self):
        df = self.data.mk_df1('bar')
        fig = px.bar(df,x=df.index,y='comment_amount',color=df.index, height=400, width=500, text_auto='.1s',
                     labels={'catg': '熱門漫畫類別','comment_amount':'評論總數'}, title="各類別評論總數")
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        fig = fig.to_html
        return fig
    
    def send_pie(self):
        df = self.data.mk_df1('pie')
        fig = px.pie(df, values='score_amount', names = df.index, height=400, width=500, title = '各類別評價人數')
        fig = fig.to_html
        return fig

    def send_box(self):
        df = self.data.mk_df1('box')
        fig = px.box(df,x='catg',y='last_chapter',color='catg', height=400, width=500,
                     labels={'catg': '熱門漫畫類別','last_chapter':'最新章節'}, title="各類漫畫章數分布")
        fig = fig.to_html
        return fig
    
    def send_line(self):
        df = self.data.mk_df2()
        fig = px.line(df,x=df.index,y=df.columns, height=400, width=500,
              labels={'index': '年分','value':'發布次數', 'variable':'熱門漫畫類別'},title="熱門漫畫類別每年發布次數")
        fig = fig.to_html
        return fig