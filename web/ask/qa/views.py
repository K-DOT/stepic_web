from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from qa.models import Question, Answer
from django.http import Http404
from qa.forms import AskForm, AnswerForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.views.decorators.http import require_POST

def pagination(request, qs):
    try:                                                                        
        limit = int(request.GET.get('limit', 10))                               
    except ValueError:                                                          
        limit = 10                                                              
    try:                                                                        
        page = int(request.GET.get('page', 1))                                  
    except ValueError:                                                          
        return Http404                                                          
    paginator = Paginator(qs, limit)                                       
    return paginator.page(page)
    

def index(request):
    objects = Question.objects.order_by('-added_at')
    questions = pagination(request, objects)
    return render(request, 'questions.html', {
        'questions' : questions
    })
    

def popular(request):
    objects = Question.objects.order_by('-rating')
    return render(request, 'questions.html', {                     
        'questions' : pagination(request, objects)                                                 
    })

def question(request, id):
    question = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question=question)
    form = AnswerForm()
    return render(request, 'question.html', {
        'question' : question,
        'answers' : answers,
        'form' : form 
    })

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()     
            return HttpResponseRedirect(reverse('question', args=[question.id,]))
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form' : form
    })

@require_POST
def answer(request):
    if request.method == 'POST':
        form = AnswerForm()
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect(reverse('question', args=[answer.question,]))
        else:
            return render(request, 'answer.html', {
                'form' : form,
            })

def test(request, *args, **kwargs):
    return HttpResponse('OK')
