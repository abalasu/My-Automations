from platform import java_ver
from fpdf import FPDF

txtfile = open("datafile.txt", "rt")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Courier",size=15)
i = 20
j = 0
tmplist = []
while (True):
    txtline = txtfile.readline()
    if txtline.count(",") > j:
        j = txtline.count(",")
    txtline = txtline.replace("\n","")
    if txtline.count(",") >= 1:
        tmplist = txtline.split(sep=",")
        print(tmplist)
    pdf.text(20, i, txtline)
    i += 8
    if len(txtline) == 0:
        break
k = 0
i = 0
while (k <= j):
    pdf.rect((i+10),10,50,50)
    i+=50
    k+=1

pdf.output("datafile.pdf")