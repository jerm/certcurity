from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import FormView
from .forms import ContactForm, FilesForm, ContactFormSet
from django.conf import settings


# Create your views here.
def index(request):
    context = {"PROJECT_NAME": settings.PROJECT_NAME}
    return render(request, 'webapp/index.html', context)

class FormWithFilesView(FormView):
    template_name = 'demo/form_with_files.html'
    form_class = FilesForm
