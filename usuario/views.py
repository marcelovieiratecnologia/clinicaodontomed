from django.shortcuts import render
from .models import Profile

def avatar(request):
		avatar = Profile.objects.all()
		# print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF',avatar)
		return render(request, {'avatar':avatar})






