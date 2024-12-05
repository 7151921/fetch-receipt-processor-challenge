import uuid
from unittest.mock import Mock, patch

from pydantic import ValidationError

from app.core.exceptions import NoReceiptData, NoReceiptId, ReceiptNotFound
from app.models.receipt import Receipt, ReceiptId, ReceiptRewards
from app.services.receipt_service import ReceiptService
from test.common.common import target_receipt, m_m_market_receipt, is_uuid
import pytest


@pytest.fixture
def receipt_service():
    return ReceiptService()


@pytest.fixture
async def processed_receipt_service(receipt_service: ReceiptService, target_receipt: Receipt):
    return await receipt_service.process_receipt(receipt=target_receipt)


@pytest.mark.asyncio
async def test_receipt_service_m_m_market(receipt_service: ReceiptService, m_m_market_receipt: Receipt):
    receipt_id = await receipt_service.process_receipt(receipt=m_m_market_receipt)
    assert isinstance(receipt_id, ReceiptId)
    assert is_uuid(receipt_id.receipt_id)


@pytest.mark.asyncio
async def test_receipt_service_no_data(receipt_service: ReceiptService):
    try:
        await receipt_service.process_receipt(receipt=None)
    except Exception as error:
        assert isinstance(error, NoReceiptData)


@pytest.mark.asyncio
async def test_receipt_service_get_target_points(receipt_service: ReceiptService, target_receipt: Receipt):
    receipt_id = await receipt_service.process_receipt(receipt=target_receipt)
    reward_points = await receipt_service.calculate_points_by_receipt_id(receipt_id=receipt_id)
    assert isinstance(reward_points, ReceiptRewards)
    assert reward_points.points == 28


@pytest.mark.asyncio
async def test_receipt_service_no_get_none_obj(receipt_service: ReceiptService):
    try:
        await receipt_service.calculate_points_by_receipt_id(receipt_id=None)
    except Exception as error:
        assert isinstance(error, NoReceiptId)


@pytest.mark.asyncio
async def test_receipt_service_no_get_target_id(receipt_service: ReceiptService):
    try:
        await receipt_service.calculate_points_by_receipt_id(receipt_id=ReceiptId(receipt_id=None))
    except Exception as error:
        assert isinstance(error, ValidationError)


@pytest.mark.asyncio
async def test_receipt_service_no_receipt_by_id(receipt_service: ReceiptService):
    try:
        receipt_id = str(uuid.uuid4())
        await receipt_service.calculate_points_by_receipt_id(receipt_id=ReceiptId(receipt_id=receipt_id))
    except Exception as error:
        assert isinstance(error, ReceiptNotFound)
