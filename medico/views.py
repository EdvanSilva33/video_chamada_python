from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required
def cadastro_medico(request):
    if request.method == "GET":
        return render(request, 'cadastro_medico.html')