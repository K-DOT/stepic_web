from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse 
from qa.models import Question, Answer
from django.http import Http404
# Create your views here.

def index(request):
    objects = Question.objects.order_by('-added_at')
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    try:                                                                        
        page = int(request.GET.get('page', 1))                               
    except ValueError:                                                          
        return Http404
    paginator = Paginator(objects, limit)
    pages = paginator.page(page)
    return render(request, 'index.html', {
        'paginator' : paginator,
        'pages' : pages 
    })
    

def popular(request):
    pass

def question(request, id):
    pass

def test(request, *args, **kwargs):
    return HttpResponse('OK')
