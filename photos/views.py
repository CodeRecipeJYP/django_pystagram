# coding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from photos.models import Photo
from .forms import PhotoEditForm


def single_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)

    return render(
        request,
        'photo.html',
        {
            'photo': photo,
        }
    )

def new_photo(request):
    if request.method == "GET":
        edit_form = PhotoEditForm()
    elif request.method == "POST":
        edit_form = PhotoEditForm(request.POST, request.FILES)

        if edit_form.is_valid():
            new_photo = edit_form.save()

            return redirect(new_photo.get_absolute_url())

    return render(
        request,
        'new_photo.html',
        {
            'form': edit_form,
        }
    )