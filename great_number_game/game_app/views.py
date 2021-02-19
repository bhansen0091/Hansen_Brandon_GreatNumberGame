from django.shortcuts import render, redirect
import random

def root(request):
    if 'number_to_guess' not in request.session:
        request.session['number_to_guess'] = random.randint(0,100)
    if 'guess_box' not in request.session:
        request.session['guess_box'] = -1   
    context = {
        "number_to_guess_template": request.session['number_to_guess'],
        "guess_box_template": int(request.session['guess_box'])
    }
    return render(request, "index.html", context)

def handle_data(request):
    request.session['guess_box'] = request.POST['guess_box']
    print(request.session['number_to_guess'])
    print(request.session['guess_box'])
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')




