from django.shortcuts import render ,redirect
from django.views import View
from .forms import RegisterUserForm ,LoginUserForm
from .models import CustomUser
from django.contrib import messages  # to get messages
from django.contrib.auth import authenticate , login , logout




class RegisterUserView(View) :


# To show Register Form to the User in the website :
    def get(self, request,*args, **kwargs):
        form = RegisterUserForm()
        # context ={"form":form} Also one method to use context
        return render(request, 'register.html',{ "form":form })



    # def post(self, request,*args, **kwargs):
    #     # sourcery skip: remove-unnecessary-else, swap-if-else-branches,get , inquire data
    #     form=RegisterUserForm(request.POST)

    #     #The is_valid() method is used to [perform validation for each field of the form,] AND BRINGS TRUE
    #     # it is defined in Django Form class. It returns True if data is valid and place all data into a cleaned_data attribute.
    #     if  form.is_valid(): #if it is True

    #         #cleaned_data RETURNS a dictionary of VALIDATED FORM  input fields and their values, where string primary keys are
    #         # returned as objects. form. data returns a dictionary of un-validated form input fields and their values in string format
    #         user=form.cleaned_data
    #         CustomUser.objects.create_user(
    #             email = user['email'],
    #             name = user['name'],
    #             family = user['family'],
    #             mobile_number =user['mobile_number'],
    #             gender = user['gender'],
    #             password = user['password']
    #             # is_active = True during Registeration we can active it
    #         )
    #         messages.success(request, 'Registeration Successfully Done','success')
    #         return redirect('main:index')
    #     else:
    #         messages.error(request,'Information Invalid','ERROR')
    #         return render(request, 'register.html',{ "form":form })








class LoginUserView(View) :
     def get(self, request,*args, **kwargs):
        form = LoginUserForm()
       # render it into the page
        return render(request, 'account_app/login.html',{ "form":form })


     def post(self, request,*args, **kwargs):  # sourcery skip: assign-if-exp, remove-unnecessary-else, remove-unreachable-code, swap-if-else-branches
        form=LoginUserForm(request.POST)
            # if all the data is correct
            # as per the clean function, it returns true
        if form.is_valid():
            cd=form.cleaned_data
            # user=authenticate( username=cd.get('email'),password=cd.get('password'))
            user=authenticate( username=cd['email'],password=cd['password']) # gives a token in browser session
            if user is not None: # if user: confirm with our data!
                db_user=CustomUser.objects.get(email=user.email) # use.email is all datas discoverd by authenticate
                if not db_user.is_admin:
                    messages.success(request,'Successfully DONE, BRAVO!')
                    login(request,user)



                     # when you want to log in , look at the (request of )URL, & from its GET ,Do get fro me next :
                    next_url = request.GET.get('next') # keeps next URL !
                    if next_url is not None: # if its not empty
                        return redirect(next_url)
                    else:
                        return redirect('main:index')
                else:
                    messages.warning(request,'User Admin can not enter from here ')
                     # render it into the page
                    return render(request, 'account_app/login.html',{ "form":form })
            else:
                messages.warning(request,'USER was not found !')
                return render(request, 'account_app/login.html',{ "form":form })
        else:
            messages.warning(request,'Invalid Information ')
            return render(request, 'account_app/login.html',{ "form":form })



class LogoutUserView(View):
    # To avoid Twice logged out :
    def dispatch(self, request, *args, **kwargs):
        # sourcery skip: assign-if-exp, reintroduce-else, swap-if-expression
    # is_authenticated which is always False ). This is a way to tell if the user has been authenticated.
        if not request.user.is_authenticated:
             return redirect('main:index')
         # data from the form is fetched using super function
        return super().dispatch(request , *args, **kwargs)

    def get(self, request , *args, **kwargs):
        logout(request)
        messages.success(request,'Thanks ')
        return redirect('main:index')







