from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Estimate, Request, Photo
from .forms import EstimateForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'landingpage/main.html')

@login_required(login_url='common:login')
def estimate_new(request):
    if request.method == "POST":
        form = EstimateForm(request.POST)
        if form.is_valid():
            estimate = form.save(commit=False)
            estimate.author = request.user  # 추가한 속성 author 적용
            """estimate.author = request.user"""
            estimate.create_date = timezone.now()   
            estimate.save()
            return redirect('landingpage:request_new', estimate.id)
    else:
        estimate_form = EstimateForm()
    return render(request, 'landingpage/estimate_new.html', {'estimate_form' : estimate_form})

@login_required(login_url='common:login')
def request_new(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    if request.method == "POST":
        request_instance = Request()
        request_instance.estimate = estimate
        request_instance.content = request.POST['content']
        request_instance.save()
        for img in request.FILES.getlist('imgs'):
            photo = Photo()
            photo.request_target = request_instance
            photo.image = img
            photo.save()
        return render(request, 'landingpage/main.html')
    
    else:
        return render(request, 'landingpage/request_new.html', {'estimate_id' : estimate_id})

# def detail(request, estimate_id):
#     estimate = estimate.objects.get(id=estimate_id)
#     request = 
#     context = {'estimate': estimate, 'request': request}
#     return render(request, 'pybo/question_detail.html', context)
    