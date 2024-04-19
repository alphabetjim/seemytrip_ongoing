from django.urls import path
from . import views

urlpatterns = [
    path('', views.TripCommentList, name='tripcommentlist'),
    # path('edit_tripcomment/<int:pk>', views.comment_edit, name='edit_tripcomment'),
    # path('delete_tripcomment/<int:comment_id>', views.comment_delete, name='delete_tripcomment'),
]