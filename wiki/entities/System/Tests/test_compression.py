import pytest
import zlib
import gzip
from pathlib import Path

class TestDataCompression:
    """Tests data compression and decompression utilities."""

    def test_zlib_compression(self):
        """Tests standard zlib compression."""
        original_data = b"This is some sample data that needs to be compressed. " * 10
        compressed_data = zlib.compress(original_data)
        
        # Verify it actually compressed
        assert len(compressed_data) < len(original_data)
        
        # Verify decompression matches original
        decompressed_data = zlib.decompress(compressed_data)
        assert decompressed_data == original_data

    def test_gzip_file_compression(self, temp_workspace: Path):
        """Tests file-based gzip compression."""
        test_file = temp_workspace / "test.txt"
        gz_file = temp_workspace / "test.txt.gz"
        
        test_content = b"Data line 1\nData line 2\n" * 100
        test_file.write_bytes(test_content)
        
        # Compress
        with open(test_file, 'rb') as f_in:
            with gzip.open(gz_file, 'wb') as f_out:
                f_out.writelines(f_in)
                
        assert gz_file.exists()
        assert gz_file.stat().st_size < test_file.stat().st_size
        
        # Decompress and verify
        with gzip.open(gz_file, 'rb') as f_in:
            decompressed_content = f_in.read()
            
        assert decompressed_content == test_content
