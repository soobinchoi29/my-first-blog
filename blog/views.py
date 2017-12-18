from django.shortcuts import render

from .models import Customer
from .form import PostForm

# Create your views here.
def index(request):
	return render(request, 'html/index.html')

def result(request):
	customers = Customer.objects.all()
	context = {'customers' : customers}

	return render(request, 'html/result.html', context)

def post(request):

	customers = Customer.objects.all()
	context = {'customers' : customers}
	
	if request.method == 'POST':
		form = PostForm(request.POST)
		
		if form.is_valid():
			customer = form.save(commit = False) # 중복방지
			customer.ip = request.META['REMOTE_ADDR']
			customer.save()
			
			return render(request,'html/result.html', context);
	else:
		form = PostForm()
	
	return render(request, 'html/form.html', {"form":form})

def analysis(request):
	return render(request, 'html/analysis.html')

def chatbot(request):
	return render(request, 'html/chatbot.html')