from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from app1.models import Stream


def epList(request, page):
    episodes_List = []
    for e in Stream.objects.all():
        id = e.id
        link = e.link
        title = e.title
        ep = []
        ep.append(id), ep.append(link), ep.append(title)
        episodes_List.append(ep)
    if not request.user.is_authenticated:
        p = 'app2/epList'+page+'.html'
        return render(request, p, {"ep_l": episodes_List})
    else:
        p = 'app2/epList'+page+'-connected.html'
        return render(request, p, {"ep_l": episodes_List})


def stream(request, ep):
    if request.user.is_authenticated:
        if int(ep) >= 0 & int(ep) <= 64:
            if len(ep) != 2:
                id = "0"+ep
                title = Stream.objects.get(id=ep).title
                link = "https://mugiwara.xyz/op/saga-1/op-" + id + ".mp4"
                return render(request, 'app2/stream-connected.html', {"ep": ep, "link": link, "title": title})
            else :
                title = Stream.objects.get(id=ep).title
                link = "https://mugiwara.xyz/op/saga-1/op-" + ep + ".mp4"
                return render(request, 'app2/stream-connected.html', {"ep": ep, "link": link, "title" :title})
        else:
            link = ""
            return render(request, 'app2/stream-connected.html', {"ep": ep, "link": link, "title": title})
    else:
        return render(request, 'app2/stream.html')
