from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Traveller
from .forms import TravellerForm


# Create your views here.
def homepage(request):
    """
    View to display home page
    """

    return render(
        request,
        'travellerprofile/index.html',
        {},
    )

def TravellerList(request):
    """
    Returns all Traveller profiles in :model:`travellerprofile:Traveller`
    and displays them in a page.
    **Context**

    ``queryset``
        All published instances of :model:`travellerprofile:Traveller`

    **Template:**

    :template:`travellerprofile/index.html`
    """
    queryset = Traveller.objects.all()
    for traveller in queryset:
        print(traveller.user.username)
        print(traveller.trips_planned.count)
    template_name = "travellerprofile/travellerlist.html"
    return render(
        request,
        template_name,
        {
            'queryset': queryset,
        },
    )

def view_profile(request):
    """
    Display individual :model: travellerprofile.Traveller of 
    logged-in user

    **Context**
    ``traveller``
        An instance of travellerprofile.Traveller

    **Template**
    :template: ``travellerprofile/view_traveller.html``
    """
    queryset = Traveller.objects.all()
    # Try to get Traveller instance associated with user
    try:
        traveller = get_object_or_404(queryset, user=request.user)
    except:
        # redirect if none exists
        return HttpResponseRedirect('../create_traveller')
    else:    
        # Render profile
        own_profile = True
        return render(
            request,
            "travellerprofile/view_profile.html",
            {
                "traveller": traveller,
                'own_profile': own_profile,
            },
        )

def traveller_profile(request, pk):
    """
    Display profile of an individual traveller
    """
    queryset = Traveller.objects.all()
    # get specified traveller
    traveller = get_object_or_404(queryset, pk=pk)
    # redirect to view_own_profile if viewing own
    if traveller.user == request.user:
        return HttpResponseRedirect(reverse(view_profile))
    own_profile = False
    return render(
        request,
        'travellerprofile/view_profile.html',
        {
            'traveller': traveller,
            'own_profile': own_profile,
        }
    )

def create_traveller(request):
    """
    Display form to allow user creation of a .models:Traveller instance
    """
    context = {}
    if request.method == "POST":
        form = TravellerForm(request.POST, request.FILES)
        if form.is_valid():
            traveller = form.save(commit=False)
            traveller.user = request.user
            traveller.save()
            messages.add_message(request, messages.SUCCESS, 'Profile Created!')
            return HttpResponseRedirect(reverse(view_profile))
    else:
        form = TravellerForm()
    context['form'] = form
    return render(
        request,
        "travellerprofile/create_traveller.html",
        context,)

def edit_traveller(request):
    """
    Display form to allow traveller to edit their profile
    """
    traveller = get_object_or_404(Traveller, user=request.user)
    
    if request.method == "POST":
        form = TravellerForm(request.POST, request.FILES, instance=traveller)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile Updated!')
            return HttpResponseRedirect(reverse(view_profile))
        else:
            messages.add_message(request, messages.ERROR,
                'Error updating profile.')
    else:
        form = TravellerForm(instance=traveller)
    return render(
        request,
        "travellerprofile/edit_traveller.html",
        {
            "traveller": traveller,
            "form": form,
        },
    )

def delete_traveller(request):
    """
    View to allow traveller profile deletion
    """
    traveller = get_object_or_404(Traveller, user=request.user)
    traveller.delete()
    messages.add_message(request, messages.SUCCESS, 'Profile deleted!')

    return HttpResponseRedirect(reverse(homepage))

# custom 404 view
def custom_404(request, exception):
    return render(
        request,
        'travellerprofile/error404.html',
        status=404
    )

# custom 404 view
def custom_500(request):
    return render(
        request,
        'travellerprofile/error404.html',
        status=500
    )
