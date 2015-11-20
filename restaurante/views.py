from django.http               import HttpResponseRedirect
from django.shortcuts          import render_to_response, redirect
from django.template           import RequestContext
from django.views.generic.base import TemplateView
from restaurante.models        import Cliente
from restaurante.models        import Plato
from restaurante.forms         import ClienteForm
from restaurante.forms         import PlatoForm
from django.contrib.auth       import logout
from django.contrib 		   import messages
from django.contrib.auth.decorators import login_required

class InicioView(TemplateView):
	template_name = "restaurante/index.html"

def logIn(request):
	return render_to_response("restaurante/login.html")
	

def logOut(request):
	logout(request)
	return redirect('/')

@login_required(login_url='/login')
def lista_clientes(request):
	clientes = Cliente.objects.all()
	return render_to_response("restaurante/clientes/clientes.html", {"clientes":clientes}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def agregar_cliente(request):
	if request.method == "POST":
		formulario = ClienteForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.INFO, 'Cliente Adicionado correctamente.')
			return HttpResponseRedirect("/clientes")
	else:
		formulario = ClienteForm()

	return render_to_response("restaurante/clientes/newCliente.html", {"formulario":formulario}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def borrar_cliente(request, id):
	cliente = Cliente.objects.get(pk=id)
	cliente.delete()
	messages.add_message(request, messages.INFO, 'El Cliente fu Eliminado.')
	return HttpResponseRedirect("/clientes")

@login_required(login_url='/login')
def editar_cliente(request, id):
	cliente = Cliente.objects.get(pk=id)	
	if request.method == "POST":
		formulario = ClienteForm(request.POST, instance=cliente)
		if formulario.is_valid():
			formulario.save()
			messages.add_message(request, messages.INFO, 'Datos del Cliente Modificados correctamente.')
			return HttpResponseRedirect("/clientes")
	else:
		formulario = ClienteForm(instance = cliente)

	return render_to_response("restaurante/clientes/editCliente.html", {"formulario":formulario}, context_instance=RequestContext(request))

##platos:
@login_required(login_url='/login')
def lista_platos(request):
	platos = Plato.objects.all()
	return render_to_response("restaurante/platos/platos.html", {"platos":platos}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def agregar_plato(request):
	if request.method == "POST":
		formulario = PlatoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()			
			return HttpResponseRedirect("/platos")
	else:
		formulario = PlatoForm()

	return render_to_response("restaurante/platos/newPlato.html", {"formulario":formulario}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def borrar_plato(request, id):
	plato = Plato.objects.get(pk=id)
	plato.delete()	
	Plato.imagen_delete(plato)
	return HttpResponseRedirect("/platos")

@login_required(login_url='/login')
def editar_plato(request, id):
	plato = Plato.objects.get(pk=id)	
	if request.method == "POST":
		formulario = PlatoForm(request.POST, request.FILES, instance=plato)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/platos")
	else:
		formulario = PlatoForm(instance = plato)

	return render_to_response("restaurante/platos/editPlato.html", {"formulario":formulario}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def catalogo(request):
	platos = Plato.objects.all()
	for p in platos:	
		listaDesc = list(p.descripcion)		
		descMenor = p.descripcion
		descMayor = ''
		ban = False
		for i in range(0,105):
			if(len(listaDesc)<105):
				descMenor = descMenor+' '
				p.descripcion = descMenor
				ban = True
			else:
				if(len(descMayor)<104):
					descMayor = descMayor+listaDesc[i]
					p.descripcion = descMayor
				else:
					descMayor = descMayor+' ...'
					p.descripcion = descMayor

	

	return render_to_response("restaurante/platos/catalogo.html", {"platos":platos}, context_instance=RequestContext(request))	