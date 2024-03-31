from django.urls import path
from .userViews import RegisterView, LoginView, UserView, LogoutView
from .equiposViews import EquipoView, EquipoIdView, EquipoNombreView, PostEquipoFavoritoView, DeleteEquipoFavoritoView
from .partidosViews import PartidoView, PartidoIdView, PartidosEquipoView, PartidosJornadaView
from .valoracionesViews import ValoracionView
from .visualizacionesViews import VisualizacionView

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
    path('partido/', PartidoView.as_view()),
    path('partido/<int:id>/', PartidoIdView.as_view()),
    path('partido/equipo/<int:id>/', PartidosEquipoView.as_view()),
    path('partido/jornada/<int:jornada>/', PartidosJornadaView.as_view()),
    path('valoracion/', ValoracionView.as_view()),
    path('visualizacion/', VisualizacionView.as_view()),
]