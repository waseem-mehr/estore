from .models import Cart
def cartItems(request):
    products=Cart.objects.all()
    totalItems=len(products)
    context={
        "cart_items":totalItems
    }
    return(context)