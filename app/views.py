from django.shortcuts import render

# Create your views here.
def plot(request):
    return render(request,'plot.html')

def mlmodel(request):
    return render(request,'mlPredict.html')