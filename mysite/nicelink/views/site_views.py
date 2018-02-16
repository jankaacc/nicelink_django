
from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from ..models.Link import Link, LinkManager
from ..forms import LinkForm
from ..forms import UserRegisterForm


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LinkForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # link = Link.objects.create_link(form.cleaned_data['oryginal_link'])

            flag = True
            while flag:
                try:
                    link = Link(oryginal_link_text=form.cleaned_data['oryginal_link'],
                                nice_link_text=LinkManager.link_generator(),
                                user = None)
                    if request.user.is_authenticated:
                        link = Link(oryginal_link_text = form.cleaned_data['oryginal_link'],
                                    nice_link_text = LinkManager.link_generator(),
                                    user = request.user)
                        print(request.user.id)
                        link.save()
                    flag =False
                except IntegrityError:
                   print(IntegrityError)

            messages.success(request, 'Link generated')
            return render(request, 'nicelink/index.html', {'form': form,
                                                           'link':link})
    else:
        form = LinkForm()

    return render(request, 'nicelink/index.html', {'form': form})

@login_required(login_url='/nicelink/login/')
def link_list(request):
    links = Link.objects.filter(user = request.user)
    links = reversed(links)
    return render(request, 'nicelink/link_list.html',{'links' : links})

def redirect_to_oryginal_link(request, original_link):
    print(original_link)
    return redirect(original_link)

def user_register(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserRegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # link = Link.objects.create_link(form.cleaned_data['oryginal_link'])
            print('form valid')

            flag = True
            while flag:
                try:
                    form.clean()
                    form.save()
                    print('done')
                    flag = False
                except IntegrityError:
                    print('ERROR')


            return HttpResponseRedirect(reverse('nicelink:index'))
    else:
        form = UserRegisterForm()

    return render(request, 'nicelink/user.html', {'form': form})