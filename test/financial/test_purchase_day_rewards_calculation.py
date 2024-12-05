import pytest

from app.financial.purchase_day_rewards_calculation import PurchaseDayRewardsCalculation
from app.models.receipt import Receipt
from test.common.common import target_receipt, m_m_market_receipt


@pytest.fixture
def reward_purchase_day_calculator_target(target_receipt: Receipt):
    return PurchaseDayRewardsCalculation(purchase_date=target_receipt.purchaseDate)


@pytest.fixture
def reward_purchase_day_calculator_m_m_market_receipt(m_m_market_receipt: Receipt):
    return PurchaseDayRewardsCalculation(purchase_date=m_m_market_receipt.purchaseDate)


def test_purchase_day_reward_calculation_data_type(reward_purchase_day_calculator_m_m_market_receipt:PurchaseDayRewardsCalculation):
    assert isinstance(reward_purchase_day_calculator_m_m_market_receipt.calculate_reward(), PurchaseDayRewardsCalculation)


def test_purchase_day_get_reward_data_type(reward_purchase_day_calculator_m_m_market_receipt: PurchaseDayRewardsCalculation):
    assert isinstance(reward_purchase_day_calculator_m_m_market_receipt.get_rewards(), int)


def test_purchase_day_get_reward_no_calculation(reward_purchase_day_calculator_m_m_market_receipt: PurchaseDayRewardsCalculation):
    assert reward_purchase_day_calculator_m_m_market_receipt.get_rewards() == 0


def test_purchase_day_m_m_rewards_calculator(reward_purchase_day_calculator_m_m_market_receipt: PurchaseDayRewardsCalculation):
    assert reward_purchase_day_calculator_m_m_market_receipt.calculate_reward().get_rewards() == 0


def test_purchase_day_target_rewards_calculator(reward_purchase_day_calculator_target: PurchaseDayRewardsCalculation):
    assert reward_purchase_day_calculator_target.calculate_reward().get_rewards() == 6
