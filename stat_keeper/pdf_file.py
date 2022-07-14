import logging
import slate3k
class PdfFile:
    def __init__(self, pdf_file: str):
        logging.getLogger('pdfminer').setLevel(logging.ERROR)
        try:
            self.file = open(pdf_file, "rb")
        except Exception as e:
            print("Unable to open PDF File")
            print(f"ERROR: {e}")
        #self.num_pages = self.reader.numPages
    
    def get_page(self, num_page: int):
        return slate3k.PDF(self.file)

