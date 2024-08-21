from PyPDF2 import PdfWriter
from os import listdir

files = listdir("D:/Code/PDFMerger")

merger = PdfWriter()

for pdf in files:
    if pdf.endswith(".pdf"):
        if pdf != "result.pdf":
            with open(pdf, "rb") as f:
                merger.append(f)

merger.write("D:/Code/PDFMerger/result.pdf")