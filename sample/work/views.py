from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.http import HttpResponse
from datetime import date
from .models import Question,Stan
i=1


def index(request):
    global i
   
    c=Stan.objects.get(pk=i)
    
    year=date.today()
    a=5
    b=59
    question=Question.objects.get(pk=i)
    val=c.reponse
    
  
    return render(request,"index.html",{"year": year,"question":question,"i":i,"val":val,"a":a,"b":b})


    
    
  

    
    

def retr(request):
    if request.method=='POST' and 'next' in request.POST:
        
         i= int(request.POST['i'])
         q=Question.objects.get(pk=i)
         a=(request.POST['a'])
         b=(request.POST['b'])
         item=request.POST.get('ch',False)
         h=Stan(ques=q,reponse=item,pk=i)
   
         
         h.save()
        
         k=Question.objects.get(id=i)
         
         flaga=request.POST['flaga']
         print flaga
         i=i+1

       
         if (i>=4 or flaga==1):
            x=0
            for k in range(1,3):
                s=Question.objects.get(pk=k)
                t=Stan.objects.get(pk=k)
                
                if s.answer== t.reponse :
                   x=x+1
            return render(request,"retr2.html",{"x":x})
         question=Question.objects.get(id=i)
         try:
            st = Stan.objects.get(pk=i)
         except ObjectDoesNotExist:
            val=0;
            return render(request,"index.html",{"question":question,"i":i,"val":val,"a":a,"b":b})
         val=st.reponse
         return render(request,"index.html",{"question":question,"i":i,"val":val,"a":a,"b":b})
    if request.method=='POST' and 'back' in request.POST:
      
         i= int(request.POST['i'])
         q=Question.objects.get(pk=i)
        
         item=request.POST.get('ch',False)
         h=Stan(ques=q,reponse=item,pk=i)
         h.save()
         i=i-1
         a=(request.POST['a'])
         b=(request.POST['b'])
         rep=Stan.objects.get(pk=i)
         val=rep.reponse
         print a
         question=Question.objects.get(pk=i)
         if val==False:
            return render(request,"index.html",{"question":question,"i":i, "val":val,"a":a,"b":b})
       
         else :
            return render(request,"index.html",{"question": question,"i":i,"val":val,"a":a,"b":b})   
       


























