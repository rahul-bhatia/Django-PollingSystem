from django.shortcuts import render,redirect
from .models import PollModel
from .forms import PollForm

# Create your views here.


def results(request,id):
	data=PollModel.objects.get(pk=id)
	return render(request,'results.html',{'data':data})
def vote(request,id):
	data=PollModel.objects.get(pk=id)
	if request.method =="POST":
		sel_option =request.POST.get('r1')
		if sel_option =="op1":
			data.op1c+=1
		elif sel_option=="op2":
			data.op2c+=1
		else:
			data.op3c+=1
		data.save()
		return redirect('home')
	else:
		return render(request,'vote.html',{'data':data})
def home(request):
	data=PollModel.objects.all()
	print(data)
	return render(request,'home.html',{'data':data})

def create(request):
	if request.method=="POST":
		f=PollForm(request.POST)
		if f.is_valid():
			f.save()
			fm=PollForm()
			return render(request,'create.html',{'fm':fm,'msg':'Added'})
		else:
			return render(request,'create.html',{'fm':f,'msg':'Check Errors'})

	else:
		fm=PollForm()
		return render(request,'create.html',{'fm':fm})