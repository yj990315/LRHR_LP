from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Estimate, Photo
from .forms import TypeOfProductForm, PurposeForm, AddInformationForm, BasicInformationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'landingpage/main.html')

def basic_information_new(request):
    if request.method == "POST":
        estimate = Estimate()
        form = BasicInformationForm(request.POST, instance = estimate)
        if form.is_valid():
            form.save()
            """estimate.author = request.user"""
            return redirect('landingpage:purpose_new', estimate.id)
    else:
        basic_information_form = BasicInformationForm()
    return render(request, 'landingpage/basic_information.html', {'basic_information_form' : basic_information_form})

#@login_required(login_url='common:login')
def purpose_new(request, estimate_id):
    if request.method == "POST":
        estimate = get_object_or_404(Estimate, pk=estimate_id)
        form = PurposeForm(request.POST or None, instance = estimate)
        if form.is_valid():
            form.save()
            """estimate.author = request.user"""
            return redirect('landingpage:type_of_product_new', estimate_id)
    else:
        purpose_form = PurposeForm()
    return render(request, 'landingpage/request_pages/purpose.html', {'purpose_form' : purpose_form})

#@login_required(login_url='common:login')
def type_of_product_new(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    if request.method == "POST":
        form = TypeOfProductForm(request.POST or None, instance = estimate)
        if form.is_valid():
            form.save()
            return redirect('landingpage:request_new', estimate.id)
    else:
        type_of_product_form = TypeOfProductForm()
    return render(request, 'landingpage/request_pages/type_of_product.html', {'type_of_product_form' : type_of_product_form})

# @login_required(login_url='common:login')
def request_new(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    if request.method == "POST":
        estimate.request_content = request.POST['content']
        estimate.save()
        for img in request.FILES.getlist('imgs'):
            photo = Photo()
            photo.estimate = estimate
            photo.image = img
            photo.save()
        return redirect('landingpage:add_information', estimate.id)
    
    else:
        return render(request, 'landingpage/request_new.html', {'estimate_id' : estimate_id})

def add_information_new(request, estimate_id):
    estimate = get_object_or_404(Estimate, pk=estimate_id)
    if request.method == "POST":
        form = TypeOfProductForm(request.POST or None, instance = estimate)
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
    