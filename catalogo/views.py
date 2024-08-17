from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from catalogo.forms import CustomerForm, CategoryForm, ProductForm, SaleForm, SaleProductFormSet
from catalogo.models import Customer, Category, Product, Sale, SaleItem

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo:customer_add')  # Redirige a la vista de agregar cliente
    else:
        form = CustomerForm()
    return render(request, 'customer_add.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

def index(request):
    return render(request, 'index.html')

def customer(request):
    customers = Customer.objects.order_by('last_name')
    template = loader.get_template('customer.html')
    return HttpResponse(template.render({'customers': customers}, request))

def info_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    template = loader.get_template('display_customer.html')
    context = {'customer': customer}
    return HttpResponse(template.render(context, request))

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_celulares:customer')
    else:
        form = CustomerForm()   
    return render(request, 'customer_form.html', {'form': form})

@login_required
def edit_customer(request, id):
    customer = get_object_or_404(Customer, pk=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('catalogo_celulares:customer')
    else:
        form = CustomerForm(instance=customer)       
    return render(request, 'customer_form.html', {'form': form})

@login_required
def delete_customer(request, id):
    customer = get_object_or_404(Customer, pk=id)
    customer.delete()
    return redirect("catalogo_celulares:customer")

def category(request):
    categories = Category.objects.order_by('name')
    template = loader.get_template('category.html')
    return HttpResponse(template.render({'categories': categories}, request))

def info_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    template = loader.get_template('display_category.html')
    context = {'category': category}
    return HttpResponse(template.render(context, request))

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_celulares:category')
    else:
        form = CategoryForm()   
    return render(request, 'category_form.html', {'form': form})

@login_required
def edit_category(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('catalogo_celulares:category')
    else:
        form = CategoryForm(instance=category)       
    return render(request, 'category_form.html', {'form': form})

@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect("catalogo_celulares:category")

def product(request):
    products = Product.objects.order_by('name')
    template = loader.get_template('product.html')
    return HttpResponse(template.render({'products': products}, request))

def info_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    template = loader.get_template('display_product.html')
    context = {'product': product}
    return HttpResponse(template.render(context, request))

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo_celulares:product')
    else:
        form = ProductForm()   
    return render(request, 'product_form.html', {'form': form})

@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalogo_celulares:product')
    else:
        form = ProductForm(instance=product)       
    return render(request, 'product_form.html', {'form': form})

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect("catalogo_celulares:product")

@login_required
def add_saleproduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.session['selected_product_id'] = product_id
    return redirect('catalogo_celulares:add_sale')

def sale(request):
    sales = Sale.objects.order_by('date')
    template = loader.get_template('sale.html')
    return HttpResponse(template.render({'sales': sales}, request))

def info_sale(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    template = loader.get_template('display_sale.html')
    context = {'sale': sale}
    return HttpResponse(template.render(context, request))

@login_required
def add_sale(request):
    selected_product_id = request.session.get('selected_product_id')
    request.session.pop('selected_product_id', None)

    if request.method == 'POST':
        form = SaleForm(request.POST)
        formset = SaleProductFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            sale = form.save()
            for form in formset:
                if form.cleaned_data.get('select'):
                    product_id = form.cleaned_data.get('product_id')
                    product = get_object_or_404(Product, id=product_id)
                    quantity = form.cleaned_data.get('quantity')
                    price = form.cleaned_data.get('price')

                    SaleItem.objects.create(
                        sale=sale,
                        product=product,
                        quantity=quantity,
                        price=price
                    )
            return redirect('catalogo_celulares:sale')

    else:
        form = SaleForm()
        sale_products = Product.objects.all()
        sale_product_forms = [SaleProductFormSet(initial={
            'product_id': p.id,
            'product_name': p.name,
            'category': p.category.name,
            'price': p.price
        }) for p in sale_products]
        formset = SaleProductFormSet(initial=[form.initial for form in sale_product_forms])

    return render(request, 'sale_form.html', {'form': form, 'formset': formset})
