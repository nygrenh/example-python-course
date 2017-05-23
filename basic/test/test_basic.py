import unittest
from unittest.mock import patch

from tmc import points

from tmc.utils import load, get_stdout
main = load('src.basic', 'main')


@points('1.0')
class BasicTest(unittest.TestCase):

    def test_prints_correct_sum(self):
        self.longMessage = False
        main()
        printed = get_stdout()
        if not printed:
            self.fail('Et tulostanut mitään!')
        self.assertEqual(printed, '5050', msg='Tulostuksesi ei ollut sadan ensimmäisen kokonaisluvun summa.')
