from django.shortcuts import render, redirect
from .forms import TenderForm

def create_tender(request):

    if request.method == 'POST':

        form = TenderForm(request.POST)

        if form.is_valid():

            tender = form.save(commit=False)

            tender.client = request.user

            tender.save()

            return redirect('/client-dashboard/')

    else:

        form = TenderForm()

    return render(
        request,
        'create_tender.html',
        {'form': form}
    )