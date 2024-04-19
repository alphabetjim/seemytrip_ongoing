from django.shortcuts import render
from django.views import generic
from .models import TripComment

# Create your views here.
def TripCommentList(request):
    """
    Display all TripComments as a list
    """ 
    queryset = TripComment.objects.all()
    template_name = "comment/commentlist.html"
    
    return render(
        request,
        template_name,
        {
            'queryset': queryset,
        }
    )
