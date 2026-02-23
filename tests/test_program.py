from src.program import maxLenChainWithRandomDelete
import unittest

class TestMaxLenChain(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(maxLenChainWithRandomDelete([]), 0)
    
    def test_single_one(self):
        self.assertEqual(maxLenChainWithRandomDelete([1]), 0)
    
    def test_single_zero(self):
        self.assertEqual(maxLenChainWithRandomDelete([0]), 0)
    
    def test_all_ones(self):
        self.assertEqual(maxLenChainWithRandomDelete([1, 1, 1, 1]), 3)
    
    def test_all_zeros(self):
        self.assertEqual(maxLenChainWithRandomDelete([0, 0, 0, 0]), 0)
    
    def test_basic_case(self):
        self.assertEqual(maxLenChainWithRandomDelete([1, 1, 0, 1, 1, 1]), 5)
    
    def test_multiple_zeros(self):
        self.assertEqual(maxLenChainWithRandomDelete([1, 1, 0, 1, 0, 1, 1, 1]), 4)
    
    def test_zeros_at_edges(self):
        self.assertEqual(maxLenChainWithRandomDelete([0, 1, 1, 1, 0]), 3)
    
    def test_complex_pattern(self):
        self.assertEqual(maxLenChainWithRandomDelete([1, 1, 0, 0, 1, 1, 1, 0, 1, 1]), 5)
    
    def test_alternating_pattern(self):
        self.assertEqual(maxLenChainWithRandomDelete([1, 0, 1, 0, 1, 0, 1]), 2)
    
    def test_long_chain_at_end(self):
        self.assertEqual(maxLenChainWithRandomDelete([0, 1, 0, 1, 1, 1, 1, 1]), 6)
    
    def test_long_chain_at_start(self):
        self.assertEqual(maxLenChainWithRandomDelete([1, 1, 1, 1, 0, 1, 0]), 5)
    
    def test_multiple_opportunities(self):
        self.assertEqual(maxLenChainWithRandomDelete([1, 1, 0, 1, 1, 0, 1, 1, 1]), 6)
    
    def test_two_ones(self):
        self.assertEqual(maxLenChainWithRandomDelete([1, 1]), 1)
    
    def test_one_one_between_zeros(self):
        self.assertEqual(maxLenChainWithRandomDelete([0, 1, 0]), 1)
    
    def test_three_ones_between_zeros(self):
        self.assertEqual(maxLenChainWithRandomDelete([0, 1, 1, 1, 0]), 3)


if __name__ == '__main__':
    unittest.main()