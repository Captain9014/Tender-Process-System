from django.shortcuts import render, redirect
from .forms import TenderForm
from .models import Tender
from django.shortcuts import get_object_or_404
from bidapp.models import Bid
from django.shortcuts import redirect, get_object_or_404


def create_tender(request):

    if request.method == "POST":

        form = TenderForm(request.POST)

        print("POST REQUEST AAYA")

        if form.is_valid():

            print("FORM VALID")

            tender = form.save(commit=False)

            tender.client = request.user

            tender.save()

            print("TENDER SAVED")

            return redirect('/client-dashboard/')

        else:

            print(form.errors)

    else:

        form = TenderForm()

    return render(
        request,
        'create_tender.html',
        {'form': form}
    )

    if request.method == "POST":

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



def my_tenders(request):

    tenders = Tender.objects.filter(
        client=request.user
    )

    for tender in tenders:

        tender.selected_bid = Bid.objects.filter(
            tender=tender,
            is_selected=True
        ).first()

    return render(
        request,
        'my_tenders.html',
        {'tenders': tenders}
    )



def edit_tender(request, id):

    tender = get_object_or_404(
        Tender,
        id=id
    )

    if request.method == 'POST':

        form = TenderForm(
            request.POST,
            instance=tender
        )

        if form.is_valid():
            form.save()
            return redirect('/my-tenders/')

    else:

        form = TenderForm(
            instance=tender
        )

    return render(
        request,
        'edit_tender.html',
        {'form': form}
    )


def delete_tender(request,id):

    tender=get_object_or_404(
        Tender,
        id=id
    )

    tender.delete()

    return redirect('/my-tenders/')


def available_tenders(request):

    tenders = Tender.objects.all()

    search = request.GET.get('search')

    location = request.GET.get('location')

    if search:

        tenders = tenders.filter(
            title__icontains=search
        )

    if location:

        tenders = tenders.filter(
            location__icontains=location
        )

    return render(
        request,
        'available_tenders.html',
        {'tenders': tenders}
    )

def view_bids(request, id):

    bids = Bid.objects.filter(
        tender_id=id
    )

    return render(
        request,
        'view_bids.html',
        {'bids': bids}
    )

def select_builder(request, id):

    bid = get_object_or_404(
        Bid,
        id=id
    )

    bid.is_selected = True
    bid.save()

    bid.tender.status = 'assigned'
    bid.tender.save()

    return redirect(
        f'/view-bids/{bid.tender.id}/'
    )
def complete_project(request, id):

    tender = get_object_or_404(
        Tender,
        id=id
    )

    tender.status = 'completed'
    tender.save()

    selected_bid = Bid.objects.get(
        tender=tender,
        is_selected=True
    )

    return redirect(
        f'/give-review/{selected_bid.id}/'
    )

    tender = get_object_or_404(
        Tender,
        id=id
    )

    tender.status = 'completed'

    tender.save()

    return redirect('/my-tenders/')