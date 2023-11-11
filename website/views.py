from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.forms import ContactForm, NewsLetterForm
from django.contrib import messages
from django.utils.safestring import mark_safe
# def check_published_date():
    # now = datetime.now()

    # # Now time with timezone
    # now = timezone.make_aware(datetime(now.year, now.month, now.day, now.hour, now.minute, now.second))

    # # Now time without timezone
    # # now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    
    # posts = Post.objects.filter(published_date__lte=now)
    # print(now)
    # context = {'context': posts}
    # return context

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Update values before save ****************************************************************
            obj = form.save(commit=False)
            obj.name = "unknown"
            # Update values before save ****************************************************************
            form.save()
            messages.add_message(request, messages.SUCCESS, '******************<br>Well done<br>******************')
            # return HttpResponseRedirect('/contact')
        else:
            messages.add_message(request, messages.ERROR, 'Somthing went wrong<br>please try again')
            # return HttpResponseRedirect('/contact')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '******************<br>Well done<br>******************')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Somthing went wrong<br>please try again')
    return HttpResponseRedirect('/')

def json_test(request):
    return JsonResponse({'name': 'Mr.BoO', 'description': 'Scary funny little ghost'})