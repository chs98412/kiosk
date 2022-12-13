from django.shortcuts import render, redirect
from .models import bad, money, cart, user, order
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.


def test(request):
    if(request.method == 'POST'):

        form = bad()
        form.who = request.POST["who"]
        form.when = request.POST["when"]
        form.what = request.POST["what"]
        form.why = request.POST["why"]
        form.save()
        print(form)
        total = money.objects.get(name="name")
        total.total = total.total+500
        total.save()

        return redirect('/main/test/')
    else:
        badwords = bad.objects.all()
        try:
            total = money.objects.get(name="name")
        except:
            m = money()
            m.total = 0
            m.name = "name"
            m.save()
        total = money.objects.get(name="name")
        context = {"bad": badwords, "total": total}
        return render(request, 'index.html', context=context)


def test2(request):
    print(request.POST)
    
    request.session['category'] = request.POST.get('category', False)
    request.session['ice'] = request.POST["ice"]
    return redirect('/main/cartview/')


def cartview(request):
    cartItem = cart.objects.all()
    context = {
        "category": request.session['category'], "ice": request.session['ice']}
    return render(request, 'cartview.html', context=context)


def delete(request):
    q = user.objects.all()
    q.delete()
    a = order.objects.all()
    a.delete()
    a = cart.objects.all()
    a.delete()
    return redirect('/main/test/')


def join(request):
    if(request.method == 'POST'):
        try:
            user.objects.get(hp=request.POST["hp"])
        except:
            form = user()
            form.hp = request.POST["hp"]
            form.name = request.POST["name"]
            form.save()
        return redirect('/main/test/')
    else:
        return render(request, 'join.html')


def hp(request):
        return render(request, 'hp.html')
@api_view(['POST'])
def hpPost(request):
    return Response("true")
def cardorsamsung(request):
    return render(request, 'cardorsamsung.html')
def card(request):
    if(request.method == 'POST'):

        return "true"
    else:
        form = cart()
        form.hp = request.session['hp']
        form.category = request.session['category']
        form.cardorSamsung="card"
        form.save()
        context = {"carts": cart.objects.all()}
        return render(request, 'card.html', context=context)

@api_view(['GET'])
def samsung(request):
    return Response("qwer!!")


def fin(request):
    temp = "01092098517"
    finalOrder = order()
    finalOrder.hp = temp
    finalOrder.name = user.objects.get(hp=temp).name
    finalOrder.category = request.session['category']
    finalOrder.result = True
    finalOrder.reason = "Success"
    finalOrder.save()
    context = {"orders": order.objects.all()}
    lists = order.objects.all()
    for i in lists:
        print(i.name)

    return render(request, 'fin.html', context=context)


def users(request):
    context = {"users": user.objects.all()}
    return render(request, 'users.html', context=context)
