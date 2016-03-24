from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question 

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField() 

    def clean_question(self):
        question = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question)
        except Question.DoesNotExist:
            raise forms.ValidationError('Invalid question ID!')

    def save(self):
        question = Question.objects.get(id=self.cleaned_data['question'])
        answer = Answer(text=self.cleaned_data['text'], question=question)
        answer.save()
        return answer
