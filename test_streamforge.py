# test_streamforge.py
"""
Tests for StreamForge module.
"""

import unittest
from streamforge import StreamForge

class TestStreamForge(unittest.TestCase):
    """Test cases for StreamForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StreamForge()
        self.assertIsInstance(instance, StreamForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StreamForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
