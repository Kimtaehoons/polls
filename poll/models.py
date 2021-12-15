from django.db import models
#설문 투표 앱에 사용할 Question모델(설명 : 질문내용, 출판일), models안에 Model클래스(부모 상속) 생성(Model을 상속 받음), table과 같음
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    
    def __str__(self): #질문 내용이 문자로 출력됨
        return self.question_text

#Choice모델(답변)
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #외래키

    def __str__(self):
        return self.choice_text

#설문 투표 앱에 사용할 Choice모델(내용 : 답변내용, 투표수 등)