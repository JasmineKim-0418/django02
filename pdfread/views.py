from django.shortcuts import render
import pdfplumber

# Create your views here.
def index(request):
    context = {}
    if request.method =="POST":
        p = request.FILES.get("pdf")
        pdf = pdfplumber.open(p)
        pnum = len(pdf.pages)
        st = ""
        for i in range(pnum):
            page = pdf.pages[i] #1page에 대한 정보 가져옴
            st += "="*30 +"\n"
            st += f"{i+1} PAGE TEXT" +"\n"
            st += "="*30 + "\n"
            st += page.extract_text()
            st += "\n"
        context["st"] = st
    return render(request,"pdfread/index.html",context)


