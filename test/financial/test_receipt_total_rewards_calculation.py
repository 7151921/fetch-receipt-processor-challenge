from app.financial.receipt_total_rewards_calculation import ReceiptTotalRewardsCalculation
from app.financial.rewards_calculation import RewardCalculation
import pytest

from app.models.receipt import Receipt
from test.common.common import target_receipt, m_m_market_receipt


@pytest.fixture
def reward_calculator_target_total(target_receipt: Receipt):
    return ReceiptTotalRewardsCalculation(receipt_total=target_receipt.total)


@pytest.fixture
def reward_calculator_m_m_market_total(m_m_market_receipt: Receipt):
    return ReceiptTotalRewardsCalculation(receipt_total=m_m_market_receipt.total)


def test_total_reward_calculation_data_type(reward_calculator_m_m_market_total: ReceiptTotalRewardsCalculation):
    assert isinstance(reward_calculator_m_m_market_total.calculate_reward(), ReceiptTotalRewardsCalculation)


def test_total_get_reward_data_type(reward_calculator_m_m_market_total: ReceiptTotalRewardsCalculation):
    assert isinstance(reward_calculator_m_m_market_total.get_rewards(), int)


def test_total_get_reward_no_calculation(reward_calculator_m_m_market_total: ReceiptTotalRewardsCalculation):
    assert reward_calculator_m_m_market_total.get_rewards() == 0


def test_m_m_rewards_calculator(reward_calculator_m_m_market_total: ReceiptTotalRewardsCalculation):
    assert reward_calculator_m_m_market_total.calculate_reward().get_rewards() == 75


def test_target_rewards_calculator(reward_calculator_target_total: ReceiptTotalRewardsCalculation):
    assert reward_calculator_target_total.calculate_reward().get_rewards() == 0
