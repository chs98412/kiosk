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
    request.session['hp']=request.POST["hp"]
    print(request.POST["hp"])
    print(request.session['hp'])
    return Response("true")
def cardorsamsung(request):
    return render(request, 'cardorsamsung.html')
def card(request):
        request.session['cardorSamsung']="card"
        return redirect('/main/pay/')
def pay(request):
        try:
            data=cart.objects.get(hp=request.session['hp'])
            data.delete()
        except:
            pass
        finally:
            form = cart()
            form.hp = request.session['hp']
            form.category = request.session['category']
            form.cardorSamsung=request.session['cardorSamsung']
            form.save()
        return render(request, 'pay.html')
def samsung(request):
    request.session['cardorSamsung']="samsung"
    return redirect('/main/pay/')
@api_view(['POST'])
def paycheck(request):
    try:
        print(request.POST['hp'])

        data=cart.objects.get(hp=str(request.POST['hp']))
        if data.cardorSamsung==request.POST['cardorSamsung']:
            return Response("same")
        else:
            return Response("differ")
    except Exception as e:
        print(e)
        return Response("error!!!")
@api_view(['POST'])
def done(request):
    try:
        print(request.POST["hp"])
        data=cart.objects.get(hp=request.POST["hp"])
        form=order()
        form.hp=data.hp
        form.name=request.POST['name']
        form.result=request.POST['result']
        form.category=data.category
        form.reason=request.POST['reason']
        return Response("done")
    except:
        return Response("error")
def donepage(request):
    return render(request, 'donepage.html')
def fin(request):

    context = {"orders": order.objects.all()}

    return render(request, 'fin.html', context=context)


def users(request):
    context = {"users": user.objects.all()}
    return render(request, 'users.html', context=context)
def carts(request):
    context = {"carts": cart.objects.all()}
    return render(request, 'carts.html', context=context)
