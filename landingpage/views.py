from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Estimate, Photo
from .forms import TypeOfProductForm, PurposeForm, AddInformationForm, BasicInformationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'landingpage/main.html')

#@login_required(login_url='common:login')
def purpose_new(request):
    estimate = Estimate()
    form = PurposeForm(request.POST or None, instance = estimate)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            """estimate.author = request.user"""
            return redirect('landingpage:type_of_product_new', estimate.id)
    return render(request, 'landingpage/request_pages/purpose.html', {'purpose_form' : form})

#@login_required(login_url='common:login')
def type_of_product_new(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    form = TypeOfProductForm(request.POST or None, instance = estimate)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('landingpage:photo_new', estimate.id)
    return render(request, 'landingpage/request_pages/type_of_product.html', {'type_of_product_form' : form})

# @login_required(login_url='common:login')
def photo_new(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    if request.method == 'POST':
        if 'overall-img' in request.FILES:
            estimate.overall_image = request.FILES['overall-img']
            estimate.save()
        for img in request.FILES.getlist('detail-img'):
            photo = Photo()
            photo.estimate = estimate
            photo.detail_image = img
            photo.save()
        return redirect('landingpage:request_content_new', estimate.id)
    else:
        return render(request, 'landingpage/photo_new.html', {'estimate_id' : estimate_id})

def request_content_new(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    if request.method == "POST":
        estimate.request_content = request.POST['content']
        estimate.save()
        return redirect('landingpage:basic_information', estimate.id)
    else:
        return render(request, 'landingpage/request_content_new.html', {'estimate_id' : estimate_id})

def basic_information_new(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    if request.method == "POST":    
        form = BasicInformationForm(request.POST, instance = estimate)
        if form.is_valid():
            form.save()
            """estimate.author = request.user"""
            return redirect('landingpage:privacy', estimate_id)
    else:
        form = BasicInformationForm(instance=estimate)
    return render(request, 'landingpage/basic_information.html', {'basic_information_form' : form})

def privacy(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    if request.method == "POST":
        estimate.is_done = True
        estimate.save()
        return redirect('landingpage:result')
    return render(request, 'landingpage/privacy.html', {'estimate_id' : estimate_id})

def privacy_pop(request):
    return render(request, 'landingpage/privacy_pop.html')

def result(request):
    return render(request, 'landingpage/result.html')

def add_information_new(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    if request.method == "POST":
        form = AddInformationForm(request.POST or None, instance = estimate)
        if form.is_valid():
            form.save()
            return render(request, 'landingpage/main.html')
    else:
        add_information_form = AddInformationForm()
    return render(request, 'landingpage/add_information.html', {'add_information_form' : add_information_form})


#@login_required(login_url='common:login')
# def brand_new(request, estimate_id):
#     estimate = get_object_or_404(Estimate, pk=estimate_id)
#     if request.method == "POST":
#         form = BrandForm(request.POST or None, instance = estimate)
#         if form.is_valid():
#             form.save(commit=False)
#             form.create_date = timezone.now()
#             form.save()
#             return redirect('landingpage:request_new', estimate.id)
#     else:
#         brand_form = BrandForm()
#     return render(request, 'landingpage/request_pages/brand.html', {'brand_form' : brand_form})


# @login_required(login_url='common:login')
# def estimate_new(request):
#     if request.method == "POST":
#         form = EstimateForm(request.POST)
#         if form.is_valid():
#             estimate = form.save(commit=False)
#             estimate.author = request.user  # 추가한 속성 author 적용
#             estimate.create_date = timezone.now()   
#             estimate.save()
#             return redirect('landingpage:request_new', estimate.id)
#     else:
#         estimate_form = EstimateForm()
#     return render(request, 'landingpage/estimate_new.html', {'estimate_form' : estimate_form})

# def detail(request, estimate_id):
#     estimate = estimate.objects.get(id=estimate_id)
#     request = 
#     context = {'estimate': estimate, 'request': request}
#     return render(request, 'pybo/question_detail.html', context)
    