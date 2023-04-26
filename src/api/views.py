from django.http import HttpResponse
from workshop.models import Card, Workshop


# Create your views here.
def status(request):
    return HttpResponse("up.")

#@login_required
def getnetwork(request, workshop_id):
    workshop = Workshop.objects.get(pk=workshop_id)
    cardsinworkshop = Card.objects.filter(workshop=workshop)
    networkdata = []
    for card in cardsinworkshop:
        parent = Card.objects.get(pk=card.parentnode)
        networkdata.append([card.title, parent.title])
    return HttpResponse(networkdata)

