from django.shortcuts import render,redirect
from .models import stock
from .forms import stockForm
from django.contrib import messages

def home(request):
	import requests 
	import json

	if request.method == "POST":
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_8ca7e1b16c3d4c68befb9978eadf7157")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html',{"api":api})

	else:
		return render(request, 'home.html',{'ticker':"enter a ticker symbol"})


	#pk_8ca7e1b16c3d4c68befb9978eadf7157
	
	

def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	import requests 
	import json



	if request.method == "POST":
		form = stockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("stock has been added"))
			return redirect('add_stock')
	else:


		ticker = stock.objects.all()
		output = []
	for ticker_item in ticker:
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_8ca7e1b16c3d4c68befb9978eadf7157")

		try:
			api = json.loads(api_request.content)
			output.append(api)
		except Exception as e:
			api = "Error..."
			
	return render(request, 'add_stock.html', {'ticker' : ticker,'output': output})

		
def delete(request, stock_id):
		item = stock.objects.get(pk=stock_id)
		item.delete()
		messages.success(request, ("stock has been deleted!"))
		return redirect(delete_stock)


def delete_stock(request):
	ticker = stock.objects.all()
	return render(request, 'delete_stock.html',{'ticker': ticker})
