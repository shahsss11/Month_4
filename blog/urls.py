from django.urls import path
from . import views


urlpatterns = [
    path('message/', views.FirstMessageView.as_view(), name='message'),
    path('emodji/', views.emodji, name='emodji'),
    path('', views.BlogListView.as_view(), name='blog_lst'),
    path('blog_list/<int:id>/', views.BlogDetailView.as_view(), name='blog_id'),
    path('search/', views.SearchView.as_view(), name='search'),
]