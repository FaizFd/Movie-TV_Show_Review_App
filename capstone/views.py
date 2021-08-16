from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Listing,Comment,Cart,Alllisting
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime


def index(request):
    items=Listing.objects.all()
    try:
        w = Cart.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    page = request.GET.get('page', 1)

    paginator = Paginator(items, 10)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)    
    return render(request, "capstone/index.html",{
        "items":items,
        "wcount":wcount,
    })


def categories(request):
    items=Listing.objects.raw("SELECT * FROM capstone_listing GROUP BY category")
    try:
        w = Cart.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"capstone/categpage.html",{
        "items": items,
        "wcount":wcount
    })

def categoriess(request):
    items=Listing.objects.raw("SELECT * FROM capstone_listing GROUP BY categorys")
    try:
        w = Cart.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"capstone/categpages.html",{
        "items": items,
        "wcount":wcount
    })  


def categoriesss(request):
    items=Listing.objects.raw("SELECT * FROM capstone_listing GROUP BY categoryss")
    try:
        w = Cart.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"capstone/categpagess.html",{
        "items": items,
        "wcount":wcount
    })      

def category(request,category):
    catitems = Listing.objects.filter(category=category)
    try:
        w = Cart.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"capstone/category.html",{
        "items":catitems,
        "cat":category,
        "wcount":wcount
    })

def categorys(request,categorys):
    catitemss = Listing.objects.filter(categorys=categorys)
    try:
        w = Cart.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"capstone/categorys.html",{
        "items":catitemss,
        "cats":categorys,
        "wcount":wcount
    })    
def categoryss(request,categoryss):
    catitemsss = Listing.objects.filter(categoryss=categoryss)
    try:
        w = Cart.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"capstone/categoryss.html",{
        "items":catitemsss,
        "catss":categoryss,
        "wcount":wcount
    })    

def create(request):
    try:
        w = Cart.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"capstone/create.html",{
        "wcount":wcount
    })

def submit(request):
    if request.method == "POST":
        listtable = Listing()
        now = datetime.now()
        dt = now.strftime(" %d %B %Y %X ")
        listtable.owner = request.user.username
        listtable.title = request.POST.get('title')
        listtable.title1 = request.POST.get('title1')
        listtable.title2 = request.POST.get('title2')
        listtable.description = request.POST.get('description')
        listtable.cast = request.POST.get('cast')
        listtable.price = request.POST.get('price')
        listtable.category = request.POST.get('category')
        listtable.categorys = request.POST.get('categorys')
        listtable.categoryss = request.POST.get('categoryss')
        if request.POST.get('link'):
            listtable.link = request.POST.get('link')
        else :
            listtable.link = "https://i.pinimg.com/564x/26/9e/76/269e76626c5c4438e6f602da66043a7b.jpg"       
        if request.POST.get('links'):
            listtable.links = request.POST.get('links')     
        else : 
            listtable.links = "https://www.imdb.com" 
        if request.POST.get('trailer'):
            listtable.trailer = request.POST.get('trailer')     
        else : 
            listtable.trailer = "https://www.youtube.com/embed/dQw4w9WgXcQ"   
        if request.POST.get('img'):
            listtable.img = request.POST.get('img')
        else :
            listtable.img = "https://i.pinimg.com/564x/26/9e/76/269e76626c5c4438e6f602da66043a7b.jpg"
        if request.POST.get('imgg'):
            listtable.imgg = request.POST.get('imgg')
        else :
            listtable.imgg = "https://i.pinimg.com/564x/26/9e/76/269e76626c5c4438e6f602da66043a7b.jpg"            
        listtable.time = dt
        listtable.save()
        all = Alllisting()
        items = Listing.objects.all()
        for i in items:
            try:
                if Alllisting.objects.get(listingid=i.id):
                    pass
            except:
                all.listingid=i.id
                all.title = i.title
                all.title1 = i.title1
                all.title2 = i.title2
                all.description = i.description
                all.cast = i.cast
                all.link = i.link
                all.links = i.links
                all.trailer = i.trailer
                all.img = i.img
                all.imgg = i.imgg

                all.save()

        return redirect('index')
    else:
        return redirect('index')


def listingpage(request,id):
    try:
        item = Listing.objects.get(id=id)
    except:
        return redirect('index')
    try:
        comments = Comment.objects.filter(listingid=id)
    except:
        comments = None
    if request.user.username:
        try:
            if Cart.objects.get(user=request.user.username,listingid=id):
                added=True
        except:
            added = False
        try:
            l = Listing.objects.get(id=id)
            if l.owner == request.user.username :
                owner=True
            else:
                owner=False
        except:
            return redirect('index')
    else:
        added=False
        owner=False
    try:
        w = Cart.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"capstone/listingpage.html",{
        "i":item,
        "error":request.COOKIES.get('error'),
        "errorgreen":request.COOKIES.get('errorgreen'),
        "comments":comments,
        "added":added,
        "owner":owner,
        "wcount":wcount
    })



def cmntsubmit(request,listingid):
    if request.method == "POST":
        now = datetime.now()
        dt = now.strftime(" %d %B %Y %X ")
        c = Comment()
        c.comment = request.POST.get('comment')
        c.user = request.user.username
        c.time = dt
        c.listingid = listingid
        c.save()
        return redirect('listingpage',id=listingid)
    else :
        return redirect('index')


def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Listing.objects.all().filter(title__contains=search)   
        return render(request, "capstone/search.html", {
        'post': post    
     })


def addcart(request,listingid):
    if request.user.username:
        w = Cart()
        w.user = request.user.username
        w.listingid = listingid
        w.save()
        return redirect('listingpage',id=listingid)
    else:
        return redirect('index')


def removecart(request,listingid):
    if request.user.username:
        try:
            w = Cart.objects.get(user=request.user.username,listingid=listingid)
            w.delete()
            return redirect('listingpage',id=listingid)
        except:
            return redirect('listingpage',id=listingid)
    else:
        return redirect('index')

def cartpage(request,username):
    if request.user.username:
        try:
            w = Cart.objects.filter(user=username)
            items = []
            for i in w:
                items.append(Listing.objects.filter(id=i.listingid))
            try:
                w = Cart.objects.filter(user=request.user.username)
                wcount=len(w)
            except:
                wcount=None
            return render(request,"capstone/cartpage.html",{
                "items":items,
                "wcount":wcount
            })
        except:
            try:
                w = Cart.objects.filter(user=request.user.username)
                wcount=len(w)
            except:
                wcount=None
            return render(request,"capstone/cartpage.html",{
                "items":None,
                "wcount":wcount
            })
    else:
        return redirect('index')   

   


def corlosal(request):
    return render(request,"capstone/corlosal.html")


def test(request):
    return render(request,"capstone/test.html")    
    



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "capstone/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "capstone/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "capstone/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "capstone/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "capstone/register.html")
