from django.urls import path, include
from entidades.views import *

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('home/', views.home, name='home'),

    path('acerca_de/', acerca_de, name="acerca_de"),
    
    # Juegos de mesa
    path('juegos_de_mesa/', Juegos_de_mesaList.as_view(), name="juegos_de_mesa"),
    path('juegos/', views.encontrarJuego, name='encontrarJuego'),
    path('juegos_de_mesaCreate/', Juegos_de_mesaCreate.as_view(), name="juegos_de_mesaCreate"),
    path('juegos_de_mesaUpdate/<int:pk>/', Juegos_de_mesaUpdate.as_view(), name="juegos_de_mesaUpdate"),
    path('juegos_de_mesaDelete/<int:pk>/', Juegos_de_mesaDelete.as_view(), name="juegos_de_mesaDelete"),
    
    # Miniaturas
    path('miniaturas/', MiniaturasList.as_view(), name="miniaturas"),
    path('miniatura/', views.encontrarMiniatura, name='encontrarMiniatura'),
    path('miniaturasCreate/', MiniaturasCreate.as_view(), name="miniaturasCreate"),
    path('miniaturasUpdate/<int:pk>/', MiniaturasUpdate.as_view(), name="miniaturasUpdate"),
    path('miniaturasDelete/<int:pk>/', MiniaturasDelete.as_view(), name="miniaturasDelete"),
    
    # Libros
    path('libros/', LibrosList.as_view(), name="libros"),
    path('libro/', views.encontrarLibro, name='encontrarLibro'),
    path('librosCreate/', LibrosCreate.as_view(), name="librosCreate"),
    path('librosUpdate/<int:pk>/', LibrosUpdate.as_view(), name="librosUpdate"),
    path('librosDelete/<int:pk>/', LibrosDelete.as_view(), name="librosDelete"),
    
    # Consolas
    path('consolas/', ConsolasList.as_view(), name="consolas"),
    path('consola/', views.encontrarConsola, name='encontrarConsola'),
    path('consolasCreate/', ConsolaCreate.as_view(), name="consolasCreate"),
    path('consolasUpdate/<int:pk>/', ConsolaUpdate.as_view(), name="consolasUpdate"),
    path('consolasDelete/<int:pk>/', ConsolaDelete.as_view(), name="consolasDelete"),

    # Login
    path('login/', ingresar, name="login"),
    
    # Logout
    path('logout/', views.logout, name='logout'),

    # Register
    path('register/', registrarse, name="register"),
    
    # Editar Usuario
    path('perfil/', editarProfil, name="perfil"),
    
    #Cambiar Contraseña
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='entidades/password_change.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='entidades/password_change_done.html'), name='password_change_done'),
    
    #Agregar imagen al usuario
    path('agregar_imagenUsuario/', agregarImagenUsuario, name="agregar_imagenUsuario"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)