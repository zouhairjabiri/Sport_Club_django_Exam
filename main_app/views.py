from django.http import HttpResponseRedirect
from django.shortcuts import render

from main_app.models import Adherent, Sport, Inscription
from .forms import AdherentForm
# Create your views here.


def index(request):
    return render(request, 'main_app/index.html')


def inscription(request):
    if request.method == "POST":
        form = AdherentForm(request.POST)
        if form.is_valid():
            print('FORM is valid')#Ca march :)
            adherent = Adherent()
            adherent.username = form.cleaned_data['username']
            adherent.password = form.cleaned_data['password']
            adherent.Email = form.cleaned_data['Email']
            adherent.nom = form.cleaned_data['nom']
            adherent.prenom = form.cleaned_data['prenom']
            adherent.adresse = form.cleaned_data['adresse']
            adherent.genre = form.cleaned_data['genre']
            adherent.tel = form.cleaned_data['tel']
            sports = request.POST.getlist('sport')
            request.session['adherent'] = form.cleaned_data
            request.session['sports'] = sports
            print(sports)
            return render(request, 'main_app/confirmer.html', {'adherent': adherent, 'sports': sports})
    else:
        form = AdherentForm()
        sports = Sport.objects.all()
        return render(request, 'main_app/Formulaire.html', {'form': form, 'sports': sports})
    return HttpResponseRedirect('/')


def confirmation(request):
    data = request.session.get('adherent')
    adherent = Adherent()
    adherent.username = data['username']
    adherent.password = data['password']
    adherent.Email = data['Email']
    adherent.nom = data['nom']
    adherent.prenom = data['prenom']
    adherent.adresse = data['adresse']
    adherent.genre = data['genre']
    adherent.tel = data['tel']
    adherent.save()
    SportsListSelect = request.session['sports']
    for sport in SportsListSelect:
        insc = Inscription(Email=adherent, designation=Sport.objects.get(designation=sport))
    insc.save()
    return render(request, 'main_app/Succes.html',
                  {'adherent': request.session.get('adherent'), 'SportsListSelect': SportsListSelect})
