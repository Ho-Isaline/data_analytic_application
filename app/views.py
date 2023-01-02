from django.shortcuts import render
from crawl_pic_cate import send_categories
from picture import send_pc1


# Create your views here.
def index(request):
    
    all = {"categories":send_categories(), 'plot_div': send_pc1()}
    return render(request, "index.html", context = all)