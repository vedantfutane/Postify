from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse
from .models import Tweet
from .forms import Tweetform, UserRegisterationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == "POST":
       form = Tweetform(request.POST, request.FILES)
       if form.is_valid():
           tweet = form.save(commit=False)
           tweet.user = request.user
           tweet.save()
           return redirect('tweet_list')
    else:
        form = Tweetform()
    return render(request, 'tweet_form.html', {'form':form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user= request.user)
    if request.method=="POST":
       form = Tweetform(request.POST, request.FILES, instance=tweet)
       if form.is_valid():
           tweet= form.save(commit=False)
           tweet.user= request.user
           tweet.save()
           return redirect('tweet_list')
    else:
        form = Tweetform(instance=tweet)
    return render(request, 'tweet_form.html', {'form':form})

@login_required
def tweet_delete(request, tweet_id):
    tweet= get_object_or_404(Tweet, pk=tweet_id, user= request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request , 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegisterationForm()
    return render(request, 'registration/register.html', {'form': form})



def search_tweets(request):
    query = request.GET.get('q')  # Get the search query from the request
    results = []
    if query:
        # Search for tweets where the `text` field contains the query (case-insensitive)
        results = Tweet.objects.filter(text__icontains=query).only('text', 'photo', 'user', 'created_at')
    return render(request, 'search_results.html', {'results': results, 'query': query})
    
