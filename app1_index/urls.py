from django.urls import path
from . import views

handler404 = views.handler404
handler500 = views.handler500
handler400 = views.handler400
handler403 = views.handler403

urlpatterns = [
    path('home/', views.index, name="homee"),
    path('resume/', views.resm, name="resumee"),
    path('blog/', views.blog, name="blogg"),
    path('contact/', views.contact, name="contactt"),
    path('portfolio/', views.portfolio, name="portfolioo")
]
