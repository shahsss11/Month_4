from django.urls import path
from . import views


urlpatterns = [
    path('donate_list/', views.donate_list_view, name='dt_list'),
    path('donate_list/<int:id>/delete/', views.delete_donate_view, name='del_list'),
    path('donate_list/<int:id>/update/', views.update_donate_view, name='edit_list'),
    path('create_donate/', views.create_donate_view, name='cr_donate'),
]