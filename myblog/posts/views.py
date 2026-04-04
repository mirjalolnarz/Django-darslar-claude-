from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def bosh_sahifa(request):
    return HttpResponse("<h1>Salom, bu mening birinchi blog sahifam!</h1> <p>Bu yerda men blog postlarini joylashtiraman.</p>")

def haqida(request):
    return HttpResponse("<h1>Bu mening blogim haqida sahifa!</h1> <p>Bu yerda men o'zim va blogim haqida ma'lumot beraman.</p>")

def post_detail(request, post_id):
    return HttpResponse(f"<h1>Post {post_id} tafsilotlari</h1> <p>Bu yerda postning tafsilotlari ko'rsatiladi.</p>")

def foydalanuvchi(request, username):
    return HttpResponse(f"<h1>Foydalanuvchi: {username}</h1> <p>Bu yerda foydalanuvchining profili ko'rsatiladi.</p>")

def maqola(request, slug):
    return HttpResponse(f"<h1>Maqola: {slug}</h1> <p>Bu yerda maqolaning tafsilotlari ko'rsatiladi.</p>")