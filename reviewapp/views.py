from django.shortcuts import render,redirect,get_object_or_404
from .forms import ReviewForm
from .models import Review
from bidapp.models import Bid


def give_review(request,id):

    bid = get_object_or_404(
        Bid,
        id=id
    )

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.client = request.user

            review.builder = bid.builder

            review.tender = bid.tender

            review.save()

            return redirect('/my-tenders/')

    else:

        form = ReviewForm()

    return render(
        request,
        'give_review.html',
        {'form':form}
    )