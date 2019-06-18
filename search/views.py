from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'banks.html', {})

def bankdetails(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    ifsc = request.GET.get('ifsc')
    branch = request.GET.get('branch')
    city = request.GET.get('city')
    address = request.GET.get('address')
    disrict = request.GET.get('dist')
    state = request.GET.get('state')
    context = {'id': id, 'name': name, 'ifsc': ifsc, 'branch': branch, 'city':city, 'address': address, 'dist': disrict, 'state': state}
    return render(request, 'bankdetail.html', context)
