from django.shortcuts import render
from .models import Notice,Principal,Contact,Gallery


def home(request):

    notices = Notice.objects.all().order_by("-date")[:6]
    images = Gallery.objects.all()

    return render(request, "home.html", {
        "notices": notices,
        "images": images
    })

def about(request):
    return render(request, 'about.html')

def notices(request):
    notices = Notice.objects.all()
    return render(request, 'notices.html', {'notices': notices})

def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'gallery.html', {'images': images})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, 'contact.html')
