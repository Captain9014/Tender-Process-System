from django.shortcuts import render,redirect,get_object_or_404
from .models import Message
from .forms import MessageForm
from tenderapp.models import Tender
from accounts.models import UserBlock


def chat_room(request,id):

    tender = get_object_or_404(
        Tender,
        id=id
    )
    is_blocked = UserBlock.objects.filter(
    blocked_by=tender.client,
    blocked_user=request.user
    ).exists()

    if is_blocked:
     return redirect('/')

    messages = Message.objects.filter(
        tender=tender
    )

    if request.method == 'POST':

        form = MessageForm(request.POST)

        if form.is_valid():

            message = form.save(commit=False)

            message.sender = request.user

            message.tender = tender

            message.save()

            return redirect(
                f'/chat-room/{id}/'
            )

    else:

        form = MessageForm()

    return render(
        request,
        'chat_room.html',
        {
            'messages': messages,
            'form': form
        }
    )

def delete_message(request, id):

    message = get_object_or_404(
        Message,
        id=id
    )

    tender_id = message.tender.id

    if message.sender == request.user:

        message.delete()

    return redirect(
        f'/chat-room/{tender_id}/'
    )


def edit_message(request, id):

    message = get_object_or_404(
        Message,
        id=id
    )

    if message.sender != request.user:

        return redirect(
            f'/chat-room/{message.tender.id}/'
        )

    if request.method == 'POST':

        form = MessageForm(
            request.POST,
            instance=message
        )

        if form.is_valid():

            form.save()

            return redirect(
                f'/chat-room/{message.tender.id}/'
            )

    else:

        form = MessageForm(
            instance=message
        )

    return render(
        request,
        'edit_message.html',
        {'form': form}
    )