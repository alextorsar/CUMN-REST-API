from django.urls import path
from .views.userViews import RegisterView, LoginView, UserView, LogoutView, AllUsersView
from .views.equiposViews import EquipoView, EquipoIdView, EquipoNombreView, PostEquipoFavoritoView, DeleteEquipoFavoritoView
from .views.partidosViews import PartidoView, PartidoIdView, PartidosEquipoView, PartidosJornadaActualView, PartidosJornadaView, PartidosStatusView
from .views.valoracionesViews import ValoracionView, ValoracionPartidoView
from .views.visualizacionesViews import VisualizacionView, VisualizacionPartidoView
from .views.reseniasViews import ResenaView, ResenaPartidoView
from .views.seguidosViews import SeguidosView, SeguidoresView
from .views.socialViews import UltimasAccionesSociales
from .views.estadisticasViews import EstadisticasView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('user/', UserView.as_view()),
    path('users/', AllUsersView.as_view()),
    path('equipo/', EquipoView.as_view()),
    path('equipo/<int:id>/', EquipoIdView.as_view()),
    path('equipo/<str:nombre>/', EquipoNombreView.as_view()),
    path('equipoFavorito/<int:favorito>/', PostEquipoFavoritoView.as_view()),
    path('equipoFavorito/', DeleteEquipoFavoritoView.as_view()),
    path('partido/', PartidoView.as_view()),
    path('partido/<int:id>/', PartidoIdView.as_view()),
    path('partido/equipo/<int:id>/', PartidosEquipoView.as_view()),
    path('partido/jornada/<int:jornada>/', PartidosJornadaView.as_view()),
    path('partido/jornada/actual/', PartidosJornadaActualView.as_view()),
    path('partido/status/<int:status>/', PartidosStatusView.as_view()),
    path('partido/status/', PartidosStatusView.as_view()),
    path('valoracion/', ValoracionView.as_view()),
    path('valoracion/partido/<int:partido_id>/', ValoracionPartidoView.as_view()),
    path('visualizacion/', VisualizacionView.as_view()),
    path('visualizacion/<int:visualizacion_id>/', VisualizacionView.as_view()),
    path('visualizacion/partido/<int:partido_id>/', VisualizacionPartidoView.as_view()),
    path('resenia/', ResenaView.as_view()),
    path('resenia/<int:partido_id>/', ResenaView.as_view()),
    path('resenia/partido/<int:partido_id>/', ResenaPartidoView.as_view()),
    path('seguido/', SeguidosView.as_view()),
    path('seguido/<int:seguido_id>/', SeguidosView.as_view()),
    path('seguidor/', SeguidoresView.as_view()),
    path('social/', UltimasAccionesSociales.as_view()),
    path('estadisticas/', EstadisticasView.as_view()),
]