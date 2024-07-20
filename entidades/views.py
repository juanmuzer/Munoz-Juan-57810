from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth import logout as django_logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):
    # Crear el contexto con 3 objetos de cada seccion seleccionados aleatoriamente
    contexto = {"juegos_random": Juegos_de_Mesa.objects.order_by('?')[:3], 
                "miniaturas_random": Miniaturas.objects.order_by('?')[:3], 
                "libros_random": Libros.objects.order_by('?')[:3],
                "consolas_random": Consolas.objects.order_by('?')[:3]
                }
    # Renderizar la plantilla con el contexto
    return render(request, "entidades/index.html", contexto)

def acerca_de(request):
    return render(request, "entidades/acerca_de.html")

# Juegos de mesa
class Juegos_de_mesaList(ListView):
    model = Juegos_de_Mesa

def encontrarJuego(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar']
        juegos = Juegos_de_Mesa.objects.filter(nombre__icontains=patron)
    else:
        juegos = Juegos_de_Mesa.objects.all()

    contexto = {"juegos_de_mesa": juegos}
    return render(request, "entidades/juegos_de_mesa.html", contexto)

class Juegos_de_mesaCreate(CreateView):
    model = Juegos_de_Mesa
    fields = ["codigo", "nombre", "cant_jugadores", "edad_recomendada", "precio", "imagen"]
    success_url = reverse_lazy("juegos_de_mesa")
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        if 'imagen' in self.request.FILES:
            obj.imagen = self.request.FILES['imagen']
        obj.save()
        return super().form_valid(form)


class Juegos_de_mesaUpdate(UpdateView):
    model = Juegos_de_Mesa
    fields = ["codigo", "nombre", "cant_jugadores", "edad_recomendada", "precio", "imagen"]
    success_url = reverse_lazy("juegos_de_mesa")
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        if 'imagen' in self.request.FILES:
            obj.imagen = self.request.FILES['imagen']
        obj.save()
        return super().form_valid(form)
    
class Juegos_de_mesaDelete(DeleteView):
    model = Juegos_de_Mesa
    success_url = reverse_lazy("juegos_de_mesa")

# Miniaturas
class MiniaturasList(ListView):
    model = Miniaturas

def encontrarMiniatura(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar']
        miniaturas = Miniaturas.objects.filter(nombre__icontains=patron)
    else:
        miniaturas = Miniaturas.objects.all()

    contexto = {"miniaturas": miniaturas}
    return render(request, "entidades/miniaturas.html", contexto)

class MiniaturasCreate(CreateView):
    model = Miniaturas
    fields = ["codigo", "nombre", "escala", "material", "precio", "imagen"]
    success_url = reverse_lazy("miniaturas")
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        if 'imagen' in self.request.FILES:
            obj.imagen = self.request.FILES['imagen']
        obj.save()
        return super().form_valid(form)

class MiniaturasUpdate(UpdateView):
    model = Miniaturas
    fields = ["codigo", "nombre", "escala", "material", "precio", "imagen"]
    success_url = reverse_lazy("miniaturas")
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        if 'imagen' in self.request.FILES:
            obj.imagen = self.request.FILES['imagen']
        obj.save()
        return super().form_valid(form)

class MiniaturasDelete(DeleteView):
    model = Miniaturas
    success_url = reverse_lazy("miniaturas")

# Libros
class LibrosList(ListView):
    model = Libros

def encontrarLibro(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar']
        libros = Libros.objects.filter(nombre__icontains=patron)
    else:
        libros = Libros.objects.all()

    contexto = {"libros": libros}
    return render(request, "entidades/libros.html", contexto)


class LibrosCreate(CreateView):
    model = Libros
    fields = ["codigo", "nombre", "autor", "genero", "cant_pag", "precio", "imagen"]
    success_url = reverse_lazy("libros")
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        if 'imagen' in self.request.FILES:
            obj.imagen = self.request.FILES['imagen']
        obj.save()
        return super().form_valid(form)

class LibrosUpdate(UpdateView):
    model = Libros
    fields = ["codigo", "nombre", "autor", "genero", "cant_pag", "precio", "imagen"]
    success_url = reverse_lazy("libros")
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        if 'imagen' in self.request.FILES:
            obj.imagen = self.request.FILES['imagen']
        obj.save()
        return super().form_valid(form)

class LibrosDelete(DeleteView):
    model = Libros
    success_url = reverse_lazy("libros")
    
# Consolas
class ConsolasList(ListView):
    model = Consolas

def encontrarConsola(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar']
        consola = Consolas.objects.filter(nombre__icontains=patron)
    else:
        consola = Consolas.objects.all()

    contexto = {"consola": consola}
    return render(request, "entidades/consolas.html", contexto)

class ConsolaCreate(LoginRequiredMixin, CreateView):
    model = Consolas
    fields = ["codigo", "nombre", "modelo", "estado", "precio", "imagen"]
    success_url = reverse_lazy("consolas")

    def form_valid(self, form):
        obj = form.save(commit=False)
        if 'imagen' in self.request.FILES:
            obj.imagen = self.request.FILES['imagen']
        obj.save()
        return super().form_valid(form)

class ConsolaUpdate(LoginRequiredMixin, UpdateView):
    model = Consolas
    fields = ["codigo", "nombre", "modelo", "estado", "precio", "imagen"]
    success_url = reverse_lazy("consolas")
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        if 'imagen' in self.request.FILES:
            obj.imagen = self.request.FILES['imagen']
        obj.save()
        return super().form_valid(form)

class ConsolaDelete(LoginRequiredMixin, DeleteView):
    model = Consolas
    success_url = reverse_lazy("consolas")
    
# Login
def ingresar(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            try:
                foto = ImagenUsuario.objects.get(user=request.user).imagen.url
            except ImagenUsuario.DoesNotExist:
                foto = "/media/imagenesusuarios/default.png"
                
            request.session["imagenUsuario"] = foto
            
            return redirect('home')
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "entidades/login.html", {"form": miForm})

# Logout
def logout(request):
    django_logout(request)
    return redirect('home')

# Register

def registrarse(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "entidades/register.html", {"form": miForm})   

# Editar Perfiles
@login_required
def editarProfil(request):
    usuario = request.user
    if request.method == "POST":
        miForm = EditarUsuarioForm(request.POST, instance=usuario)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = EditarUsuarioForm(instance=usuario)
    return render(request, "entidades/editarPerfil.html", {"form": miForm})

# Agregar foto de usuario
@login_required
def agregarImagenUsuario(request):
    if request.method == "POST":
        miForm = ImagenUsuarioForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            # Borrar avatares viejos
            imagenVieja = ImagenUsuario.objects.filter(user=usuario)
            if len(imagenVieja) > 0:
                for i in range(len(imagenVieja)):
                    imagenVieja[i].delete()

            imagenUsuario = ImagenUsuario(user=usuario, imagen=imagen)
            imagenUsuario.save()

            imagen = ImagenUsuario.objects.get(user=usuario).imagen.url
            request.session["imagenUsuario"] = imagen

            return redirect(reverse_lazy("home"))
    else:
        miForm = ImagenUsuarioForm()
    return render(request, "entidades/agregarImagenUsuario.html", {"form": miForm})    