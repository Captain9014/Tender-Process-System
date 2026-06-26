from django.shortcuts import render
from bidapp.models import Bid
from progressapp.models import Progress

def assigned_projects(request):

    bids = Bid.objects.filter(
    builder=request.user,
    is_selected=True
)

    for bid in bids:

        latest_progress = Progress.objects.filter(
        tender=bid.tender
    ).order_by('-created_at').first()

    bid.latest_progress = latest_progress

    return render(
    request,
    'assigned_projects.html',
    {'bids': bids}
)

    