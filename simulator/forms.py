"""Form description module for user data entry."""
from django import forms

class AnswerForm(forms.Form):
    """A form for receiving a numerical answer to a physical problem."""
    user_answer = forms.FloatField(
        label="Ваш ответ",
        required=True,
        error_messages={
            'invalid': "Ошибка: введите число (например, 1.24 или 14)",
            'required': "Поле не может быть пустым!"
        }
    )
