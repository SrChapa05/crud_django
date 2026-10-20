
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm



def listar_productos(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render(request, 'productos/listar.html', contexto)

def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm()

    contexto = {'formulario': formulario}
    return render(request, 'productos/crear.html', contexto)


def editar_producto(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm(instance=producto)

    contexto = {
        'formulario': formulario,
        'producto': producto
    }

    return render(request, 'productos/editar.html', contexto)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')

    contexto = {'producto': producto}
    return render(request, 'productos/eliminar.html', contexto)
