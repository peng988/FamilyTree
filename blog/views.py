from django.shortcuts import render
from django.utils import timezone

import string

from .models import Post
from .models import Family

from .forms import PostForm
from .forms import FamilyForm
from .forms import SearchForm

from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post}) 

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def family_list(request):
    familys = Family.objects.all().order_by('id')
    return render(request, 'blog/family_list.html', {'familys': familys})

def family_detail(request,pk):
    familys = Family.objects.all().order_by('id')
    return render(request, 'blog/family_detail.html', {'familys': familys}) 

def family_new(request):
    if request.method == "POST":
        form_input = FamilyForm(request.POST)
        if form_input.is_valid():
            code123 = form_input.cleaned_data['my_code123']
            familys = Family.objects.filter(my_code123__gte = code123)
            return render(request, 'blog/family_detail.html', {'familys': familys}) 

    else:
        form = FamilyForm()
    return render(request, 'blog/family_edit.html', {'form': form})



def search_new(request):
    if request.method == "POST":
        form_input = SearchForm(request.POST)
        if form_input.is_valid():
            code123 = form_input.cleaned_data['m_input']
            
            T1 = code123.strip('傅')
           
            T = T1.strip('付')
           
            m = len(T) 

            if m > 0 :
                familys = Family.objects.filter(name__icontains = T)
            else:
                familys = Family.objects.filter(name__icontains = code123)
            
            return render(request, 'blog/search_edit.html', {'form': form_input,'m_start': 0,'familys': familys}) 

    else:
        form = SearchForm()
    return render(request, 'blog/search_edit.html', {'form': form,'m_start': 1})


def Fsearch(request):
    q = request.GET['q']
    recontents = Family.objects.filter(sons__contains=q)
    
    rejson = []
    for recontent in recontents:
        rejson.append(recontent.name)
    return HttpResponse(json.dumps(rejson), content_type='application/json')