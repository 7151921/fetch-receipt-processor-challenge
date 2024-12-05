from app.financial.retailer_rewards_calculation import RetailerRewardsCalculation
from app.financial.rewards_calculation import RewardCalculation
import pytest

from app.models.receipt import Receipt
from test.common.common import target_receipt, m_m_market_receipt


@pytest.fixture
def reward_calculator_target_retailer(target_receipt: Receipt):
    return RetailerRewardsCalculation(retailer=target_receipt.retailer)


@pytest.fixture
def reward_calculator_m_m_market_retailer(m_m_market_receipt: Receipt):
    return RetailerRewardsCalculation(retailer=m_m_market_receipt.retailer)


def test_retailer_reward_calculation_data_type(reward_calculator_m_m_market_retailer: RetailerRewardsCalculation):
    assert isinstance(reward_calculator_m_m_market_retailer.calculate_reward(), RetailerRewardsCalculation)


def test_retailer_get_reward_data_type(reward_calculator_m_m_market_retailer: RetailerRewardsCalculation):
    assert isinstance(reward_calculator_m_m_market_retailer.get_rewards(), int)


def test_retailer_get_reward_no_calculation(reward_calculator_m_m_market_retailer: RetailerRewardsCalculation):
    assert reward_calculator_m_m_market_retailer.get_rewards() == 0


def test_m_m_rewards_calculator(reward_calculator_m_m_market_retailer: RetailerRewardsCalculation):
    assert reward_calculator_m_m_market_retailer.calculate_reward().get_rewards() == 14


def test_target_rewards_calculator(reward_calculator_target_retailer: RetailerRewardsCalculation):
    assert reward_calculator_target_retailer.calculate_reward().get_rewards() == 6
