import uuid

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

from app.api.routes import receipt_router
from fastapi.testclient import TestClient

from test.common.common import target, is_uuid, target_with_bad_data

app = FastAPI(
    title="Test Receipt Processor",
    description="A simple test receipt processor",
    version="1.0.0"
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, rve: RequestValidationError):
    body = await request.json()
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={
            "detail": rve.errors(),
            "body": body
        }
    )

app.include_router(receipt_router.router)

client = TestClient(app)


def test_post_receipt():
    response = __create_receipt()
    json = response.json()
    assert response.status_code == 200
    assert "receipt_id" in json
    assert is_uuid(json.get("receipt_id"))


def test_post_bad_receipt():
    response = __create_bad_receipt()
    assert response.status_code == 400


def test_get_receipt():
    response = __create_receipt()
    json = response.json()
    response = client.get(f"/receipts/{json.get('receipt_id')}/points")
    assert response.status_code == 200
    assert response.json() == {'points': 28}


def test_get_bad_url_receipt():
    response = client.get("/receipts/%20/points")
    assert response.status_code == 400


def test_get_no_receipt():
    receipt_id = str(uuid.uuid4())
    response = client.get(f"/receipts/{receipt_id}/points")
    assert response.status_code == 400


def __create_receipt():
    return client.post("/receipts/process", json=target)


def __create_bad_receipt():
    return client.post("/receipts/process", json=target_with_bad_data)
