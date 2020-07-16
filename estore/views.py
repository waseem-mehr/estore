from django.shortcuts import render,redirect
from .models import Product
from django.http import HttpResponse,JsonResponse
from json import loads
from .models import Cart
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    all_prods=[]
    products=Product.objects.values('prod_category')
    cats={item['prod_category'] for item in products}
    products=Product.objects.all()
    for cat in cats:
        for product in products:
            if(cat==product.prod_category):
                item={
                    "category":cat,
                    "category_image":product.prod_image
                }
                all_prods.append(item)
                break
            
    total_products=len(all_prods) 
    context={"range":range(1,total_products),"products":all_prods}
    return render(request,'estore/home.html',context)


def store(request,cat):
    products=Product.objects.filter(prod_category=cat)
    total_products=len(products)
    context={"range":range(1,total_products),"products":products}
    return  render(request,'estore/store.html',context)

def cart(request):
    products=Cart.objects.all()
    cart_products=[]
    single_product_items=0
    for item1 in products:
        for item2 in products:
            if(item1.product_name==item2.product_name):
                single_product_items=single_product_items+1
        item={
            "id":item1.product_id,
            "product":item1,
            "total_items":single_product_items,
            "total_price":single_product_items*item1.product_price
        }
        cart_products.append(item)
        single_product_items=0
    total_products_price=0
    total_products_cart_prices=[]
    for item in cart_products:
        total_products_cart_prices.append(item['total_price'])
    total_products_cart_prices={price for price in total_products_cart_prices}
    for price in total_products_cart_prices:
        total_products_price=total_products_price+price
    cart_products={v['id']:v for v in cart_products}.values()
    context={
        "cart_products":cart_products,
        "total_products_price":total_products_price,

    }

    return render(request,'estore/cart.html',context)

def checkout(request):
    products = Cart.objects.all()
    cart_products = []
    single_product_items = 0
    for item1 in products:
        for item2 in products:
            if (item1.product_name == item2.product_name):
                single_product_items = single_product_items + 1
        item = {
            "id": item1.product_id,
            "product": item1,
            "total_items": single_product_items,
            "total_price": single_product_items * item1.product_price
        }
        cart_products.append(item)
        single_product_items = 0
    total_products_price = 0

    total_products_cart_prices = []
    for item in cart_products:
        total_products_cart_prices.append(item['total_price'])
    total_products_cart_prices = {price for price in total_products_cart_prices}
    for price in total_products_cart_prices:
        total_products_price = total_products_price + price

    cart_products = {v['id']: v for v in cart_products}.values()
    context = {

        "total_products_price": total_products_price,

    }
    return render(request,'estore/checkout.html',context)



def product(request,i,id):
    id=str(id)
    product=Product.objects.filter(prod_id=id)

    products={}
    for x in product:
        products=x
    context={"product":products}
    return render(request,'estore/product.html',context)


def search(request):
    search_query=request.GET.get('search').lower()
    search_query=search_query.strip()
    if search_query=="":
        search_query="none"
    items=Product.objects.all()
    products=[]
    for item in items:
        if search_query in item.prod_name.lower():
            products.append(item)
    context={"products":products,"len":len(products)}
    return render(request,'estore/search.html',context)

def update_cart(request):
    data=loads(request.body)
    prod_id=data.get('product_id')
    action=data.get('action').strip()
    if action=='add':
        product=Product.objects.get(prod_id=prod_id)
        prod_name=product.prod_name
        prod_price=product.prod_price
        prod_image=product.prod_image
        create_cart=Cart.objects.create(product_id=prod_id,product_name=prod_name,
                                        product_price=prod_price,product_image=prod_image)
    elif action=='remove':
        product=Cart.objects.filter(product_id=prod_id)
        for x in product:
            x.delete()
            break
    return JsonResponse({"data":"hello"})

def login(request):
    return render(request,'estore/login.html')

def signup(request):
    form=UserCreationForm()
    if request.method=="POST":
        user=UserCreationForm(request.POST)
        print(user)
        print(user.is_valid())
        if user.is_valid():
            user.save()
            return redirect('/login/')
        else:
            errors=user.errors
    else:
        errors=False
    context={
        "form":form,
        "errors":errors
    }
    return render(request,'estore/signup.html',context)