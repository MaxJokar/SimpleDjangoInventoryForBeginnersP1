from django.shortcuts import render , redirect
from django.views import View
from django.conf import settings
from django.forms import modelformset_factory
from account.models import CustomUser
from .models import MemoirGallery,Memoir,UserBlocked ,MemoirLike
from .forms import MemoirGalleryForm, MemoirForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# TEST template works or not 
from django.http import HttpResponse
# import datetime
# def now(request):
#     now = datetime.datetime.now() 
#     msg = f'Today is {now}'
#     return HttpResponse(msg, content_type='text/plain')

def media_admin(request):
    return {"media_url":settings.MEDIA_URL,}


class MainView(View):
    def get(self, request ,*args, **kwargs):
        memoi = Memoir.objects.all()
        #forms
        # form = MemoirForm
        # if request.method == 'GET':
        #     form = MemoirForm(request.GET)
        #     if form.is_valid():
        #         form.save()
        #         messages.success(request, 'Done','success')
        return render(request,'main_index.html',{ "memoi" : memoi})


    def post(self, request ,*args, **kwargs):
        pass
        
        # return render(request, 'templates/inventory_temp_app/index.html' , { "form" : form})




# 1.images and text of  Memoir:

# @login_required :unregistered USERs can not   surf our website pages & read memoirs
@login_required
def add_memoir(request):  
    ImageFormSet = modelformset_factory(MemoirGallery, form =MemoirGalleryForm, extra=4)
    if request.method =='GET':
        memoir_form = MemoirForm() # fields = ['memoir_title','Memoir_text']
        # in GET method ,we use none() means: DO NOT PUT ANYTHNG inside
        # A QuerySet is a collection of data from a database
        image_formset=ImageFormSet(queryset=MemoirGallery.objects.none(),)
        context={
            "memoir_form":memoir_form,
            "image_formset":image_formset
        }
        return render(request, 'register_memoir.html' ,context)
    elif request.method =='POST':
        memoir_form = MemoirForm(request.POST) #   title and text

        # request.FILES : get Both  text request.POST   and files request.FILES  from ImageFormSet
        image_formsset = ImageFormSet(request.POST,request.FILES)
        # TEST:
        # print(memoir_form.is_valid())
        # print(image_formset.is_valid())
        # print(100*'-')

        # To see the User  Added number in db :
        if memoir_form.is_valid() and image_formsset.is_valid(): # from valid (charfield , emailfield)
            # from main_memoir in db ,to obtain user_registered_id field
            cd = memoir_form.cleaned_data # a dictionary text & title  get from db as a dictionary
            mem_obj = Memoir.objects.create(
                memoir_title = cd["memoir_title"],
                Memoir_text = cd["Memoir_text"],
                user_registered = request.user # in veiw to access to user  request . user(from logged in USER)
            )


            # mem_obj = memoir_form.save() #memoir is saved
            for form in image_formsset.cleaned_data:
                if form: # if form had something with it
                    MemoirGallery.objects.create(
                        Memoir_image_name = form['Memoir_image_name'],
                        memoir= mem_obj
                    )
            messages.success(request, 'SAVED your Memoir  Successfully Done','success')
            return redirect('main:index')
        else:
            return render(request, 'register_memoir.html',{ "memoir_form":memoir_form })







