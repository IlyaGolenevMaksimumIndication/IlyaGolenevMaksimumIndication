from django.forms import ModelForm
from .models import Advertisement
from django.core.exceptions import ValidationError


class AdvertisementForm(ModelForm):
     class Meta:
         model = Advertisement
         fields = ['description', 'price', 'auction', 'image', 'title']

def clean_title(self):
     title = self.cleaned_data["title"]
     if title.startswith("?"):
          raise ValidationError(" Заголовок не может начинаться с вопросительного знака и форма не проходит валидацию.")
     return title
     
          
   