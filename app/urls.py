from django.urls import path
from app.views import Something,Gamedetailview
urlpatterns = [
    path('', Something.as_view(),name='something'),
    path('<slug:slug>/',Gamedetailview.as_view(),name='g_path'),
]
