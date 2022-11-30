import unittest
from battle_royale import battle_royale

class TestBattleRoyale(unittest.TestCase):

    def test1(self):
        self.assertEqual(battle_royale([i for i in range(0, 10)]), [4, 4])


if __name__ == "__main__":
    unittest.main()