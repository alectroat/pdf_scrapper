from scrap import Scrapper


class Main:
    def __init__(self):
        pass

    def scrap_pdf(self, pdf_no):
        scrapper = Scrapper(pdf_no)
        scrapper.read_table_data()
        scrapper.save_into_excel()


Main().scrap_pdf(10)
