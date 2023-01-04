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
    if request.method == 'GET':
        ca= request.GET.get('catg')
        print(ca)
        book_name, comic_file_name, book, chapter = comic_scrap.scrap(ca,ca)
                
        print(book)
    #接著再去render 圖片檔案
    return render(request, 'read_comic.html', context={'book_name':book_name, 'comic_file_name':comic_file_name, 'book':book, 'chapter':chapter})

def read_next_chapter(request):
    book = request.GET.get('book')
    chapter = int(request.GET.get('chapter'))
    print('read_next_chapter: ',book)
    print('chapter: ', chapter, type(chapter))
    book_name, comic_file_name, chapter = comic_scrap.next_chap(book,chapter)
    return render(request, 'read_comic.html', context={'book_name':book_name, 'comic_file_name': comic_file_name, 'book':book, 'chapter':chapter})