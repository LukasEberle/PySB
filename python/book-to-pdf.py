import PyPDF2
import os


# Please set these parameters
path_to_file = ""
output_file = ""
book_back_left = True


def reformat(pages, reader, writer, western):
    for i in range(0, pages, 2):
        if western:
            if i < pages - i:
                writer.addPage(reader.getPage(pages - (i + 1)))
                writer.addPage(reader.getPage(i))
                writer.addPage(reader.getPage(i + 1))
                writer.addPage(reader.getPage(pages - (i + 2)))
        if not western:
            if i < pages-i:
                writer.addPage(reader.getPage(i))
                writer.addPage(reader.getPage(pages - (i + 1)))
                writer.addPage(reader.getPage(pages - (i + 2)))
                writer.addPage(reader.getPage(i + 1))


pdfFile = open(path_to_file, 'rb')
org_reader = PyPDF2.PdfFileReader(pdfFile)
totalPages = org_reader.numPages
if not ((totalPages % 4) == 0):
    tmp_writer = PyPDF2.PdfFileWriter()
    tmp_writer.insertBlankPage(index=(totalPages - 2))
    added_blanks = open('../data/tmp.pdf', 'wb')
    tmp_writer.write(added_blanks)
    added_blanks.close()
    pdfFile.close()
    prepared_reader = open('../data/tmp.pdf', 'rb')
    book_writer = PyPDF2.PdfFileWriter()
    reformat(totalPages, prepared_reader, book_writer, book_back_left)
    prepared_reader.close()
    os.remove('../data/tmp.pdf')
else:
    book_writer = PyPDF2.PdfFileWriter()
    reformat(totalPages, org_reader, book_writer, book_back_left)
    pdfFile.close()
wb_output = open(output_file, 'wb')
book_writer.write(wb_output)
wb_output.close()
