from django.shortcuts import render, redirect, get_object_or_404
from .forms import FileUploadForm
from .models import ProjectFile
from tenderapp.models import Tender


def upload_file(request, id):

    tender = get_object_or_404(
        Tender,
        id=id
    )

    files = ProjectFile.objects.filter(
        tender=tender
    )

    if request.method == 'POST':

        form = FileUploadForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            uploaded_file = form.save(commit=False)

            uploaded_file.tender = tender

            uploaded_file.uploaded_by = request.user

            uploaded_file.save()

            return redirect(
                f'/upload-file/{id}/'
            )

    else:

        form = FileUploadForm()

    return render(
        request,
        'upload_file.html',
        {
            'form': form,
            'files': files
        }
    )


def project_files(request, id):

    files = ProjectFile.objects.filter(
        tender_id=id
    ).order_by('-uploaded_at')

    return render(
        request,
        'project_files.html',
        {
            'files': files
        }
    )