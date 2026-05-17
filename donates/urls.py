from django.urls import path
from . import views


urlpatterns = [
    path('donate_list/', views.DonateListView.as_view(), name='dt_list'),
    path('donate_list/<int:id>/delete/', views.DeleteDonateView.as_view(), name='del_list'),
    path('donate_list/<int:id>/update/', views.UpdateDonateView.as_view(), name='edit_list'),
    path('create_donate/', views.CreateDonateView.as_view(), name='cr_donate'),
]