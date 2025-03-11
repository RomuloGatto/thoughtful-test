import unittest

from app import sort

class TestPackageSorting(unittest.TestCase):
    
    def test_standard_package(self):
        """Test for normal package (neither bulky nor heavy)."""
        self.assertEqual(sort(10.0, 10.0, 10.0, 5.0), "STANDARD")
    
    def test_bulky_package(self):
        """Test for a bulky package that is not heavy."""
        self.assertEqual(sort(200.0, 200.0, 5.0, 10.0), "SPECIAL")
    
    def test_heavy_package(self):
        """Test for a heavy package that is not bulky."""
        self.assertEqual(sort(50.0, 50.0, 50.0, 25.0), "SPECIAL")
    
    def test_bulky_and_heavy_package(self):
        """Test for a package that is both bulky and heavy (should be rejected)."""
        self.assertEqual(sort(200.0, 200.0, 200.0, 30.0), "REJECTED")
    
    def test_invalid_negative_dimension(self):
        """Test for a package with a negative dimension."""
        self.assertEqual(sort(-1.0, 50.0, 50.0, 25.0), "INVALID")
    
    def test_invalid_zero_dimension(self):
        """Test for a package with a zero dimension."""
        self.assertEqual(sort(0.0, 50.0, 50.0, 25.0), "INVALID")
    
    def test_invalid_negative_mass(self):
        """Test for a package with negative mass."""
        self.assertEqual(sort(50.0, 50.0, 50.0, -5.0), "INVALID")
    
    def test_invalid_zero_mass(self):
        """Test for a package with zero mass."""
        self.assertEqual(sort(50.0, 50.0, 50.0, 0.0), "INVALID")
    
    def test_edge_case_bulky_but_not_heavy(self):
        """Test for a bulky package with volume but low mass."""
        self.assertEqual(sort(200.0, 200.0, 200.0, 5.0), "SPECIAL")
    
    def test_edge_case_heavy_but_not_bulky(self):
        """Test for a heavy package with low volume."""
        self.assertEqual(sort(10.0, 10.0, 10.0, 25.0), "SPECIAL")
