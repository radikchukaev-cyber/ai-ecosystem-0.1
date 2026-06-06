import pytest
import tempfile
import shutil
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)

@pytest.fixture(scope="session")
def temp_workspace():
    """Provides a temporary workspace directory for testing."""
    workspace = tempfile.mkdtemp(prefix="test_workspace_")
    yield Path(workspace)
    shutil.rmtree(workspace)

@pytest.fixture
def mock_data_file(temp_workspace):
    """Creates a mock data file for testing file operations."""
    file_path = temp_workspace / "mock_data.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Sample test data for unit testing.\nLine 2.\n")
    yield file_path
    if file_path.exists():
        file_path.unlink()

@pytest.fixture
def api_base_url():
    """Returns a base URL for API testing."""
    return "http://localhost:8080/api/v1"
