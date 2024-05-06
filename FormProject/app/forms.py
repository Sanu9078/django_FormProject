from django import forms
gender=[['male','Male'],['female','Female']]
course=[['python','Python'],['java','Java'],['testing','Testing'],['morn','Morn']]
class ModelRegisterForm(forms.Form):
    Name=forms.CharField( max_length=50, required=False)
    Phone_No=forms.CharField(max_length=13, required=False)
    Email=forms.EmailField( required=False)
    Addres=forms.CharField( max_length=250, required=False, widget=forms.Textarea(attrs={'cols':20,'rows':5}))
    Gender=forms.ChoiceField(choices=gender, required=False, widget=forms.RadioSelect)
    Course=forms.MultipleChoiceField(choices=course, widget=forms.CheckboxSelectMultiple)
    Username=forms.CharField( max_length=50, required=False)
    Password=forms.CharField( max_length=50, required=False)