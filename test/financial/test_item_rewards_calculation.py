import pytest

from app.financial.items_rewards_calculation import ItemRewardsCalculation
from app.models.receipt import Receipt
from test.common.common import m_m_market_receipt, target_receipt


@pytest.fixture
def m_m_receipt_items_rewards(m_m_market_receipt: Receipt):
    return ItemRewardsCalculation(m_m_market_receipt.items)


@pytest.fixture
def target_items_rewards(target_receipt: Receipt):
    return ItemRewardsCalculation(target_receipt.items)


def test_item_reward_calculation_data_type(m_m_receipt_items_rewards: ItemRewardsCalculation):
    assert isinstance(m_m_receipt_items_rewards.calculate_reward(), ItemRewardsCalculation)


def test_item_get_reward_data_type(m_m_receipt_items_rewards: ItemRewardsCalculation):
    assert isinstance(m_m_receipt_items_rewards.get_rewards(), int)


def test_item_get_reward_no_calculation(m_m_receipt_items_rewards: ItemRewardsCalculation):
    assert m_m_receipt_items_rewards.get_rewards() == 0


def test_item_get_reward_with_calculation(m_m_receipt_items_rewards: ItemRewardsCalculation):
    assert m_m_receipt_items_rewards.calculate_reward().get_rewards() == 10


def test_target_receipt_short_description(target_items_rewards: ItemRewardsCalculation):
    assert target_items_rewards.calculate_reward().get_rewards() == 16
