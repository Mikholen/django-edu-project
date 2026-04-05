from django import forms

class AnswerForm(forms.Form):
    user_answer = forms.FloatField(
        label="Ваш ответ",
        required=True,
        error_messages={
            'invalid': "Ошибка: введите число (например, 1.24 или 14)",
            'required': "Поле не может быть пустым!"
        }
    )