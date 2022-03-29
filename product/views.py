from multiprocessing import context
from re import template
from urllib import request
from django.views.generic import DeleteView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.



# product detail page
# show all categories

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

# have to chage varialbles name..
class RegisterView(View):
    def get(self,request):
        return render(request,'registration.html')
    def post(self,request):
        username = request.POST['username']
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=username,first_name=first_name,last_name=last_name,email=email)
        # user.save()
        user.set_password(password)
        user.save()
        return redirect('login')


class LoginUserView(View):
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            error = "Enter valid details..."
            return render(request,'login.html',{'error':error})
    def get(self,request):
        return render(request,'login.html')


class ProfileView(View):
    def get(self,request):
        user_obj = User.objects.get(pk=request.user.id)
        total = Product.objects.filter(user=user_obj,deleted = False)
        category_obj = Category.objects.all()
        # product_list = Product.objects.all().order_by('id')
        paginetor = Paginator(total, 3)
        page_number = request.GET.get('page')
        page_obj = paginetor.get_page(page_number)
        return render(request,'profile_page.html',{'category_obj':category_obj,'pages':page_obj,'total':total.count()})


class CategoryProfileView(View):
    def get(self,request,category_name):
        user_obj = User.objects.get(pk=request.user.id)
        category_obj = Category.objects.all()
        product_obj = Product.objects.filter(product_category=category_name,user=user_obj,deleted=False)
        # total = Product.objects.filter(product_category=category_name,deleted=False,user=user_obj)
        # category_obj = Category.objects.all()
        context = {'product':product_obj, 'total':product_obj.count(),'category_obj':category_obj,'user':user_obj}
        return render(request,'category_on_profile.html',context)



class LogoutUserView(View):
    def get(self,request):
        logout(request)
        return redirect('login')
        

class AddProductView(View):
    def get(self,request):
        # user_name = User.objects.get(pk=request.user.id)
        # category = Category.objects.filter(user=user_name)
        category_list = Category.objects.all()
        return render(request,'add_product.html',{'category_list':category_list})
    def post(self,request):
        name = request.POST['product_name']
        discription = request.POST['product_discription']
        image = request.FILES.get('product_image')
        price = request.POST['product_price']
        category = request.POST['product_category']
        category_val = Category.objects.get(category_name=category)
        user_name = User.objects.get(pk=request.user.id)
        # category_list = Category.objects.all()
        product_data = Product(product_name=name, product_discription=discription, product_image=image, product_price=price, product_category=category_val,user=user_name)
        product_data.save()
        return redirect('profile')


class AddCategoryView(View):
    def get(self,request):
        category_list = Category.objects.all()
        return render(request,'add_category.html',{'category_list':category_list})
    def post(self,request):
        name = request.POST['category_name']
        user_name = User.objects.get(pk=request.user.id)
        if name == "":
            empty_category = "Enter the category..."
            return render(request,'add_category.html',{'empty_category':empty_category})
        elif Category.objects.filter(category_name__icontains=name).exists():
            category_error = "Category is already exists..."
            return render(request,'add_category.html',{'category':category_error})
        else:
            category_data = Category(category_name=name,user=user_name)
            category_data.save()
        return redirect('profile')

        


class DeleteProductView(View):
    def get(self,request,id):
        product = Product.objects.get(id=id)
        product.deleted = True
        product.save()
        return redirect('profile')
            


class HomePageView(View):
    def get(self,request):
        product_obj = Product.objects.filter(deleted=False)
        category_obj = Category.objects.all()
        paginetor = Paginator(product_obj,5)
        page_number = request.GET.get('page')
        page_obj = paginetor.get_page(page_number)
        context = {'product_list':page_obj,'category':category_obj,'product_obj':product_obj.count()}
        return render(request,'home_page.html',context)


class ShowCategoryView(View):
    def get(self,request,category_name):
        product_obj = Product.objects.filter(product_category=category_name,deleted = False)
        # total = Product.objects.filter(product_category=category_name,deleted = False)
        category_obj = Category.objects.all()
        context = {'product':product_obj, 'category':category_obj,'total':product_obj.count()}
        return render(request,'show_category_products.html',context)


class SearchProductView(View):
    def get(self,request):
        search_obj = request.GET['search']
        search_data = Product.objects.filter(product_name__icontains = search_obj,deleted=False)
        # total = Product.objects.filter(product_name__icontains = search_obj).count()
        category_obj = Category.objects.all()
        return render(request,'search.html',{'search':search_data,'category':category_obj,'total':search_data.count()})
  
        
class DetailProductView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class UpdateProductView(UpdateView):
    model = Product
    fields = ['product_name','product_discription','product_image','product_price']
    template_name = 'update_product.html'
    success_url = reverse_lazy('profile')