from django.shortcuts import render
from .forms import UserForm
from .models import User

def signup(request):
	print("inside function")
	if request.method == 'POST':
		form = UserForm(request.POST)
		print("before if")
		if form.is_valid():
			print("true")
			username = request.POST.get('username')
			email = request.POST.get('email')
			password = request.POST.get('password')
			user_obj = User(username=username, email=email, password=password)
			user_obj.save()
			return render(request, 'users/signup.html', { 'user_obj' : user_obj , 'is_registered':True })

	else:
		form = UserForm()
		return render(request, 'users/signup.html', { 'form' : form })

def showdata(request):
	all_users = User.objects.all()
	return render(request, 'users/showdata.html', { 'all_users' : all_users })