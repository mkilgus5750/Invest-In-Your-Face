from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Post, Product, Category
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
import requests
import os
from dotenv import load_dotenv, find_dotenv
from .cache.single_video import single_video
from .cache.videos import videos


load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")

def get_data(max_results):
    url = f'https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId=UCceIhm3V-JVA_pc2w0MI0HA&part=snippet,id&order=date&maxResults={max_results}'
    headers = {
        'cache-control': "no-cache",
        }
    response = requests.request("GET", url, headers=headers)
    res_data = response.json()
    return res_data

def landing_page(request):
    # UNCOMMENT FOR PRODUCTION
    # res_data = get_data(1)
    posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/landing-page.html', {
        'posts': posts,
         'res_data': single_video
    })

class ProductCategoriesView(ListView):
    model = Category
    template_name = 'blog/products/product-categories.html'
    context_object_name = 'product_categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/products/category-detail.html'

class ProductsView(ListView):
    model = Product
    template_name = 'blog/products/products.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'blog/products/product-detail.html'

class PostsView(ListView):
    model = Post
    template_name = 'blog/posts/all_posts.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/posts/post.html'

def youtube_videos(request):
    #UNCOMMENT FOR PRODUCTION 
    # res_data = get_data(20)
    return render(request, 'blog/youtube/youtube-videos.html', {
        'res_data': videos
    })