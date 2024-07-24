from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ShowContentView.as_view(), name='home-page'),
    path('item/<int:pk>', views.ContentDetailView.as_view(), name='content-detail'),
    path('item/<int:pk>/delete', views.DeleteContentView.as_view(), name='content-delete'),
    path('item/<int:pk>/update', views.UpdateContentView.as_view(), name='content-update'),
    path('item/add', views.CreateContentView.as_view(), name='content-add'),
    path('about/', views.about, name='about-page'),
		path('ar/', views.ar, name='ar'),
]