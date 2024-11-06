import logging
from fastapi import FastAPI, WebSocket, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from io import StringIO
import pandas as pd

app = FastAPI()

# Mounting the 'static' folder at '/static'
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up the template directory
templates = Jinja2Templates(directory="templates/")

# Define a route for the home page that renders index.html
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    # Render index.html template
    return templates.TemplateResponse("index.html", {"request": request})

# Define a route for the home page that renders dashboard.html
@app.get("/dashboard", response_class=HTMLResponse)
async def read_index(request: Request):
    # Render index.html template
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        logging.info(f"Received file: {file.filename}, size: {len(contents)} bytes")

        # If it's a CSV file, try to process it
        if file.filename.endswith(".csv"):
            import pandas as pd
            from io import StringIO

            csv_file = StringIO(contents.decode())
            df = pd.read_csv(csv_file)
            logging.info(f"CSV Data: {df.head()}")

            return {"filename": file.filename, "data": df.to_dict()}
        else:
            return {"error": "Invalid file format"}

    except Exception as e:
        logging.error(f"Error processing file: {e}")
        return {"error": "Internal server error"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    stats = df.describe().to_dict()  # Generate basic statistics
    return stats
