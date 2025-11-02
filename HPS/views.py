from django.shortcuts import render, redirect


def HomeView(request):
    
    return redirect("predictionAdd") if request.user.is_authenticated else redirect('started')



def Get_Started(request): return render(request,'core1/welcomeScreen.html')



# ERROR PAGES
def get_403(request,exception):  return render(request, 'core/errors/403.html', status=403)

def get_404(request,exception): return render(request, 'core/errors/404.html', status=404)

def get_500(request): return render(request, 'core/errors/500.html', status=500)

def get_400(request,exception): return render(request, 'core/errors/400.html', status=400)
