from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import Ricette, Preferiti, Categoria
from .forms import RicettaForm




def homePageView(request):
    categorie = Categoria.objects.all()
    contesto = {'categorie': categorie}
    return render(request, 'ricette/home.html', contesto)

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
             form.add_error(None, "Invalid username or password")

    else:
        form = AuthenticationForm()

    return render(request, 'ricette/login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'ricette/register.html', {'form': form})



def ricette(request, id_ricetta):
    ricetta = Ricette.objects.get(id=id_ricetta)
    return render(request, 'ricette/ricette.html', {'ricetta': ricetta})

@login_required(login_url='/login/')
def crea_ricetta(request):
    if request.method == 'POST':
        form = RicettaForm(request.POST)
        if form.is_valid():
            ricetta = form.save(commit=False)
            ricetta.save()
            return redirect('home')  # Redirigi l'utente alla home dopo aver creato la ricetta
    else:
        form = RicettaForm()
    return render(request, 'ricette/crea_ricetta.html', {'form': form})

def lista_ricette(request):
    ricette = Ricette.objects.all()
    categoria=request.GET.get('categoria')
    if categoria:
        ricette=ricette.filter(categoria__nome=categoria)
    contesto = {'ricette': ricette,
                'categorie': Categoria.objects.all(),
                'categoria_selezionata': categoria if categoria else 'Tutte le ricette'}
    return render(request, 'ricette/lista_ricette.html', contesto)

@login_required(login_url='/login/')
def preferiti(request):
    preferiti = Preferiti.objects.get(user=request.user)
    return render(request, 'ricette/preferiti.html', {'preferiti': preferiti})

@login_required(login_url='/login/')
def aggiungi_preferiti(request, id_ricetta):
    if request.method == 'POST':
        ricetta = Ricette.objects.get(id=id_ricetta)
        preferiti, crea_ricetta = Preferiti.objects.get_or_create(user=request.user)
        preferiti.lista.add(ricetta)
        preferiti.save()
        return redirect('preferiti')
    else:
        return redirect('home')

@login_required(login_url='/login/')
def rimuovi_preferiti(request, id_ricetta):
    if request.method == 'POST':
        ricetta = Ricette.objects.get(id=id_ricetta)
        preferiti = Preferiti.objects.get(user=request.user)
        preferiti.lista.remove(ricetta)
        return redirect('preferiti')
    else:
        return redirect('home')


def idee_ricette(request):
    return render(request, 'ricette/idee_ricette.html')

def antipasti(request):
    return render(request, 'ricette/antipasti.html')

def primi(request):
    return render(request, 'ricette/primi.html')

def secondi(request):
    return render(request, 'ricette/secondi.html')

def dolci(request):
    return render(request, 'ricette/dolce.html')

def contorni(request):
    return render(request, 'ricette/contorni.html')

def intolleranti(request):
    return render(request, 'ricette/intolleranti.html')



