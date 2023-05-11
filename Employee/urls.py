from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('edit', views.edit, name='edit'),
    path('update/<int:id>', views.edit, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]