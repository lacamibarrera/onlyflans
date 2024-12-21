from django import forms
from .models import ContactFormModelForm, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']  # Puedes incluir otros campos si es necesario



class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactFormModelForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo Electrónico',
            'customer_name': 'Nombre',
            'message': 'Mensaje',
        }



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating'] 