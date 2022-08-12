from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()


app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)


templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse("pages/forside.html", {"request": request})


@app.get("/{page}")
async def get_page(request: Request, page):
    try:
        return templates.TemplateResponse(
            "pages/{0}.html".format(page, "utf-8"), {"request": request}
        )
    except:
        raise HTTPException(status_code=404, detail="Page not found")