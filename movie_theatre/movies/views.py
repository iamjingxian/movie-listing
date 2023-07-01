from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from .models import Movie
from .forms import MovieForm

def index(request):
    all_movies_in_db = Movie.objects.all

    submitted = False
    if request.method =="POST":
        form = MovieForm(request.POST)

        if form.is_valid() and 'addmovie_btn' in request.POST:
            print("here?1")
            form.save()
            return HttpResponseRedirect('/about-us/movies/')
        
        elif 'delete_btn' in request.POST: #Delete Button#
          movie_title_to_delete = request.POST['item_delete_id']
          obj_to_delete = Movie.objects.filter(movieTitle=movie_title_to_delete)
          obj_to_delete.delete()
          return HttpResponseRedirect('/about-us/movies/')
        
        else: #Buy Ticket Button#
            val = request.POST['Buy Ticket']
            movie_title = val.replace("Click here to buy tickets for ","") 
            redirectExtUrl = Movie.objects.filter(movieTitle=movie_title) \
            .values_list('buyTicketUrl', flat=True) \
            .first()
            return HttpResponseRedirect(redirectExtUrl)

    else:
        form = MovieForm
        if submitted in request.GET:
            submitted = True
    
    return render(request,'movies.html',{'all':all_movies_in_db, 'form':form, 'submitted':submitted})