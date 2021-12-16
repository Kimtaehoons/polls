from django.http import HttpResponse
from django.shortcuts import render
from poll.models import Question

#index 페이지
def index(request):
    #return HttpResponse("Welcome~ 환영합니다!!")
    #db에 있는 모든 데이터 조회하기(select)
    question_list = Question.objects.all() 
    return render(request, 'poll/index.html', {'question_list' : question_list})

#상세 페이지
def detail(request, question_id):
    #해당 id(순번)로 자료 조회(select)-개별
    question = Question.objects.get(id=question_id)
    return render(request, 'poll/detail.html', {'question': question})

#투표 하기
def vote(request, question_id):
    #db에서 질문 세 개중 한 개만 가져오기
    question = Question.objects.get(id=question_id) #질문을 question에 담아서(flask에서 conn 등등 여러 줄로 했던 것을 한 줄로 처리 가능)
    #선택 자료 한 개만 넘겨 받음
    try: #선택을 안 했을 때 오류 처리
        choice_id = request.POST['choice']
        sel_choice = question.choice_set.get(id=choice_id)
    except:
        return render(request, 'poll/detail.html', {'question':question, 'error':'선택을 확인하세요'})
    else:
        sel_choice.votes = sel_choice.votes + 1
        sel_choice.save() #db에 저장
    #결과페이지에 보내기
        return render(request, 'poll/vote_result.html', {'question':question}) #가져온 질문 보내준다