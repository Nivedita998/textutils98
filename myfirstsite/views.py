#i hav created this file -niti
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     
     return render(request,'index.html',)
    #return HttpResponse('<h1>Home </h1>')

def analyze(request):
    #Get the text
    djtext=request.POST.get('text','default')

    #check check box values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    #check which box is on
    if removepunc=="on":
        punctuations=''' !()-[]{};:'"\,<>./?@#$&%^*_~ '''  
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                 analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text': analyzed}
        djtext=analyzed
       # return render(request,'analyze.html',params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed =analyzed+char.upper()
        params={'purpose':'change to uppercase','analyzed_text': analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if(  newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
               analyzed =analyzed+char
        params={'purpose':'remove new lines','analyzed_text': analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if( extraspaceremover== "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed =analyzed+char
        params={'purpose':'remove extra spaces','analyzed_text': analyzed}
    if(removepunc!="on" and fullcaps!= "on" and   newlineremover != "on" and extraspaceremover!= "on" ):
        return HttpResponse("please select the operations...")


    return render(request,'analyze.html',params)

def aboutus(request):
     
     return render(request,'aboutus.html',)
       
def contactus(request):
     
     return render(request,'contactus.html',)
       
   

    