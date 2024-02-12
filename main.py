from scrap import Scrapper


class Main:
    def __init__(self):
        pass

    @staticmethod
    def scrap_pdf(pdf_no):
        scrapper = Scrapper(pdf_no)
        scrapper.print_pdf_path()
        scrapper.read_table_data()
        scrapper.save_into_excel()


Main.scrap_pdf(3)
