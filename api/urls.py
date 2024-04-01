from django.urls import path
from .userViews import RegisterView, LoginView, UserView, LogoutView
from .equiposViews import EquipoView, EquipoIdView, EquipoNombreView, PostEquipoFavoritoView, DeleteEquipoFavoritoView
from .partidosViews import PartidoView, PartidoIdView, PartidosEquipoView, PartidosJornadaView
from .valoracionesViews import ValoracionView, ValoracionPartidoView
from .visualizacionesViews import VisualizacionView, VisualizacionPartidoView
from .reseniasViews import ResenaView, ResenaPartidoView
from .seguidosViews import SeguidosView

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
    path('valoracion/partido/<int:partido_id>/', ValoracionPartidoView.as_view()),
    path('valoracion/<int:valoracion_id>/', ValoracionView.as_view()),
    path('visualizacion/', VisualizacionView.as_view()),
    path('visualizacion/<int:visualizacion_id>/', VisualizacionView.as_view()),
    path('visualizacion/partido/<int:partido_id>/', VisualizacionPartidoView.as_view()),
    path('resenia/', ResenaView.as_view()),
    path('resenia/<int:resena_id>/', ResenaView.as_view()),
    path('resenia/partido/<int:partido_id>/', ResenaPartidoView.as_view()),
    path('seguido/', SeguidosView.as_view()),
    path('seguido/<int:seguido_id>/', SeguidosView.as_view()),
]