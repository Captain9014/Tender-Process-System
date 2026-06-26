from django.shortcuts import render, redirect, get_object_or_404
from .forms import BidForm
from .models import Bid
from tenderapp.models import Tender
from notificationapp.models import Notification
from accounts.models import UserBlock


def submit_bid(request, id):

    tender = get_object_or_404(
        Tender,
        id=id
    )

    is_blocked = UserBlock.objects.filter(
        blocked_by=tender.client,
        blocked_user=request.user
    ).exists()

    if is_blocked:
        return redirect('/available-tenders/')

    if request.method == 'POST':

        form = BidForm(request.POST)

        if form.is_valid():

            bid = form.save(commit=False)
            bid.builder = request.user
            bid.tender = tender
            bid.save()

            Notification.objects.create(
                user=tender.client,
                message=f'New bid received for {tender.title}'
            )

            Notification.objects.create(
                user=request.user,
                message=f'You submitted a bid for {tender.title}'
            )

            return redirect('/available-tenders/')

    else:
        form = BidForm()

    return render(
        request,
        'submit_bid.html',
        {'form': form}
    )