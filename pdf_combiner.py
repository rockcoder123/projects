from PyPDF2 import PdfFileMerger
pdf_files=['',''] # enter the first pdf name, enter the second pdf name with the .pdf extension, in the first and second double quotes respectively
merger=PdfFileMerger()
for i in pdf_files:
    merger.append(i)
merger.write('') # enter a pdf name which is not there in your pycharm folder, this pdf file will be created as you run the code. This pdf file will have your two pdf files entered, combined in it.
merger.close()
