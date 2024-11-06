from fastapi import FastAPI, WebSocket, UploadFile, File
import pandas as pd

app = FastAPI()

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
