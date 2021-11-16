FROM mcr.microsoft.com/azure-cognitive-services/vision/read:3.2-preview.1

RUN mkdir /ocr

RUN cd /ocr

COPY OCR.ipynb OCR.ipynb 

COPY OCR.py OCR.py 

COPY requirements.txt 

RUN pip3 install -r requirements.txt 

EXPOSE 8080 

ENTRYPOINT 
