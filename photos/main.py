from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from deta import Deta

app = FastAPI()
deta = Deta("a0bbqsrh_c2bH4it9HCzFC5r6GPbqRtq2EXrR46Jx")  # configure your Deta project 
drive = deta.Drive("images") # access to your drive

@app.get("/", response_class=HTMLResponse)
def render():
    return """
    <form action="/upload" enctype="multipart/form-data" method="post">
        <input name="file" type="file">
        <input type="submit">
    </form>
    """
@app.get("/pic")
def rendering():
    img = drive.get('1.jpg')
    return responses.StreamingResponse(img.iter_chunks(), media_type=f"octet-stream/{'jpg'}")

@app.get("/{name}")
async def serve(name):
    img = drive.get(name)
    ext = name.split(".")[1]
    return responses.StreamingResponse(img.iter_chunks(), media_type=f"octet-stream/{ext}")

@app.post("/upload")
def upload_img(file: UploadFile = File(...)):
    name = file.filename
    f = file.file
    res = drive.put(name, f)
    return res

@app.get("/download/{name}")
def download_img(name: str):
    res = drive.get(name)
    return StreamingResponse(res.iter_chunks(1024), media_type="image/png")