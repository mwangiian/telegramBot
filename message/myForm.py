from django.forms import ModelForm
from .models import Message

# Create the form class.
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
