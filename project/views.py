from django.shortcuts import render, redirect
from .form import TodoForm
from  .models import Diary
# Create your views here.
def home(request):
    queryset = Diary.objects.order_by("-date")

    context = {
        "list": queryset
    }
    return render(request, 'home.html', context)
def add(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        "form": form
    }
    return render(request, "add.html", context)