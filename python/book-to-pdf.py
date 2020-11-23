import PyPDF2

# loop over PDF File add all pages expect the last, add blank pages until the total pages mod 4 = 0
# reorder recursively


def add_blanks(reader, writer):
    pass


def reformat(pages, reader, writer):
    for i in range(1, pages/2, 2):
        writer.addPage(reader.getPage(i))
        writer.addPage(reader.getPage(pages-i))
        writer.addPage(reader.getPage(pages-(i+1)))
        writer.addPage(reader.getPage(i + 1))


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
