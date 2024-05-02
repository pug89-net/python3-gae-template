from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from python3_gae_template.router import api, web

app = FastAPI()

# app.mount("/static", app=StaticFiles(directory="static"), name="static")

app.include_router(api.router, prefix="/api/v1")
app.include_router(web.router, default_response_class=HTMLResponse)

