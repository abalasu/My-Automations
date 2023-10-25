import PyPDF2

pdfreader = PyPDF2.PdfReader("sample.pdf")
pdfwriter = PyPDF2.PdfWriter()

for page in pdfreader.pages:
    pdfwriter.add_page(page)

pdfwriter.encrypt("Arul")

with open("en_sample.pdf","wb") as f:
    pdfwriter.write(f)

