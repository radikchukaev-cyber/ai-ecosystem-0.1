import pytest
import os
from pathlib import Path
import sys

# Add parent dir to path to allow importing the scripts
sys.path.append(str(Path(__file__).parent.parent))
from Scripts.backup_manager import BackupManager
from Scripts.rollback_automation import RollbackManager

class TestBackupAndRecovery:
    """Tests the backup and rollback mechanics."""

    def test_backup_creation(self, temp_workspace: Path, mock_data_file: Path):
        """Tests if a backup is created successfully."""
        source_dir = temp_workspace / "source"
        source_dir.mkdir(exist_ok=True)
        backup_dir = temp_workspace / "backups"
        
        # Copy mock file to source
        import shutil
        target_file = source_dir / mock_data_file.name
        shutil.copy(mock_data_file, target_file)

        manager = BackupManager(str(source_dir), str(backup_dir))
        success = manager.create_backup()
        
        assert success is True
        assert backup_dir.exists()
        
        # Verify backup contents
        backups = list(backup_dir.glob("backup_*"))
        assert len(backups) == 1
        assert (backups[0] / mock_data_file.name).exists()

    def test_rollback_execution(self, temp_workspace: Path):
        """Tests if rollback restores the exact state."""
        source_dir = temp_workspace / "source2"
        backup_dir = temp_workspace / "backups2"
        source_dir.mkdir(exist_ok=True)
        
        # Create initial state
        (source_dir / "file.txt").write_text("initial")
        
        # Backup
        bm = BackupManager(str(source_dir), str(backup_dir))
        bm.create_backup()
        
        # Modify state
        (source_dir / "file.txt").write_text("modified")
        
        # Rollback
        rm = RollbackManager(str(source_dir), str(backup_dir))
        success = rm.execute_rollback()
        
        assert success is True
        assert (source_dir / "file.txt").read_text() == "initial"
