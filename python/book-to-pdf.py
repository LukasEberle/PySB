import PyPDF2

# pdfFile = open(path, 'rb') # rb = read Binary
# reader = PyPDF2.PdfFileReader(pdfFile)
# totalPages = reader.numPages
# tmp_writer = PyPDF2.PdfFileWriter()
# loop over PDF File add all pages expect the last, add blank pages until the total pages mod 4 = 0
# reorder recursively