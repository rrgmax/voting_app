from django.shortcuts import render

# Create your views here.
from. models import Question

def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'votings/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
