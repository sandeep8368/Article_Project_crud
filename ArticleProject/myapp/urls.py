from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.display_index, name='home'),
    path('allarticle/', views.display_articles, name='allart'),
    path('specarticle/<int:id>', views.spec_article, name = 'specific'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('update/<int:id>', views.update_view, name = 'update'),
]