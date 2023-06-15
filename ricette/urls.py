from django.urls import path

from .import views



urlpatterns = [
    path("", views.homePageView, name="home"),
    path("login/", views.signin, name="login"),
    path("logout/", views.signout, name="logout"),
    path("register/", views.signup, name="register"),
    path("crea_ricetta/", views.crea_ricetta, name="crea_ricetta"),
    path("ricette/<int:id_ricetta>/", views.ricette, name="ricette"),
    path("lista_ricette/", views.lista_ricette, name="lista_ricette"),
    path("aggiungi_preferiti/<int:id_ricetta>/", views.aggiungi_preferiti, name="aggiungi_preferiti"),
    path("preferiti/", views.preferiti, name="preferiti"),
    path("rimuovi_preferiti/<int:id_ricetta>/", views.rimuovi_preferiti, name="rimuovi_preferiti"),
    path("idee_ricette/", views.idee_ricette, name="idee_ricette"),
    path("idee_ricette/antipasti/", views.antipasti, name="antipasti"),
    path("idee_ricette/primi/", views.primi, name="primi"),
    path("idee_ricette/secondi/", views.secondi, name="secondi"),
    path("idee_ricette/dolci/", views.dolci, name="dolci"),
    path("idee_ricette/contorni/", views.contorni, name="contorni"),
    path("idee_ricette/intolleranti/", views.intolleranti, name="intolleranti"),
]


