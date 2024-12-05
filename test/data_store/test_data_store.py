from uuid import UUID

from app.core.exceptions import NoReceiptData
from app.data_store.receipt_data_store import ReceiptDataStore
from app.models.receipt import Receipt
from test.common.common import target_receipt, m_m_market_receipt, is_uuid
import pytest


@pytest.fixture
def data_store():
    return ReceiptDataStore()


@pytest.mark.asyncio
async def test_insert_data_store(data_store: ReceiptDataStore, target_receipt: Receipt):
    receipt_id = await data_store.store_receipt(data=target_receipt)
    assert receipt_id is not None
    assert isinstance(receipt_id, str)
    assert is_uuid(receipt_id)


@pytest.mark.asyncio
async def test_insert_data_store_none(data_store: ReceiptDataStore):
    try:
        await data_store.store_receipt(data=None)
    except Exception as error:
        assert isinstance(error, NoReceiptData)


@pytest.mark.asyncio
async def test_get_receipt(data_store: ReceiptDataStore, target_receipt: Receipt):
    receipt_id = await data_store.store_receipt(data=target_receipt)
    data = await data_store.get_receipt(receipt_id)
    assert data is not None
    assert isinstance(data, Receipt)
    assert data.__dict__ == target_receipt.__dict__


@pytest.mark.asyncio
async def test_get_no_receipt(data_store: ReceiptDataStore):
    data = await data_store.get_receipt("some_bad_value")
    assert data is None


@pytest.mark.asyncio
async def test_delete_receipt(data_store: ReceiptDataStore, target_receipt: Receipt):
    receipt_id = await data_store.store_receipt(data=target_receipt)
    has_been_deleted = await data_store.delete_receipt(receipt_id)
    assert has_been_deleted


@pytest.mark.asyncio
async def test_update_receipt(data_store: ReceiptDataStore, target_receipt: Receipt, m_m_market_receipt: Receipt):
    receipt_id = await data_store.store_receipt(data=target_receipt)
    has_been_updated = await data_store.update_receipt(receipt_id=receipt_id, data=m_m_market_receipt)
    assert has_been_updated


@pytest.mark.asyncio
async def test_update_receipt_no_value_to_update(data_store: ReceiptDataStore, m_m_market_receipt: Receipt):
    has_been_updated = await data_store.update_receipt(receipt_id="some_bad_value", data=m_m_market_receipt)
    assert not has_been_updated


@pytest.mark.asyncio
async def test_update_receipt_none(data_store: ReceiptDataStore, target_receipt: Receipt):
    try:
        receipt_id = await data_store.store_receipt(data=target_receipt)
        await data_store.update_receipt(receipt_id=receipt_id, data=None)
    except Exception as error:
        assert isinstance(error, ValueError)


@pytest.mark.asyncio
async def test_delete_receipt_nothing_to_delete(data_store: ReceiptDataStore):
    has_been_deleted = await data_store.delete_receipt("some_bad_value")
    assert not has_been_deleted


@pytest.mark.asyncio
async def test_list_store_none(data_store: ReceiptDataStore):
    empty_data_store = await data_store.list_all_receipts()
    assert empty_data_store == {}
    assert len(empty_data_store) == 0


@pytest.mark.asyncio
async def test_list_store(data_store: ReceiptDataStore, target_receipt: Receipt):
    receipt_id = await data_store.store_receipt(data=target_receipt)
    data_store = await data_store.list_all_receipts()
    assert receipt_id in data_store
    assert len(data_store) == 1
