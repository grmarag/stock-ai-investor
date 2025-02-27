from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.ui import router as ui_router

app = FastAPI(title="Stock AI Investor")

# Mount static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include the UI router
app.include_router(ui_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)