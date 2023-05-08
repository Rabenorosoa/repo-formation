
from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from django.template import loader
from .models import PostModel
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
@login_required
def indexView(request):
    Posts = PostModel.objects.all().order_by('id')
    paginator = Paginator(Posts , 3)
    pageNb = request.GET.get('page')
    page_obj = paginator.get_page(pageNb)
    nb = Posts.count() 
    message = str(nb) + ' posts'
    if nb <2 :
        message = str(nb) + ' post'
    
    context = {'i' : page_obj , 'nb': nb, 'message': message}  
    
    return render( request,'myApp/home.html',  context)

@login_required
def detailsView(request , id):
    Posts = PostModel.objects.get(id=id)
    context = { 'i': Posts}
    return render(request , 'myApp/details.html', context)

@login_required
def newPostView(request):
    if request.method== 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('myApp:home')
    else:
        form = PostForm()
    context ={'form': form}
    return render(request , 'myApp/newPost.html',context)

@login_required
def updateView(request,id):
    Post = PostModel.objects.get(id=id)
    if Post.user == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES , instance = Post)
            if form.is_valid():
                form.save()
                return redirect('myApp:home')
        else:
            form = PostForm( instance= Post)
        
    else:
        raise Http404
    context = { 'post':Post, 'form':form}
    return render(request, 'myApp/update.html',context)

@login_required
def deleteView(request, id):
    Post = PostModel.objects.get(id=id)
    if Post.user == request.user:
        Post.delete()
    else:
        raise Http404
    return redirect('myApp:home')
    
    
@login_required
def searchview(request):
    search = request.GET.get('search')
    post = PostModel.objects.filter(Q(title__icontains= search)|Q(content__icontains= search)
                                    |Q(image__icontains= search))
    nb = post.count()
    message = str(nb) + ' '+ 'posts'
    if nb <2 :
        message = str(nb) + ' post'
    context = {'search': search, 'post':  post , 'message': message}
    return render(request, 'myApp/search.html', context)