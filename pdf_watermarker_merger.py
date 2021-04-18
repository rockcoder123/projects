import PyPDF2
# before coding the below steps, make sure that you have your both the pdf files in your pycharm folder.
pdf=PyPDF2.PdfFileReader(open('','rb')) # enter the pdf name with .pdf extension in the first single quotes (this is the pdf upon which you need to apply the watermark)
watermark=PyPDF2.PdfFileReader(open('','rb')) # enter the pdf name with .pdf extension in the first single quotes (this is the watermark.pdf)
output=PyPDF2.PdfFileWriter()
for i in range(pdf.getNumPages()):
    page=pdf.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
with open('','wb') as file1: # just name a new pdf file with the .pdf extension here, which is not existing in your pycharm folder. This pdf file will be created as soon you run this code
    output.write(file1)
