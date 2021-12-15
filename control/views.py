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