from django.shortcuts import render, redirect
import random

def root(request):
    if 'number_to_guess' not in request.session:
        request.session['number_to_guess'] = random.randint(0,100)
    return render(request, "index.html")

def handle_data(request):
    # number_to_guess = request.session['number_to_guess']
    # user_guess = request.session['guess_box']

    if 'guess_box' not in request.session:
        request.session['guess_box'] = request.POST['guess_box']
    request.session['guess_box'] = request.POST['guess_box']
    print(request.session['number_to_guess'])
    print(request.session['guess_box'])
    if request.session['number_to_guess'] > int(request.session['guess_box']):
        print("too low")
        return redirect('/too_low')
    elif request.session['number_to_guess'] < int(request.session['guess_box']):
        print("too high")
        return redirect('/too_high')
    else:
        print("success")
    return redirect('/success')

def too_low(request):
    return render(request, "too_low.html")

def too_high(request):
    return render(request, "too_high.html")

def success(request):
    return render(request, "success.html")

def start_over(request):
    request.session.clear()
    return redirect('/')




