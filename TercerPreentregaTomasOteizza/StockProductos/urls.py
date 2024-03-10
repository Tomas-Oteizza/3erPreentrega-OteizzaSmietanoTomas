from django.urls import path , include 
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('procesador', procesador, name="procesador"),
    path('placaVideo', placaVideo, name="placaVideo"),
    path('teclado', teclado, name="teclado"),
    
    #---------Formularios:
    path('nuevoProcesadorForm', nuevoProcesadorForm, name="nuevoProcesadorForm"),
    path('nuevoPlacaVideoForm', nuevoPlacaVideoForm, name="nuevoPlacaVideoForm"),
    path('nuevoTecladoForm', nuevoTecladoForm, name="nuevoTecladoForm"),
    #=========Busqueda:
    path('buscarProcesadores', buscarProcesadores, name="buscarProcesadores"),
    path('buscarPlacasVideo', buscarPlacasVideo, name="buscarPlacasVideo"),
    path('buscarTeclados', buscarTeclados, name="buscarTeclados"),
    path('encontrarProcesadores', encontrarProcesadores, name="encontrarProcesadores"),
    path('encontrarPlacasVideo', encontrarPlacasVideo, name="encontrarPlacasVideo"),
    path('encontrarTeclados', encontrarTeclados, name="encontrarTeclados"),
]