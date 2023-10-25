import PyPDF2

file_name = input("Enter PDF Name ")
file_data = PyPDF2.PdfReader(file_name)
no_of_pages = len(file_data.pages)
print("PDF Header ", file_data.pdf_header)
print("PDF information ", file_data.metadata)
print("Named desination ", file_data.named_destinations)
"""
i = 0
while (i < no_of_pages):
    page=file_data.pages[i]
    text = page.extract_text()
    print(text)
    count=0
    for images in page.images:
        with open(str(count) + images.name, "wb") as fp:
            fp.write(images.data)
            count += 1
            print("Image file name ", images.name)
    i+=1

    """