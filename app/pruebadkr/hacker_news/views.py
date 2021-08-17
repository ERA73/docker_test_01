import requests, json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

#@method_decorator(cache_page(100, key_prefix='main'), name='dispatch')
def index(request):
    return render(request, "busqueda.html", {})

def is_integer(value):
	try:
		int(value)
		return True
	except:
		return False

def busqueda(request, inicio = 0, final = 0):
	print(f"inicio:{inicio}, final:{final}")
	url = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
	# text = json.dumps(url.text)
	data = {}
	if is_integer(inicio) and is_integer(final) and int(inicio) >= 0 and int(final) > int(inicio):
		identificaciones = url.json()
		identificaciones = identificaciones[inicio:inicio+final]
		for identificacion in identificaciones:
			url_detalle = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{identificacion}.json?print=pretty")
			# detalle = url_detalle.json()
			detalle = url_detalle.text
			data[identificacion] = detalle
		# data["usuario_2"] = {"nombre":"Menganita", "apellido":"soles"}
	response_data = {"data":data}
	return HttpResponse(json.dumps(response_data), content_type="application/json")