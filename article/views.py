from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.

def article(request):
    keyword = request.GET.get("keyword")
    
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
    else:
        articles = Article.objects.all()

    return render(request,"article.html",{"articles":articles})


def index(request):
    context = {
        'number':123
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")
@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        'articles' : articles
    }
    return render(request,"dashboard.html",context = context)
@login_required(login_url = "user:login")
def addarticle(request):

    form = ArticleForm(request.POST or None,request.FILES or None)
   
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla kaydedildi.")
        return redirect("index")
    return render(request,"addarticle.html",{'form':form})

def detail(request,id):
   # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()
    return render(request,"detail.html",context={"article":article,"comments":comments})
@login_required(login_url = "user:login")
def update(request,id):
    
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None, request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla güncellendi.")
        return redirect("article:dasghboard")
        
    return render(request,"update.html",context={"form":form})
@login_required(login_url = "user:login")
def delete(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()

    messages.success(request,"Makale Başarıyla silindi")
    return redirect("article:dashboard")

def addcomment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author = request.POST.get("name")
        comment_content = request.POST.get("content")
        
        newComment = Comment(comment_author = comment_author,comment_content=comment_content)

        newComment.article = article

        newComment.save()

    return redirect(reverse("article:detail",kwargs={"id":id}))