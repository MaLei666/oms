from django import forms

######################################
# 添加平台表单
######################################
class AddPlatformForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)
    url=forms.CharField(min_length=2, max_length=50, required=True)

######################################
# 添加平台表单
######################################
class EditPlatformForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=20, required=True)
    url=forms.CharField(min_length=2, max_length=50, required=True)