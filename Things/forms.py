from django import forms

class ThingForm(forms.Form):
    #     x = forms.CharField(label='x', max_length=100)
    thing_id = forms.IntegerField(label='Thing id')
    user_id = forms.IntegerField(label='User id')
    enName = forms.CharField(label='EnName')
    color_id = forms.IntegerField(label='Color id')
    shape_id = forms.IntegerField(label='Shape id')
    description = forms.CharField(label='Description', max_length=100)

class ThingColorForm(forms.Form):
    color_id = forms.IntegerField(label='Color Id')
    enName = forms.CharField(label='EnName')
    description = forms.CharField(label='Description', max_length=100)

class NameForm(forms.Form):
    name_id = forms.CharField(label='Id', required=False)
    myName = forms.CharField(label='MyName')
    cleaned_data = {'name_id': None, 'myName': ''}
    
    def is_valid(self):
    #    self.cleaned_data = self.cleaned_data
        return True
