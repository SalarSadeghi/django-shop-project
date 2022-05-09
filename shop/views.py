from django.views.generic import ListView, DetailView, TemplateView
from .models import Product
# Create your views here.
class HomePageView(ListView):
    paginate_by = 2
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    # queryset = Product.objects.order_by('id')
   
    def get_queryset(self):
        if self.request.method == 'GET':
            item_name = self.request.GET.get('item_name')
            if (item_name != '') and (item_name is not None):
                return Product.objects.filter(title__icontains=item_name)
            return Product.objects.all()       

class HomeDetailView(DetailView):
    model = Product
    template_name = 'detail.html'

class CheckOutView(TemplateView):
    template_name = 'checkout.html'

    def get_data(self):
        if self.request.method == 'POST':
            name = self.request.POST.get('name',"")
            address = self.request.POST.get('address',"")
            email = self.request.POST.get('email',"")
            city = self.request.POST.get('city',"")
            zip = self.request.POST.get('zip',"")
            

