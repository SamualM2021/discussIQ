from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import pandas as pd
import os
from io import StringIO

app = FastAPI()

@app.get("/")
def get():
    return HTMLResponse("""
    <html>
        <head>
            <title>Discuss IQ - Chat</title>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.min.js"></script>
        </head>
        <body>
            <h1>Chat Room</h1>
            <div id="chat"></div>
            <input type="text" id="message" placeholder="Enter message">
            <button onclick="sendMessage()">Send</button>

            <h2>Upload CSV</h2>
            <input type="file" id="file" accept=".csv">
            <button onclick="uploadFile()">Upload</button>

            <script>
                var socket = io.connect('http://' + document.domain + ':' + location.port);
                socket.on('message', function(msg) {
                    var chat = document.getElementById('chat');
                    chat.innerHTML += '<br>' + msg;
                });

                function sendMessage() {
                    var msg = document.getElementById('message').value;
                    socket.send(msg);
                }

                function uploadFile() {
                    var file = document.getElementById('file').files[0];
                    var reader = new FileReader();
                    reader.onload = function(e) {
                        var csvData = e.target.result;
                        fetch("/upload", {
                            method: "POST",
                            headers: { "Content-Type": "application/json" },
                            body: JSON.stringify({ data: csvData })
                        })
                        .then(response => response.json())
                        .then(data => console.log(data));
                    };
                    reader.readAsText(file);
                }
            </script>
        </body>
    </html>
    """)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message: {data}")
        except WebSocketDisconnect:
            break

@app.post("/upload")
async def upload(csv_data: str):
    df = pd.read_csv(StringIO(csv_data))
    return {"columns": df.columns.tolist(), "data": df.head(5).to_dict()}
