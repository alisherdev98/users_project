import unittest
from threading import get_native_id


def get_nds(a, b):
    result = a * b + a ** b + 14
    return result

def get_osms(a, b, c):
    return (a + b + c) * a / b

def raschet_zp(a, b, c):
    nds = get_nds(a, b)



    osms = get_osms(a, b, c)

    return nds + osms


class TestNDSGetting(unittest.TestCase):
    def setUp(self):
        self.results = [28, 22]
        print('Hello!')
        print('testing')


    def test_get_nds(self):
        result = get_nds(2, 3)

        self.assertEqual(result, 28)

    def test_get_nds2(self):
        result = get_nds(2, 2)

        self.assertEqual(result, 22)
