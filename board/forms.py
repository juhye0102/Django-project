from django.forms import ModelForm
from .models import Post
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm): 
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        labels = {
            'title': _('제목'),
            'content': _('내용'),
            'author': _('작성자'),
        }
        error_messages = {
            'title': {
                'max_length': _("제목이 너무 깁니다. 50자 이하로 작성해 주세요.")
            }
        }
