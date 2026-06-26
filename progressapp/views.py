from django.shortcuts import render, redirect, get_object_or_404
from .models import Progress
from .forms import ProgressForm
from tenderapp.models import Tender
from django.shortcuts import render
from .models import Progress


def update_progress(request, id):

    tender = get_object_or_404(
        Tender,
        id=id
    )

    updates = Progress.objects.filter(
        tender=tender
    ).order_by('-created_at')

    if request.method == 'POST':

        form = ProgressForm(request.POST)

        if form.is_valid():

            progress = form.save(commit=False)

            progress.builder = request.user

            progress.tender = tender

            progress.save()

            return redirect(
                f'/update-progress/{id}/'
            )

    else:

        form = ProgressForm()

    return render(
        request,
        'update_progress.html',
        {
            'form': form,
            'updates': updates
        }
    )


def project_progress(request, id):

    progress_list = Progress.objects.filter(
        tender_id=id
    ).order_by('-created_at')

    return render(
        request,
        'project_progress.html',
        {
            'progress_list': progress_list
        }
    )