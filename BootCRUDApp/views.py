from django.shortcuts import render,redirect,get_object_or_404
from .forms import GarageSell,GarageForm

# Create your views here.
def index(request):
    allJunk=GarageSell.objects.all() #gets an array of all models
    form=GarageForm(request.POST or None)   #get request of form
    context={
        'form':form,
        'allJunk':allJunk,
    }
    if request.method=='POST':  #if post request
        if form.is_valid(): #if valid
            form.save()
            return redirect('index')
        else:            #returns the filled form with errors
            form=GarageForm(request.POST or None)
        context={
            'form':form,
            'errors':form.errors,
        }
        return render(request,'BootCRUDApp/index.html',context)  #sends user back to index
    return render(request, 'BootCRUDApp/index.html',context)

def editItem(request,ID):     #accepts id from the model
    oldJunk=get_object_or_404(GarageSell,pk=ID)
    editJunk=GarageForm(request.POST ,instance=oldJunk)   #saves the old information
    if request.method=='POST':
        if editJunk.is_valid():  #if valid overwrites the previous form
            editJunk.save()
            return redirect('index')
        else: #otherwise sends errors
            context={
                'form':editJunk,
            '   errors':editJunk.errors,
            }
        return render(request,'BootCRUDApp/editItem.html',context)

    return render(request, 'BootCRUDApp/editItem.html',{'form':editJunk})
