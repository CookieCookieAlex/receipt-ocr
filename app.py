import numpy as np
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from utils import perform_ocr

app = FastAPI()

# Add CORS middleware to allow requests from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the OCR API"}

@app.get("/hr/")
async def root_hr():
    return {"message": "Dobrodošli u OCR API"}

@app.post("/ocr/")
async def ocr_receipt(file: UploadFile):
    # Check if the uploaded file is an image
    if file.content_type.startswith("image"):
        image_bytes = await file.read()
        img_array = np.frombuffer(image_bytes, np.uint8)

        ocr_text = perform_ocr(img_array)
        return JSONResponse(content={"result": ocr_text}, status_code=200)
    else:
        return {"error": "Uploaded file is not an image"}

@app.post("/ocr/hr/")
async def ocr_receipt_hr(file: UploadFile):
    # Check if the uploaded file is an image
    if file.content_type.startswith("image"):
        image_bytes = await file.read()
        img_array = np.frombuffer(image_bytes, np.uint8)

        ocr_text = perform_ocr(img_array)
        return JSONResponse(content={"rezultat": ocr_text}, status_code=200)
    else:
        return {"pogreška": "Prenesena datoteka nije slika"}

