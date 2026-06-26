
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from .forms import RegisterForm, ProfileForm
from .models import User, BlockBuilder, UserBlock

from tenderapp.models import Tender
from bidapp.models import Bid
from notificationapp.models import Notification
from reviewapp.models import Review
from progressapp.models import Progress


# ================= REGISTER =================

def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            return redirect('login')

    else:
        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )


# ================= LOGIN =================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == 'client':
                return redirect('/client-dashboard/')

            elif user.role == 'builder':
                return redirect('/builder-dashboard/')

        else:

            return render(
                request,
                'login.html',
                {'error': 'Invalid Credentials'}
            )

    return render(request, 'login.html')


# ================= CLIENT DASHBOARD =================

@login_required
def client_dashboard(request):

    total_tenders = Tender.objects.filter(
        client=request.user
    ).count()

    active_projects = Tender.objects.filter(
        client=request.user,
        status='assigned'
    ).count()

    total_builders = Bid.objects.values(
        'builder'
    ).distinct().count()

    notifications = Notification.objects.filter(
        user=request.user
    ).count()

    recent_tenders = Tender.objects.filter(
        client=request.user
    ).order_by('-id')[:5]

    context = {

        'total_tenders': total_tenders,
        'active_projects': active_projects,
        'total_builders': total_builders,
        'notifications': notifications,
        'recent_tenders': recent_tenders,

    }

    return render(
        request,
        'client_dashboard.html',
        context
    )


# ================= BUILDER DASHBOARD =================

@login_required
def builder_dashboard(request):

    assigned_projects = Bid.objects.filter(
        builder=request.user,
        is_selected=True
    )

    assigned_count = assigned_projects.count()

    active_bid_count = Bid.objects.filter(
        builder=request.user
    ).count()

    notification_count = Notification.objects.filter(
        user=request.user
    ).count()

    latest_tenders = Tender.objects.filter(
        status='open'
    ).order_by('-id')[:5]

    recent_notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-id')[:5]

    completed_projects = Progress.objects.filter(
        builder=request.user,
        progress=100
    ).count()

    context = {

        'assigned_projects': assigned_projects,
        'assigned_count': assigned_count,
        'active_bid_count': active_bid_count,
        'notification_count': notification_count,
        'latest_tenders': latest_tenders,
        'recent_notifications': recent_notifications,
        'completed_projects': completed_projects,

    }

    return render(
        request,
        'builder_dashboard.html',
        context
    )


# ================= LOGOUT =================

def logout_view(request):

    logout(request)

    return redirect('/login/')


# ================= PROFILE =================

@login_required
def profile(request, id):

    user = get_object_or_404(
        User,
        id=id
    )

    reviews = Review.objects.filter(
        builder=user
    ).order_by('-created_at')

    avg_rating = reviews.aggregate(
        Avg('rating')
    )['rating__avg']

    is_blocked = UserBlock.objects.filter(
        blocked_by=request.user,
        blocked_user=user
    ).exists()

    return render(
        request,
        'profile.html',
        {
            'user_profile': user,
            'reviews': reviews,
            'avg_rating': avg_rating,
            'is_blocked': is_blocked
        }
    )


# ================= EDIT PROFILE =================

@login_required
def edit_profile(request):

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            return redirect(
                f'/profile/{request.user.id}/'
            )

    else:

        form = ProfileForm(
            instance=request.user
        )

    return render(
        request,
        'edit_profile.html',
        {'form': form}
    )


# ================= BLOCK BUILDER =================

@login_required
def block_builder(request, id):

    builder = get_object_or_404(
        User,
        id=id
    )

    BlockBuilder.objects.get_or_create(
        client=request.user,
        builder=builder
    )

    return redirect('/my-tenders/')


# ================= BLOCK USER =================

@login_required
def block_user(request, id):

    user_to_block = get_object_or_404(
        User,
        id=id
    )

    UserBlock.objects.get_or_create(
        blocked_by=request.user,
        blocked_user=user_to_block
    )

    return redirect(
        f'/profile/{user_to_block.id}/'
    )


# ================= UNBLOCK USER =================

@login_required
def unblock_user(request, id):

    blocked_user = get_object_or_404(
        User,
        id=id
    )

    UserBlock.objects.filter(
        blocked_by=request.user,
        blocked_user=blocked_user
    ).delete()

    return redirect(
        f'/profile/{blocked_user.id}/'
    )
