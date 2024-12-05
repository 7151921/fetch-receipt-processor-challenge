import logging

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

from app.api.routes import receipt_router

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Receipt Processor",
    description="A simple receipt processor",
    version="1.0.0"
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={
            "detail": exc.errors(),
            "body": await request.json()
        }
    )


app.include_router(receipt_router.router)

