from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    return render(request, "StockProductos/index.html")

def procesador(request):
    procesadores = Procesador.objects.all()
    contexto = {'procesadores': procesadores}
    return render(request, "StockProductos/procesador.html", contexto)

def placaVideo(request):
    placasVideo = PlacaVideo.objects.all()  
    contexto = {'placasVideo': placasVideo}  
    return render(request, "StockProductos/placaVideo.html", contexto)

def teclado(request):
    teclados = Teclado.objects.all()
    contexto = {'teclados': teclados}
    return render(request, "StockProductos/teclado.html", contexto)

#-------------------- formularios de nuevos productos:
def nuevoProcesadorForm(request):
    if request.method == "POST":
        nuevoProcesador = NuevoProcesadorForm(request.POST)
        if nuevoProcesador.is_valid():
            
            procesadorMarca = nuevoProcesador.cleaned_data.get("marca")
            procesadorModelo = nuevoProcesador.cleaned_data.get("modelo")
            procesadorPrecio = nuevoProcesador.cleaned_data.get("precio")
            procesadorDescripcion = nuevoProcesador.cleaned_data.get("descripcion")
            
            procesadorNuevo = Procesador.objects.create(
                marca=procesadorMarca,
                modelo=procesadorModelo,
                precio=procesadorPrecio,
                descripcion=procesadorDescripcion
            )
            return redirect("home")  
    else:
        nuevoProcesador = NuevoProcesadorForm()
        
    return render(request, "StockProductos/nuevoProcesadorForm.html", {"form": nuevoProcesador})

def nuevoPlacaVideoForm(request):
    if request.method == "POST":
        nuevoPlacaVideo = NuevoPlacaVideoForm(request.POST)
        if nuevoPlacaVideo.is_valid():
            
            placaVideoMarca = nuevoPlacaVideo.cleaned_data.get("marca")
            placaVideoModelo = nuevoPlacaVideo.cleaned_data.get("modelo")
            placaVideoPrecio = nuevoPlacaVideo.cleaned_data.get("precio")
            placaVideoDescripcion = nuevoPlacaVideo.cleaned_data.get("descripcion")
            
            placaVideoNuevo = PlacaVideo.objects.create(
                marca=placaVideoMarca,
                modelo=placaVideoModelo,
                precio=placaVideoPrecio,
                descripcion=placaVideoDescripcion
            )
            return redirect("home")  
    else:
        nuevoPlacaVideo = NuevoPlacaVideoForm()
        
    return render(request, "StockProductos/nuevoPlacaVideoForm.html", {"form": nuevoPlacaVideo})

def nuevoTecladoForm(request):
    if request.method == "POST":
        nuevoTeclado = NuevoTecladoForm(request.POST)
        if nuevoTeclado.is_valid():
            
            tecladoMarca = nuevoTeclado.cleaned_data.get("marca")
            tecladoModelo = nuevoTeclado.cleaned_data.get("modelo")
            tecladoPrecio = nuevoTeclado.cleaned_data.get("precio")
            tecladoDescripcion = nuevoTeclado.cleaned_data.get("descripcion")
            
            TecladoNuevo = Teclado.objects.create(
                marca=tecladoMarca,
                modelo=tecladoModelo,
                precio=tecladoPrecio,
                descripcion=tecladoDescripcion
            )
            return redirect("home")  
    else:
        nuevoTeclado = NuevoTecladoForm()
        
    return render(request, "StockProductos/nuevoTecladoForm.html", {"form": nuevoTeclado})

#-------------Formulario de busqueda:
def buscarProcesadores(request):
    return render(request, "StockProductos/buscarProcesadores.html")

def encontrarProcesadores(request):
    if 'buscarProcesadores' in request.GET:
        patron = request.GET.get('buscarProcesadores', '')
        if patron:
            procesadores = Procesador.objects.filter(modelo__icontains=patron)
            contexto = {"procesadores": procesadores}
            return render(request, "StockProductos/procesador.html", contexto)

    
    contexto = {'procesadores': Procesador.objects.all()}
    return render(request, "StockProductos/procesador.html", contexto)

def buscarPlacasVideo(request):
    return render(request, "StockProductos/buscarPlacasVideo.html")

def encontrarPlacasVideo(request):
    if 'buscarPlacasVideo' in request.GET:
        patron = request.GET.get('buscarPlacasVideo', '')
        if patron:
            placasVideo = PlacaVideo.objects.filter(modelo__icontains=patron)
            contexto = {"placasVideo": placasVideo}  
            return render(request, "StockProductos/placaVideo.html", contexto)

    contexto = {'placasVideo': PlacaVideo.objects.all()}
    return render(request, "StockProductos/placaVideo.html", contexto)

def buscarTeclados(request):
    return render(request, "StockProductos/buscarTeclados.html")

def encontrarTeclados(request):
    if 'buscarTeclado' in request.GET:  
        patron = request.GET.get('buscarTeclado', '')  
        if patron:
            teclados = Teclado.objects.filter(modelo__icontains=patron)
            contexto = {"teclados": teclados}
            return render(request, "StockProductos/teclado.html", contexto)

    
    
    contexto = {'teclados': Teclado.objects.all()}
    return render(request, "StockProductos/teclado.html", contexto)




    
