# posts/views.py
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView,
    TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q, Count
from .models import Post
from .forms import PostForm


# --- Ro'yxat ---
class PostListView(ListView):
    model               = Post
    template_name       = 'posts/bosh.html'
    context_object_name = 'postlar'
    paginate_by         = 5

    def get_queryset(self):
        queryset = Post.objects.filter(published=True)

        # URL da ?q=django bo'lsa qidiruv
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Statistika qo'shamiz
        context['jami_postlar'] = Post.objects.filter(published=True).count()
        context['qidiruv'] = self.request.GET.get('q', '')
        return context


# --- Bitta post ---
class PostDetailView(DetailView):
    model         = Post
    template_name = 'posts/detail.html'
    # Avtomatik: {{ object }} yoki {{ post }} — context_object_name bilan
    context_object_name = 'post'


# --- Yaratish ---
class PostCreateView(LoginRequiredMixin, CreateView):
    model         = Post
    form_class    = PostForm
    template_name = 'posts/post_form.html'
    login_url     = '/login/'

    # def post(self, request, *args, **kwargs):
    #     form = PostForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         return redirect('post_detail', pk=post.pk)
    #     return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        # Saqlashdan oldin muallif qo'shamiz
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return f'/posts/{self.object.id}/'


# --- Tahrirlash ---
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model         = Post
    form_class    = PostForm
    template_name = 'posts/post_form.html'
    login_url     = '/login/'

    def get_success_url(self):
        return f'/posts/{self.object.id}/'


# --- O'chirish ---
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model         = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url   = reverse_lazy('bosh')   # o'chirilgandan keyin bosh sahifa
    login_url     = '/login/'


# --- Haqida ---
class HaqidaView(TemplateView):
    template_name = 'posts/haqida.html'