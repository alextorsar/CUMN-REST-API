from django.urls import path
from .userViews import RegisterView, LoginView, UserView, LogoutView
from .equiposViews import EquipoView, EquipoIdView, EquipoNombreView, PostEquipoFavoritoView, DeleteEquipoFavoritoView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('user/', UserView.as_view()),
    path('equipo/', EquipoView.as_view()),
    path('equipo/<int:id>/', EquipoIdView.as_view()),
    path('equipo/<str:nombre>/', EquipoNombreView.as_view()),
    path('equipoFavorito/<int:favorito>/', PostEquipoFavoritoView.as_view()),
    path('equipoFavorito/', DeleteEquipoFavoritoView.as_view()),
]