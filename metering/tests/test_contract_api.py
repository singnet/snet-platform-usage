import unittest

from services import APIUtilityService


class TestContractAPI(unittest.TestCase):
    def test_contract_api(self):
        APIUtilityService().get_user_address('m5FKWq4hW0foGW5qSbzGSjgZRuKs7A1ZwbIrJ9e96rc=', 0)
