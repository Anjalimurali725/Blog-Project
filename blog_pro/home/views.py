from django.shortcuts import render, get_object_or_404
from.models import blog
from.models import latest


# Create your views here.
def home(request, start_date=None):
    obj=blog.objects.order_by('-date')
    obje=latest.objects.order_by('-date')
    return render(request,'index.html',{'data':obj,'data1':obje})

def detail(request,id):
    obj1=get_object_or_404(blog,pk=id)
    return render(request,'single-post.html',{'obj':obj1})

def about(request):
    return render(request,'about-us.html')
def contact(request):
    return render(request,'contact.html')

