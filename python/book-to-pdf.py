import PyPDF2


def add_blanks(pages, reader, writer):
    to_add = pages % 4
    assert to_add != 0
    for i in range(0, (pages-2)):
        writer.addPage(reader.getPage(i))
    blank_file = open(path_to_file, 'rb')
    blank_reader = PyPDF2.PdfFileReader(blank_file)
    while to_add > 0:
        writer.addPage(blank_reader.getPage(0))
        to_add -= 1
    writer.addPage(reader.getPage(pages-1))


def reformat(pages, reader, writer):
    for i in range(0, pages, 2):
        if i < pages-i:
            writer.addPage(reader.getPage(i))
            writer.addPage(reader.getPage(pages-i))
            writer.addPage(reader.getPage(pages-(i+1)))
            writer.addPage(reader.getPage(i + 1))


path_to_file = ""
path_to_blank = ""
pdfFile = open(path_to_file, 'rb') # rb = read Binary
org_reader = PyPDF2.PdfFileReader(pdfFile)
totalPages = org_reader.numPages
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
