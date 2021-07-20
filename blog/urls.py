from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('product-categories', views.ProductCategoriesView.as_view(), name='product-categories'),
    path('product-categories/<slug:slug>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('products', views.ProductsView.as_view(), name='products'),
    path('products/<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
    path('blog', views.PostsView.as_view(), name='posts'),
    path('blog/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('youtube-videos', views.youtube_videos, name='youtube-videos')
]