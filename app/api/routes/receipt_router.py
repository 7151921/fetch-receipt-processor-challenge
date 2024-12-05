import logging
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from app.core.exceptions import NoReceiptData, NoReceiptId, ReceiptNotFound
from app.models.receipt import Receipt, ReceiptId
from app.services.receipt_service import ReceiptService

router = APIRouter()

receipt_service = ReceiptService()


@router.post("/receipts/process")
async def process_receipt(receipt: Receipt):
    try:
        logging.info(f"Received receipt at {datetime.now(timezone.utc)} attempting to process.")
        return await receipt_service.process_receipt(receipt=receipt)
    except NoReceiptData as e:
        raise HTTPException(status_code=400, detail=str(e))
    except NoReceiptId as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/receipts/{_id}/points")
async def calculate_points_by_receipt_id(_id: str):
    try:
        receipt_id = ReceiptId(receipt_id=_id)
        return await receipt_service.calculate_points_by_receipt_id(receipt_id=receipt_id)
    except ReceiptNotFound as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
