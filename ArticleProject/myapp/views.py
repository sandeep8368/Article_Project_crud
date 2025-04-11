from django.shortcuts import render , redirect
from myapp.models import ArticleModel
# Create your views here.
def display_index(request):
    submitted = False
    if request.method == 'POST':
        submitted = True
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        ArticleModel.objects.create(name = name, desc = desc)
        
    return render(request, 'html/index.html', {'submitted':submitted})


def display_articles(request):
    all_article = ArticleModel.objects.all()
    
    return render(request, 'html/display.html',{'data':all_article})


def spec_article(request,id):
    specific_data = ArticleModel.objects.get(id=id)
    print(specific_data.name)
    print(specific_data.desc)
    return render(request, 'html/specific.html',{'data':specific_data})


def delete(request,id):
    spec_data = ArticleModel.objects.get(id=id)
    spec_data.delete()
    return redirect("allart")



def update_view(request,id):
    spec_data = ArticleModel.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        spec_data.name = name
        spec_data.desc = desc
        spec_data.save()
    return render(request, 'html/update.html',{'data':spec_data})
    
    