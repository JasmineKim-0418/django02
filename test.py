import pdfplumber

pdf = pdfplumber.open("아뱅.pdf")

pnum = len(pdf.pages)

for i in range(pnum):
    p = pdf.pages[i] #1page에 대한 정보 가져옴
    print(p.extract_text())