from .models import Forum
from .forms import CreateInForum, CreateInDiscussion

from django.shortcuts import render, redirect


def forum(request):
    forums = Forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'app2/forum.html', context)


def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum')
    context = {
        'form': form
    }
    return render(request, 'app2/addInForum.html', context)


def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum')
    context = {
        'form': form
    }
    return render(request, 'app2/addInDiscussion.html', context)
