from django.shortcuts import render, redirect, get_object_or_404
from .models import Flan, ContactFormModelForm, Review
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactFormModelForm, ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404


class CustomLoginView(LoginView):
    template_name = 'welcome.html'  
    redirect_authenticated_user = True
    success_url = reverse_lazy('bienvenido')


def index(request):
    flanes = Flan.objects.filter(is_private=False) 
    return render(request, 'index.html', {'flanes': flanes})

def acerca(request):
    return render(request, 'about.html')

@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)  
    return render(request, 'welcome.html', {'flanes': flanes_privados})


def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactFormModelForm(
                customer_email=form.cleaned_data['customer_email'],
                customer_name=form.cleaned_data['customer_name'],
                message=form.cleaned_data['message']
            )
            contact_form.save()  
            return redirect('exito')  
    else:
        form = ContactFormModelForm()

    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html', {
        'message': 'Gracias por contactarte con OnlyFlans, te responderemos en breve.'
    })

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, '¡Mensaje enviado con éxito!')
            return redirect('exito')  
    else:
        form = ContactFormModelForm()
    
    return render(request, 'contacto.html', {'form': form})



def lista_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})



def flan_reviews(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    reviews = flan.reviews.all()  
    return render(request, 'reviews.html', {'flan': flan, 'reviews': reviews})



def add_review(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.flan = flan  
            review.user = request.user  
            review.save()
            flan.save()
            return redirect('flan_reviews', slug=flan.slug)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'flan': flan})




def view_reviews(request, flan_slug):
    flan = get_object_or_404(Flan, slug=flan_slug)
    reviews = flan.reviews.all()  
    return render(request, 'reviews.html', {'flan': flan, 'reviews': reviews})

def cerrarsesion(request):
    return render(request, 'cerrarsesion.html')



def landing(request):
 
    return render(request, 'landing.html')


