from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm, ContactMeForm
from .models import FormModel, ContactMeModel


def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)


def add(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("list")
    else:
        form = PostForm()
    return render(request,'forms_app/input.html', {'form': form})


def contact_me(request):
    contact = ContactMeForm(request.POST or None)
    if contact.is_valid():
        contact.save()
        return redirect("list")
    else:
        contact = ContactMeForm()
    return render(request,'forms_app/contact.html', {'contact': contact})


def edit(request, pk):
    the_model = get_object_or_404(FormModel, pk=pk)
    form = PostForm(request.POST, instance=the_model)
    if form.is_valid():
        form.save()
        return redirect("list")
    else:
        the_model = get_object_or_404(FormModel, pk=pk)
        form = PostForm(instance=the_model)
    return render(request, 'forms_app/input.html', {'form': form})


def delete(request, pk):
    the_model = get_object_or_404(FormModel, pk=pk)
    print(the_model)
    the_model.delete()
    return redirect("list")


def reflections(request):
    print('monkey')