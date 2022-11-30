from django.shortcuts import render
from django.http import HttpResponse

# temp add Cats class
class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
    
    def __str__(self):
        return f'What am I? {self.name}'

cats = [
    Cat('Rufus', 'tabbycat', 'crazy cat', 103),
    Cat('Bert', 'Calico', 'funny', 15),
    Cat('Simba', 'lion', 'brave', 5)
]

# Create your views here.
def index(request):
    return render(request, 'index.html', { 'cats': cats })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'blog.html')

def blog(request):
    return render(request, 'contact.html')