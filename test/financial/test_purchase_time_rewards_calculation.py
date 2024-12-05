from app.financial.purchase_time_rewards_calculation import PurchaseTimeRewardsCalculation
import pytest

from app.models.receipt import Receipt
from test.common.common import target_receipt, m_m_market_receipt


@pytest.fixture
def reward_calculator_target_purchase_time(target_receipt: Receipt):
    return PurchaseTimeRewardsCalculation(purchase_time=target_receipt.purchaseTime)


@pytest.fixture
def reward_calculator_m_m_market_purchase_time(m_m_market_receipt: Receipt):
    return PurchaseTimeRewardsCalculation(purchase_time=m_m_market_receipt.purchaseTime)


def test_purchase_time_reward_calculation_data_type(reward_calculator_m_m_market_purchase_time: PurchaseTimeRewardsCalculation):
    assert isinstance(reward_calculator_m_m_market_purchase_time.calculate_reward(), PurchaseTimeRewardsCalculation)


def test_purchase_time_get_reward_data_type(reward_calculator_m_m_market_purchase_time: PurchaseTimeRewardsCalculation):
    assert isinstance(reward_calculator_m_m_market_purchase_time.get_rewards(), int)


def test_purchase_time_get_reward_no_calculation(reward_calculator_m_m_market_purchase_time: PurchaseTimeRewardsCalculation):
    assert reward_calculator_m_m_market_purchase_time.get_rewards() == 0


def test_m_m_rewards_calculator(reward_calculator_m_m_market_purchase_time: PurchaseTimeRewardsCalculation):
    assert reward_calculator_m_m_market_purchase_time.calculate_reward().get_rewards() == 10


def test_target_rewards_calculator(reward_calculator_target_purchase_time: PurchaseTimeRewardsCalculation):
    assert reward_calculator_target_purchase_time.calculate_reward().get_rewards() == 0
