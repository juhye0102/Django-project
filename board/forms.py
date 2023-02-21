from django.forms import ModelForm
from .models import Post
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm): 
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        widgets = {
            'title': ModelForm.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력하세요.',
                                                'style': 'max-width: 70%; border: none;'}),
            'content': ModelForm.TextInput(attrs={'class': 'form-control', 'placeholder': '내용을 입력하세요.'}),
            'author': ModelForm.TextInput(attrs={'class': 'form-control', 'placeholder': '작성자 이름을 입력하세요.'}),
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
