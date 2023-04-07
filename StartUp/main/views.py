from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    return render(request, 'main/contact.html')

def blog_price(request):
    return render(request, 'blog/price.html')

def blog_feature(request):
    return render(request, 'blog/feature.html')

def blog_testimonial(request):
    return render(request, 'blog/testimonial.html')

def blog_team(request):
    return render(request, 'blog/team.html')

def blog_quote(request):
    return render(request, 'blog/quote.html')