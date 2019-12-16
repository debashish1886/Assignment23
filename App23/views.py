from django.shortcuts import render


def main(request):
    return render(request,"index.html")


def adding(request):
    list=request.POST.getlist('bf')
    tot=0
    for x in list:
        tot=tot+int(x)
    tax=tot*8/100
    Gtotal=tot+tax
    return render(request,"index.html",{'data':{'list':list,'tot':tot,'tax':tax,'tottal':Gtotal}})