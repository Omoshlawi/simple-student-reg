import os

from django.shortcuts import render

from core.forms import StudentRegForm
from core.models import Students
from django.conf import settings
from django.core.files import File
import shutil


# Create your views here.


def get_tt(value):
    return "/".join(f"NITA-{value}".split("-"))


def register(request):
    form = None
    student = None
    path = settings.UNVERIFIED_IMAGES_PATH
    path_v = settings.VERIFIED_IMAGES_PATH
    tt_no = request.GET.get('tt', '')
    try:
        student = Students.objects.get(tt_number=get_tt(tt_no))
        form = StudentRegForm(instance=student, initial={'verify_image': bool(student.photo_link)})
    except Students.DoesNotExist:
        form = StudentRegForm(initial={'tt_number': get_tt(tt_no)})
    if request.method == 'POST':
        form = StudentRegForm(data=request.POST, instance=student)
        if form.is_valid():
            cd = form.cleaned_data
            verify_image = cd.get('verify_image')
            try:
                student = Students.objects.get(
                    tt_number=get_tt(tt_no)
                )
                if verify_image:
                    student.photo_link = "verified"
                    student.save()
                    image = path / f"{tt_no}.jpg"
                    try:
                        shutil.move(image, path_v / f"{tt_no}.jpg")
                    except FileNotFoundError:
                        print("File not found")
                else:
                    student.photo_link = ""
                    student.save()
                    image = path / f"{tt_no}.jpg"
                    try:
                        shutil.move(path_v / f"{tt_no}.jpg", image)
                    except FileNotFoundError:
                        print("File not found")

                student = Students.objects.get(
                    tt_number=get_tt(tt_no)
                )
                form = StudentRegForm(instance=student)
            except Students.DoesNotExist:
                pass
    return render(
        request, 'register.html',
        {
            'form': form, 'student': student, 'path': {'verified': path_v, 'unverified': path},
            'search': tt_no,
            "fields": [str(field.name).upper().replace("_", " ") for field in Students._meta.fields]
        }
    )
