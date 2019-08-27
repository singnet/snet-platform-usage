import unittest

from services import APIUtilityService


class TestContractAPI(unittest.TestCase):
    def test_contract_api(self):
        self.assertEqual(
            APIUtilityService().get_user_address('m5FKWq4hW0foGW5qSbzGSjgZRuKs7A1ZwbIrJ9e96rc=', 0),
            '0xabd2cCb3828b4428bBde6C2031A865b0fb272a5A'
        )
