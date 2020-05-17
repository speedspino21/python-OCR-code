from __future__ import print_function
import time
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
from pprint import pprint
import glob
from PIL import Image
import os

# Configure API key authorization: Apikey
configuration = cloudmersive_ocr_api_client.Configuration()
configuration.api_key['Apikey'] = '6b6fd0b7-85f1-4cad-875e-56091afe9aaa'


import glob
directory = r'./fileset1/hardest_files/' #path
pdfFiles = glob.glob(os.path.join(directory, '*.*'))
print(pdfFiles)
for pdf_path in pdfFiles:
# create an instance of the API class
    api_instance = cloudmersive_ocr_api_client.PdfOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
    image_file = pdf_path
    recognition_mode = 'Normal'
    language = 'RON' # for english(ENG),for Romanian(RON)
    preprocessing = 'Advanced'
    try:
        try:
            # Converts an uploaded PDF file into text via Optical Character Recognition.
            api_response = api_instance.pdf_ocr_post(image_file, recognition_mode=recognition_mode, language=language, preprocessing=preprocessing)
            final = api_response.ocr_pages[0].text_result
            output_name = pdf_path.split('/')[-1].replace('.pdf','').replace('.jpg','').replace('.png','')
            output_dir = './data'
            ls = r'{0}/{1}.txt'.format(output_dir,output_name)
            with open(ls, "w") as text_file:
                text_file.write(final)
            print('Done:', output_name)
        except:
            # My image is a 200x374 jpeg that is 102kb large
            foo = Image.open(pdf_path)
            foo = foo.resize((800,800),Image.ANTIALIAS)
            output_name = pdf_path.split('/')[-1].replace('.pdf','').replace('.jpg','').replace('.png','')
            foo.save(r"./fileset1/hardest_files/{0}.jpg".format(output_name),quality=95)
            api_response = api_instance.pdf_ocr_post(image_file, recognition_mode=recognition_mode, language=language, preprocessing=preprocessing)
            final = api_response.ocr_pages[0].text_result
            output_name = pdf_path.split('/')[-1].replace('.pdf','').replace('.jpg','').replace('.png','')
            output_dir = './data'
            ls = r'{0}/{1}.txt'.format(output_dir,output_name)
            with open(ls, "w") as text_file:
                text_file.write(final)
            print('Done:', output_name)
    except ApiException as e:
        print("Exception when calling PdfOcrApi->pdf_ocr_post: %s\n" % e)

   