from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home,name='home'),
    path('index/<int:id>',views.index,name='index'),
    path('questions/<int:id>',views.questions,name='questions'),
    path('quiz_delete/<int:id>',views.quiz_delete,name='quiz_delete'),
    path('quiz_edit/<int:id>',views.quiz_edit,name='quiz_edit'),
    path('que_edit/<int:id>',views.que_edit,name='que_edit'),
    path('que_delete/<int:id>',views.que_delete,name='que_delete'),
    path('mehnova_map',views.mehnova_map,name='mehnova_map')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)