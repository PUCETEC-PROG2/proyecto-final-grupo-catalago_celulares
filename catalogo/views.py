from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .forms import *
from .models import *
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
def index(request):

    template = loader.get_template('index.html')
    return HttpResponse(template.render({'index': index}, request))

def productos(request):
    productos = Producto.objects.all()  
    context = {
        'productos': productos
    }
    return render(request, 'productos.html', context)

@login_required 
def detalle_producto(request, id):
    producto = Producto.objects.get(id=id)
    context = {
        'producto': producto
    }
    return render(request, 'detalle_producto.html', context)

@login_required    
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:productos')  
        else:
            print(form.errors)  
    else:
        form = ProductoForm()
    
    return render(request, "productos_form.html", {'form': form})


@login_required 
def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk = id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('catalogo:productos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'productos_form.html', {'form': form})

@login_required 
def eliminar_producto(required, id):
    producto = get_object_or_404(Producto, pk = id)
    producto.delete()
    return redirect('catalogo:productos')

@login_required 
def compras(request):
    compras = Compra.objects.order_by('fecha_compra')
    context = {
        'compras' : compras
    }
    return render(request, 'compras.html', context)

@login_required    
def agregar_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            productos = form.cleaned_data['productos']
            precio_total = request.POST.get('precio_total')
            compra.precio_total = sum([producto.precio for producto in productos])
            compra.save()
            form.save_m2m() 
            return redirect('catalogo:detalle_compra', id=compra.id)
    else:
        form = CompraForm()
    
    productos = Producto.objects.all()
    
    return render(request, 'agregar_compra.html', {'form': form, 'productos': productos})

@login_required 
def detalle_compra(request, id):
    compra = get_object_or_404(Compra, pk=id)
    productos = compra.productos.all()
    
    context = {
        'compra': compra,
        'productos': productos,
    }
    return render(request, 'detalle_compra.html', context)

@login_required 
def clientes (request):
    clientes = Cliente.objects.all()
    context = {
        'clientes' : clientes 
    }
    return render(request,'clientes.html', context )

@login_required 
def agregar_cliente(request):
    if request.method=='POST':
        form= ClienteForm(request.POST ,request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
        
    else:   
        form = ClienteForm()
        
    return render(request,"clientes_form.html",{'form': form }) 

@login_required 
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk = id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('catalogo:clientes')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'clientes_form.html', {'form': form})

@login_required 
def eliminar_cliente(required, id):
    cliente = get_object_or_404(Cliente, pk = id)
    cliente.delete()
    return redirect('catalogo:clientes')

class CustomLoginView(LoginView):
   template_name="login.html"
       