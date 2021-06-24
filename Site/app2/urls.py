from django.urls import path
from . import views_forum, views_streaming


urlpatterns = [
    path('episodes/<str:page>', views_streaming.epList, name="liste des épisode de OP"),
    path('stream/<str:ep>', views_streaming.stream, name="page de streaming des épisodes de OP"),

    path('addInForum/', views_forum.addInForum, name='addInForum'),
    path('addInDiscussion/', views_forum.addInDiscussion, name='addInDiscussion'),
    path('forum/', views_forum.forum, name='forum'),

]