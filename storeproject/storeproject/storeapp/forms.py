from django import forms

# COURSE_CHOICES = [
#     ('commerce', 'Commerce'),
#     ('science', 'Science'),
#     ('humanities','Humanities'),
# ]
#
# SUB_COURSE_CHOICES = {
#     'commerce': [('bba', 'BBA'), ('bcom', 'BCom')],
#     'science': [('computer', 'Computer'), ('biology', 'Biology')],
#     'humanities':[('ba','BA'),('ma','MA')]

class newform(forms.Form):
    name = forms.CharField(label='Name')
    dob = forms.DateField(label='DOB')
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female')])
    phone_number = forms.CharField(label='Phone number')
    email = forms.EmailField(label='Email ID')
    address = forms.CharField(label='Address')
    courses = forms.ChoiceField(label='Courses', choices=[('commerce', 'Commerce'), ('science', 'Science'),('humanities','Humanities')])
    sub_courses = forms.ChoiceField(label='Sub Courses', choices=[('bba','BBA'),('mba','MBA'),('computer','Computer'),])
    purpose = forms.ChoiceField(label='Purpose', choices=[('enquiry', 'Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
    materials = forms.MultipleChoiceField(label='Materials Provide', choices=[('notebook', 'Debit Note Book'), ('pen', 'Pen'), ('exam', 'Exam Papers')], widget=forms.CheckboxSelectMultiple)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)