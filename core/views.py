from django.shortcuts import render

from core.forms import StudentRegForm
from core.models import Students
from django.conf import settings
from django.core.files import File

# Create your views here.


def register(request):
    form = None
    student = None
    tt_no = None
    path = settings.UNVERIFIED_IMAGES_PATH
    if request.method == 'GET':
        try:
            tt_no = request.GET.get('tt', '')
            student = Students.objects.get(tt_number=tt_no)
            form = StudentRegForm(instance=student)
        except Students.DoesNotExist:
            form = StudentRegForm(initial={'tt_number': tt_no})
    else:
        form = StudentRegForm(data=request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            tt = cd["tt_number"]
            score = cd['score']
            student = Students(
                tt_number=tt,
                score=score,
                results="Pass" if score > 70.0 else "Fail",
                verified="verified"
            )

            # Assuming 'path' is the file path to be uploaded
            with open(path / f"{tt}.jpg", 'rb') as file:
                student.image.save(f"{tt}.jpg", File(file))

            student.save()
    return render(request, 'register.html',
                  {'form': form, 'student': student, 'path': path, 'search': tt_no})
