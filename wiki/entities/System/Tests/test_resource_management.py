import pytest

class ResourceManager:
    """Mock resource manager."""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.allocated = 0

    def allocate(self, amount: int) -> bool:
        if self.allocated + amount <= self.capacity:
            self.allocated += amount
            return True
        return False

    def release(self, amount: int):
        self.allocated = max(0, self.allocated - amount)

class TestResourceManagement:
    """Tests the allocation and release of system resources."""

    def test_allocation_success(self):
        """Tests successful resource allocation."""
        rm = ResourceManager(capacity=100)
        assert rm.allocate(50) is True
        assert rm.allocated == 50

    def test_allocation_failure(self):
        """Tests failed resource allocation due to limits."""
        rm = ResourceManager(capacity=100)
        assert rm.allocate(150) is False
        assert rm.allocated == 0

    def test_release_resources(self):
        """Tests releasing allocated resources."""
        rm = ResourceManager(capacity=100)
        rm.allocate(60)
        rm.release(20)
        assert rm.allocated == 40

    def test_release_below_zero(self):
        """Tests that releasing more than allocated doesn't go below zero."""
        rm = ResourceManager(capacity=100)
        rm.allocate(30)
        rm.release(50)
        assert rm.allocated == 0
