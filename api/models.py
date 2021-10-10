from django.db import models

# Create your models here.

categories = (
    ("P","Pants"),
    ("H","Hoodie"),
    ("S","Shoes"),
)

sizes = (
    ("S","Small"),
    ("M","Medium"),
    ("L","Large"),
)

colors = (
    ("R","Red"),
    ("B","Black"),
    ("G","Greeen"),
)
    

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.CharField(choices=categories, max_length=2)
    sizes = models.CharField(choices=sizes, max_length=2)
    colors = models.CharField(choices=colors, max_length=2)
    description = models.TextField()
    img = models.ImageField(blank=True)
    slug = models.SlugField()

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}"
    

class Cart(models.Model):
    token = models.CharField(max_length=100,default=True)
    items = models.ManyToManyField(Item)
    def __str__(self):
        return self.token
    
    def create(self,token):
        allcart = Cart.objects.filter(token=token)
        if allcart.exists():
            return False
        self.token = token
        self.save()
        return True

    def all_items(self):
        data = {}
        x = 0
        for item in self.items.all():
            category = [c.name for c in item.category.all()]
            color = [c.color for c in item.colors.all()]
            size = [s.size for s in item.sizes.all()]
            data[x] = {"id":item.id,"name":item.name,"price":item.price,"category":category,"size":size,"color":color,"description":item.description,"slug":item.slug}
            x+=1
        return data            
    

class Order(models.Model):
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    addres = models.CharField(max_length=100)
    post_code = models.IntegerField()
    shipped = models.BooleanField()

    def __str__(self):
        return self.name
    
