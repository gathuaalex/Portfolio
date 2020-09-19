from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import MyInfo
from .forms import ContactForm
from app1_index.views import base


# Create your views here.
def hello_world(request):
    render(request, 'hello_world.html', {})


class Classname(TemplateView):
    template_name = 'hello_world.html'


def Folio_index(request):
    projects = MyInfo.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()

    context = {
        'obj': projects,
        'form': form
    }

    return render(request, 'folio_index.html', context)


def F_details(request, pk):
    projects = MyInfo.objects.get(id=pk)
    context = {'obj': projects, "b": base()}
    return render(request, 'folio_detail.html', context)


class Folioq(ListView):
    template_name = 'folio_index.html'

    def get_queryset(self):
        return MyInfo.objects.all()
