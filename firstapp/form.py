from django import forms
from django.core.exceptions import ValidationError

#一个并没有什么卵用的字数判定器
def words_validator(comment):
    if len(comment)<1:
        raise ValidationError('Not Enough words')

#一个并没有什么卵用的和谐文字判定器
def comment_validator(comment):
    if "fuck" in comment:
        raise ValidationError('Be Nice.')

#评论表单
class commentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(),
        validators=[words_validator,comment_validator]
    )
#文章发布表单
class articleForm(forms.Form):
    title = forms.CharField(max_length=500)
    CHOICE_SET=(
        ('life','Life'),
        ('tech','Tech')
    )
    tag = forms.ChoiceField(choices=CHOICE_SET)
    content = forms.CharField(widget=forms.Textarea())
