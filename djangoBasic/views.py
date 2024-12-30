from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    #get text
    djtext=request.POST.get("text","default")
    removepunc=request.POST.get('removepunc','off')
    capatalized=request.POST.get('Capatalize','off')
    newline=request.POST.get("NewlineRemover",'off')
    spaceremover=request.POST.get("extraspaceremover",'off')
    #analyze the text
    punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #checkbox-function
    if(removepunc=='on'):
        analyzed=''
        for i in djtext:
            if(i not in punctuation):
                analyzed+=i
        params={'purpose':'Remove Punctuation','analyze_text':analyzed}
        djtext=analyzed
    if(capatalized=="on"):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed To Uppercase','analyze_text':analyzed}
        djtext=analyzed
    if(newline=="on"):
        analyzed=''
        for char in djtext:
            if(char=='\n' or char=="\r"):
                analyzed+=" "
            else:
                analyzed+=char 
        params={'purpose':'Removed Newline','analyze_text':analyzed}
        djtext=analyzed
    if(spaceremover=='on'):
        analyzed=''
        for ind,char in enumerate(djtext):
            if not(djtext[ind]==" " and djtext[ind+1]==" "):
                analyzed+=char
        params={'purpose':'Extra Spaced Is Removed','analyze_text':analyzed}
    if(spaceremover=='off' and newline=='off' and capatalized=='off' and removepunc=='off' ):
        return render(request,'Error.html')
    return render(request,'analyze.html',params)
    