from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hey Client, my app is running")

def event_listing(request):
    html = '''
    <ul>
        <li>Chill on the beach <a href="/event/Chill">detail</a></li>
        <li>Camping in the woods <a href="/event/Camping">detail</a></li>
        <li>Flying into the space <a href="/event/Flying">detail</a></li>
    </ul>
    '''

    return HttpResponse(html)

def event_detail(request, name):
    data = {'Chill' : '<h2>Chill on the beach just for $400</h2>',
            'Camping': '<h2>Camp with us for $50</h2>',
            'Flying': '<h2>Fly for free</h2>'}

    selection = data.get(name)

    if selection:
        return HttpResponse(selection)
    else:
        return HttpResponse('No such event in offering for now')