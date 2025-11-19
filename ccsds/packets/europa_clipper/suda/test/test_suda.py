import os
import unittest

from spac_kit.parser import compare


class TestSudaCase:
    def test_parse(self):
        local_dir = os.path.dirname(__file__)
        compare(local_dir, False, True, False, create_output=False)


if __name__ == "__main__":
    unittest.main()
