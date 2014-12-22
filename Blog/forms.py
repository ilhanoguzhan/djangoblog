from django import forms


from Blog.models import TOPIC

class TOPICForm(forms.ModelForm):
    class Meta:
        model = TOPIC
