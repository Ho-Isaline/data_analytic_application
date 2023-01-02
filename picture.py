import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.offline import plot
from plotly.graph_objs import Scatter, Layout




manhua_info = pd.read_csv('manhua_rank.csv')
manhua_info.drop('Unnamed: 0', axis=1,inplace=True)
manhua_info.head()
manhua_info.iloc[:, 2].value_counts()
print(manhua_info["catagory"])
catagory_list = {}
for catagories in manhua_info.iloc[ :, 5]:
    index_num = 0
    comment_ammount = manhua_info.iloc[index_num, 4]
    for catagory in catagories.strip('[').strip(']').split(','):
        catagory = catagory.strip().strip("'")
        if catagory in catagory_list.keys():
            catagory_list[catagory]+=comment_ammount
        else:
            catagory_list[catagory]=comment_ammount

for i in manhua_info.iloc[:, 5]:
    for a in i.strip('[').strip(']').split(','):
        print(a.strip().strip("'"))
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# plt.bar(x=catagory_list.keys(), height=catagory_list.values())
# plt.xticks(rotation=90)

# plt.show()

x_data = list(catagory_list.keys())
y_data = list(catagory_list.values())
plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
def send_pc1():
    return plot_div