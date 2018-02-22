"""Unit test for task.py"""
import unittest
import task


class Test(unittest.TestCase):
    """Unit test class"""
    def setUp(self):
        """Init"""

    def test_len_output(self):
        """Testing lenght(dict)"""
        self.assertEqual(len(task.structured_output), 7)

    def tearDown(self):
        """Finish"""


if __name__ == '__main__':
unittest.main()
