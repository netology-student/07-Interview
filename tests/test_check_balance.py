
import unittest
from parameterized import parameterized
from main import check_balance



class TestFunctions(unittest.TestCase):

    # Пример сбалансированных последовательностей скобок:
    #
    # (((([{}]))))
    # [([])((([[[]]])))]
    # {()}
    # {{[()]}}
    #
    # Несбалансированные последовательности:
    #
    # }{}
    # {{[(])]}}
    # [[{())}]
    #
    @parameterized.expand(
        [
            ("(((([{}]))))", True),
            ("[([])((([[[]]])))]", True),
            ("{()}", True),
            ("{{[()]}}", True),
            ("}{}", False),
            ("{{[(])]}}", False),
            ("[[{())}]", False)
        ]
    )
    def test_check_balance(self, target_string, result):
        self.assertEqual(check_balance(target_string), result)