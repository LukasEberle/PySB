import PyPDF2

# loop over PDF File add all pages expect the last, add blank pages until the total pages mod 4 = 0
# reorder recursively


def add_blanks(reader, writer):
    pass


def reformat(page, reader, writer):
    pass


path_to_file = ""
pdfFile = open(path_to_file, 'rb') # rb = read Binary
org_reader = PyPDF2.PdfFileReader(pdfFile)
totalPages = reader.numPages
if not ((totalPages % 4) == 0):
    tmp_writer = PyPDF2.PdfFileWriter()
    add_blanks(tmp_writer, org_reader)
    # dump writer and open as reader and pass it instead of org_reader
    tmp_writer.close()
    tmp_writer = PyPDF2.PdfFileWriter()
    reformat(1, org_reader, tmp_writer)
else:
    tmp_writer = PyPDF2.PdfFileWriter()
    reformat(1, org_reader, tmp_writer)
