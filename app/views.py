from django.shortcuts import render
from preprocess import DRAW_PIC
from crawl_pic_cate import comic_scrap


# Create your views here.
def index(request):
    pic = DRAW_PIC()
    all = {"categories":comic_scrap.send_categories(), 'plot_bar': pic.send_bar(),
           'plot_pie' : pic.send_pie(), 'plot_line' : pic.send_line(), 'plot_box' : pic.send_box()}
    return render(request, "index.html", context = all)

def read_comic(request):
    #先取得index過來的漫畫類別
    if request.method == 'GET':
        ca= request.GET.get('catg')
        print(ca)
        book_name, comic_file_name = comic_scrap.scrap(ca)

    #接著再去render 圖片檔案
    return render(request, 'read_comic.html', context={'book_name':book_name, 'comic_file_name':comic_file_name})