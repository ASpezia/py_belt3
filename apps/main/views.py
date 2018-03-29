# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, reverse


def index(request):
    if 'user_id' not in request.session:
        request.session['user_id'] = -1
    return render(request,'main/index.html')

def login(request, methods = ['POST']):
    errors = User.objects.login_validator(request.POST)
    print errors
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)

        return redirect('/')
    request.session['status'] = "Logged in"
    return redirect("/landing/{}" .format(request.session["id"]))


def register(request, methods = ['POST']):
    errors = User.objects.registration_validator(request.POST)
    print "registration"
    print errors
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
        
    print "len"
    password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
    User.objects.create(name = request.POST['name'], user_name = request.POST['user_name'], password = password)
    request.session['id'] = User.objects.last().id
    request.session['status'] = "registered"

    return redirect("landing/{}".format(request.session["id"]))

def landing(request):
        u_id = request.session['user_id']
        user = User.objects.get(id =u_id)
        user_n = user.user_name
        item = User.objects.get(id=u_id).items.all()
        others = Item.objects.exclude(item__id = u_id)

        context = {
            'user': user_n,
            'items': item,
            'others': others
        }
        return render(request,'main/landing.html',context)

def add_item(request):
    postdata = {
                "item": request.POST['description'],
                "user_id": request.session['user_id'],
                "date_added" : request.POST['date_added'],
        }
    result = Item.objects.add_item_validator(postdata)
    if result[0]:
        print result[1]
        return redirect('/landing')
    else:
        print result
        for item in result[1].values():
            messages.error(request, item)
        return render(request,'main/add_item')


def wish_items(request):
    pass

def remove(request):
    if item in items: items.remove(item)
    return redirect('/landing')


def logout(request):
    request.session.clear()
    return redirect('/')
