import os

import cv2
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from pytesseract import Output

from TextCoordinate import TextCoordinate


class Main:

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.list: TextCoordinate = []
        pass

    def DrawBoundingBox(self, image_path, page_no=1):
        # Read image to extract text from image
        img = cv2.imread(f"images/{image_path}")
        # Resize the image if required
        height, width, channel = img.shape
        img = cv2.resize(img, (width // 1, height // 1))

        # Convert image to grey scale
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Converting grey image to binary image by Thresholding
        thresh_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # configuring parameters for tesseract
        custom_config = r'--oem 3 --psm 6'

        # Get all OCR output information from pytesseract
        ocr_output_details = pytesseract.image_to_data(thresh_img, output_type=Output.DICT, config=custom_config,
                                                       lang='eng')
        # Total bounding boxes
        n_boxes = len(ocr_output_details['level'])

        # Extract and draw rectangles for all bounding boxes
        for i in range(n_boxes):
            (x, y, w, h) = (ocr_output_details['left'][i], ocr_output_details['top'][i], ocr_output_details['width'][i],
                            ocr_output_details['height'][i])

            self.list.append(
                TextCoordinate(ocr_output_details['text'][i], page_no, ocr_output_details['line_num'][i], x, y, (x + w),
                               (y + h)))

            # print(ocr_output_details['level'][i],"  ",ocr_output_details['block_num'][i]," ", ocr_output_details['line_num'][i] ,"  ",ocr_output_details['par_num'][i])

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # print(ocr_output_details.keys())

        # print(ocr_output_details.keys())

        # Show output image with bounding boxes
        # cv2.imshow('img', img)
        cv2.waitKey(0)

    def ExtractDataFromPdf(self, pdf_path):
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        # print(pdf_document.page_count)
        file_name = os.path.basename(pdf_path).split('.')[0]
        extension = ".jpg"

        # Loop through each page
        for page_number in range(pdf_document.page_count):
            # Get the current page
            page = pdf_document[page_number]

            # print("page no :: " + str(page_number))

            # Get the page as an image (you can adjust the DPI value)
            image = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72))
            img = Image.frombytes("RGB", (image.width, image.height), image.samples)

            file_name_page_wise = file_name + "_" + str(page_number) + extension
            output_directory = 'images/'
            # Create the output directory if it doesn't exist
            os.makedirs(output_directory, exist_ok=True)
            output_file_path = os.path.join(output_directory, file_name_page_wise)
            img.save(output_file_path)

            self.DrawBoundingBox(file_name_page_wise, (page_number + 1))
            # print("Page No : " + str(file_name_page_wise) + str(page_number + 1))

            # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            #
            # # Perform OCR on the image
            # text = pytesseract.image_to_string(img)
            # # text = text.split
            # # Print the extracted text for the current page
            # print(f"Page {page_number + 1}:\n{text}\n")
            img.close()

        # Close the PDF document
        pdf_document.close()
        return self.list

    def PrintData(self, obj: TextCoordinate):
        print(f'{obj.text: <41}', f'{obj.pageNo: <5}',
              f'{obj.lineNo: <5}'
              , f'{obj.x1: <5}', f'{obj.y1: <5}', f'{obj.x2: <5}', f'{obj.y2: <5}')

    def StoreTableData(self):
        pass
