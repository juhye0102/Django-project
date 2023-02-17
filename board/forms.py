from django.forms import ModelForm
from .models import Post
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm): 
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        widgets = {
            'title': ModelForm.TextInput(attrs={'class': 'form_title', 'placeholder': '제목을 입력하세요.'}),
            'content': ModelForm.TextInput(attrs={'class': 'form_content'}),
            'author': ModelForm.TextInput(attrs={'class': 'form_author'}),
        }
        # labels = {
        #     'title': _('제목'),
        #     'content': _('내용'),
        #     'author': _('작성자'),
        # }
        error_messages = {
            'title': {
                'max_length': _("50자 이하로 작성해 주세요.")
            }
        }
