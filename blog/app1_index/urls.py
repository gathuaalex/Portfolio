from django.urls import  path
from . import views

urlpatterns=[
    path('home/',views.index,name="homee"),
    path('resume/',views.resm,name="resumee"),
    path('blog/', views.blog, name="blogg"),
    path('contact/',views.contact, name="contactt"),
    path('portfolio/',views.portfolio,name="portfolioo")
]
