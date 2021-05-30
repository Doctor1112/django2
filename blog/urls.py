from django.urls import path
from . import views
urlpatterns = [
    path('',views.showblog, name='showblog' ),
    path('<int:post_id>/', views.spec_post, name='spec_post')
]