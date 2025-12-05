from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import gallery_view, home, dashboard, edit_item, delete_item

urlpatterns = [
    path('', home, name='home'),
    path('gallery/', gallery_view, name='gallery'),
    path('dashboard/', dashboard, name='dashboard'),
    path('item/<int:pk>/edit/', edit_item, name='edit_item'),
    path('item/<int:pk>/delete/', delete_item, name='delete_item'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
