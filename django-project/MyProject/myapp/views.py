from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    articles= Article.objects.all()
    print(articles)
    return render(request,"index.html",{"article":articles})