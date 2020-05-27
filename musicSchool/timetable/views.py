from django.shortcuts import render, redirect 
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import OrderForm
from school.models import Teacher


def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Баян').count()
	pending = orders.filter(status='Аккордеон').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'dashboard.html', context)

def products(request):
	products = Product.objects.all()

	return render(request, 'products.html', {'products':products})

def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'customer.html',context)


def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'order_form.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'delete.html', context)


def status(request):
    return render(
        request, 
        'status.html',
        {
            'posts': Teacher.objects.all(),
        }    
    )
	
'''
from .MyForm import MyForm 
# Create your views here.

def mainview(request):
	f=MyForm()
	#rendering the home.html 
	#sending the form to the template 
	# to render the html 
	return render(request, 'detail.html', {'form':f})
	
def showview(request):
	rec_form=MyForm(request.POST)
	
	#let's access the ChoiceField and it's properties
	#we can access ChoiceField from rec_form as a BoundField object
	b_f=rec_form['c_field'] #name of the field variable
	
	#let's access the properties
	dct={
		'auto_id': b_f.auto_id,
		'data': b_f.data,
		'errors': b_f.errors,
		'field': b_f.field,
		'form': b_f.form,
		'help_text': b_f.help_text,
		'html_name': b_f.html_name,
		'id_for_label': b_f.id_for_label,
		'is_hidden': b_f.is_hidden,
		'label': b_f.label,
		'name': b_f.name,
	}
	
	#let's send the data to the template page
	return render(request, 'show.html', {'data': dct})
	'''
'''
from django.forms import modelformset_factory
from django.shortcuts import render
from .models import Author

def manage_authors(request):
    AuthorForm = modelformset_factory(Author, fields=('name', 'title'))
    if request.method == 'POST':
        formset = AuthorForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = AuthorForm()
    return render(request, 'detail.html', {'formset': formset})

'''