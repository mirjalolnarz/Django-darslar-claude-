from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

from django.http import HttpResponse

def bosh_sahifa(request):
    postlar = Post.objects.filter(published=True)[:5]  # So'nggi 5 ta nashr qilingan postlarni olish
    context = {'postlar': postlar}
    return render(request, 'posts/bosh.html', context)

def haqida(request):
    return render(request, 'posts/haqida.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, published=True)  # Postni olish yoki 404 xatolikni ko'rsatish
    return render(request, 'posts/detail.html', {'post': post, 'sarlavha': post.title})

def foydalanuvchi(request, username):
    return HttpResponse(f"<h1>Foydalanuvchi: {username}</h1> <p>Bu yerda foydalanuvchining profili ko'rsatiladi.</p>")

def maqola(request, slug):
    return HttpResponse(f"<h1>Maqola: {slug}</h1> <p>Bu yerda maqolaning tafsilotlari ko'rsatiladi.</p>")