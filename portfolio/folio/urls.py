from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import  views
from .views import *
urlpatterns=[
    path('class/', Classname.as_view(), name='hello'),
    path('cli/',views.Folio_index,name="project_index"),
    path('<int:pk>', views.F_details, name="project_det"),
    
]
