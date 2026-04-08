# posts/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post

# Create your views here.

from django.http import HttpResponse
from .forms import PostForm

def bosh_sahifa(request):
    postlar = Post.objects.filter(published=True)[:5]  # So'nggi 5 ta nashr qilingan postlarni olish
    context = {'postlar': postlar}
    return render(request, 'posts/bosh.html', context)

def haqida(request):
    return render(request, 'posts/haqida.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, published=True)  # Postni olish yoki 404 xatolikni ko'rsatish
    return render(request, 'posts/detail.html', {'post': post})

def foydalanuvchi(request, username):
    return HttpResponse(f"<h1>Foydalanuvchi: {username}</h1> <p>Bu yerda foydalanuvchining profili ko'rsatiladi.</p>")

def maqola(request, slug):
    return HttpResponse(f"<h1>Maqola: {slug}</h1> <p>Bu yerda maqolaning tafsilotlari ko'rsatiladi.</p>")

@login_required(login_url='/login/')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post_id=post.id)  # Yaratilgan postning tafsilot sahifasiga yo'naltirish
    else:
        form = PostForm() # Bo'sh form yaratish

    return render(request, 'posts/post_form.html', {'form': form})

@login_required(login_url='/login/')
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponse("Post muvaffaqiyatli yangilandi!")
    else:
        form = PostForm(instance=post) # Mavjud post ma'lumotlari bilan form yaratish
    
    return render(request, 'posts/post_form.html', {'form': form})

@login_required(login_url='/login/')
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return HttpResponse("Post muvaffaqiyatli o'chirildi!")
    
    return render(request, 'posts/post_confirm_delete.html', {'post': post})