import pytest
from typing import Dict, Any

class DecisionEngine:
    """Mock decision engine for testing."""
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> str:
        if context.get("cpu_usage", 0) > 90:
            return "SCALE_UP"
        elif context.get("error_rate", 0) > 0.05:
            return "ALERT"
        elif context.get("queue_length", 0) == 0:
            return "SCALE_DOWN"
        return "IDLE"

class TestDecisionMaking:
    """Tests the logic of the system's decision engine."""

    def test_scale_up_decision(self):
        """Tests if high CPU triggers a scale up."""
        context = {"cpu_usage": 95.5, "error_rate": 0.01}
        decision = DecisionEngine.evaluate(context)
        assert decision == "SCALE_UP"

    def test_alert_decision(self):
        """Tests if high error rate triggers an alert."""
        context = {"cpu_usage": 50, "error_rate": 0.08}
        decision = DecisionEngine.evaluate(context)
        assert decision == "ALERT"

    def test_scale_down_decision(self):
        """Tests if empty queue triggers a scale down."""
        context = {"cpu_usage": 10, "error_rate": 0.0, "queue_length": 0}
        decision = DecisionEngine.evaluate(context)
        assert decision == "SCALE_DOWN"

    def test_idle_decision(self):
        """Tests normal operating conditions."""
        context = {"cpu_usage": 45, "error_rate": 0.01, "queue_length": 10}
        decision = DecisionEngine.evaluate(context)
        assert decision == "IDLE"
