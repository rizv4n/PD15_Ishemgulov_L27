from django.contrib import admin
from django.urls import path

from ads import views
from ads.views import ADSView, ADSDetailView
from categories.views import CategoryView, CategoryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('cat/', CategoryView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('ad/', ADSView.as_view()),
    path('ad/<int:pk>/', ADSDetailView.as_view())
]
