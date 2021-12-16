from django.shortcuts import render
#index
def index(request):
    return render(request, 'control/index.html') #제어 함수로 url받아서

#회원 가입
def register(request):
    if request.method == "POST": #POST방식(아이디를 입력 후 전송 버튼을 눌렀을 때)
        userid = request.POST['userid'] #ID를 request.POST로 받아서
        return render(request, 'control/reg_result.html', {'userid':userid}) #html을 렌더링 할 때 딕셔너리 구조로 ID를 통해 받은 것을 결과페이지로 보내줌
    else: #GET방식(회원 가입 창이 뜨는 것)
        return render(request, 'control/register.html') #control의 url받아서

#반복문 forloop.counter
def counter(request):
    items = ['a', 'b', 'c', 'd']
    return render(request, 'control/counter.html', {'items':items}) #'items'라는 key값으로 자료를 받아준다

#짝수/홀수 판별하기
def calc_even_odd(request):
    if request.method == "POST":
        try: #문자가 입력될 경우 오류 처리(try~except~else)
            num = int(request.POST['num']) #num(입력값)을 받고 아래 계산이 필요하므로 웹은 숫자를 문자형으로 넘겨받기에 숫자형으로 변환
        except:
            return render(request, 'control/calc_even_odd.html', #다시 폼화면으로 보내는데
                          {'error':'정수만 입력가능합니다'})
        else:
            if num % 2 == 0: #num(입력값) 판정
                result = "짝수입니다"
            else:
                result = "홀수입니다"
            return render(request, 'control/calc_result.html', {'num':num, 'result':result}) #결과페이지에 딕셔너리로 보내주고 html을 만들어서 받은 num이 잘 넘어가는지 확인
    else:
        return render(request, 'control/calc_even_odd.html')