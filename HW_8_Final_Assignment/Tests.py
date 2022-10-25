import unittest
from HW8 import *


class Test(unittest.TestCase):
    def test_monom_create(self):
        m1 = Monom(6, 2)
        self.assertEqual(m1.power, 6)
        self.assertEqual(m1.coef, 2)
        m1 = Monom(0, 2.314)
        self.assertEqual(m1.power, 0)
        self.assertEqual(m1.coef, 2.31)

    def test_monom_repr(self):
        m1 = Monom(6, 2)
        m2 = Monom(8)
        m3 = Monom(0, 19.5)
        m4 = Monom(1, 5)
        m5 = Monom(8, 1.0)
        m6 = Monom(8, 0)
        m7 = Monom(4, 31.000)
        m8 = Monom(0, 1)
        m9 = Monom(4, 31.00124)
        m10 = Monom(4, 31.1111111)
        m11 = Monom(3, -1)
        m12 = Monom(2, -14)
        m13 = Monom(1, -5)
        m14 = Monom(0, -5)
        self.assertEqual(str(m1), '2X^6')
        self.assertEqual(str(m2), 'X^8')
        self.assertEqual(str(m3), '19.5')
        self.assertEqual(str(m4), '5X')
        self.assertEqual(str(m5), 'X^8')
        self.assertEqual(str(m6), '0')
        self.assertEqual(str(m7), '31X^4')
        self.assertEqual(str(m8), '1')
        self.assertEqual(str(m9), '31X^4')
        self.assertEqual(str(m10), '31.11X^4')
        self.assertEqual(str(m11), '(-1X^3)')
        self.assertEqual(str(m12), '(-14X^2)')
        self.assertEqual(str(m13), '(-5X)')
        self.assertEqual(str(m14), '(-5)')

    def test_monom_mul(self):
        m1 = Monom(6, 2)
        m2 = m1 * 3.5
        m3 = m1 * 4
        m4 = 2.1 * m1
        m5 = 4 * m1
        m6 = m5 * m1
        self.assertEqual(m2.coef, 7)
        self.assertEqual(m2.power, 6)
        self.assertEqual(m3.coef, 8)
        self.assertEqual(m3.power, 6)
        self.assertEqual(m4.coef, 4.2)
        self.assertEqual(m4.power, 6)
        self.assertEqual(m5.coef, 8)
        self.assertEqual(m5.power, 6)
        self.assertEqual(m6.coef, 16)
        self.assertEqual(m6.power, 12)
        self.assertEqual(m1.coef, 2)
        self.assertEqual(m1.power, 6)
        self.assertEqual(m5.coef, 8)
        self.assertEqual(m5.power, 6)

    def test_monom_derivative(self):
        m1 = Monom(5, 5)
        m2 = Monom(1, 5)
        m3 = Monom(5, 1)
        m4 = Monom(0, 10)
        m5 = Monom(12, 0)
        m6 = Monom(2, 3.542)
        self.assertEqual(str(m1.derivative()), '25X^4')
        self.assertEqual(str(m2.derivative()), '5')
        self.assertEqual(str(m3.derivative()), '5X^4')
        self.assertEqual(str(m4.derivative()), '0')
        self.assertEqual(str(m5.derivative()), '0')
        self.assertEqual(str(m6.derivative()), '7.08X')
        self.assertEqual(m1.power, 5)
        self.assertEqual(m1.coef, 5)

    def test_monom_integral(self):
        m1 = Monom(4, 5)
        m2 = Monom(0, 5)
        m3 = Monom(4, 0)
        m4 = Monom(0, 1)
        m5 = Monom(5, 5)
        m6 = Monom(3, 7)
        self.assertEqual(str(m1.integral()), 'X^5')
        self.assertEqual(str(m2.integral()), '5X')
        self.assertEqual(str(m3.integral()), '0')
        self.assertEqual(str(m4.integral()), 'X')
        self.assertEqual(str(m5.derivative().integral()), '5X^5')
        self.assertEqual(str(m6.integral()), '1.75X^4')

    def test_polynom_create(self):
        poly1 = Polynomial([])
        poly2 = Polynomial([(0, 2), (4, 4), (3, 3), (1, 1)])
        poly3 = Polynomial([(0, 2), (4, 4), (3, 3), (1, 1), (4, 1)])
        poly4 = Polynomial([(0, 2), (4, 4), (3, 3), (1, 1), (4, -4), (15, 0)])

        curr = poly1.head
        self.assertTrue(curr is None)
        curr = poly2.head
        self.assertEqual(str(curr), '4X^4')
        curr = curr.next
        self.assertEqual(str(curr), '3X^3')
        curr = curr.next
        self.assertEqual(str(curr), 'X')
        curr = curr.next
        self.assertEqual(str(curr), '2')
        curr = curr.next
        self.assertTrue(curr is None)

        curr = poly3.head
        self.assertEqual(str(curr), '5X^4')
        curr = curr.next
        self.assertEqual(str(curr), '3X^3')
        curr = curr.next
        self.assertEqual(str(curr), 'X')
        curr = curr.next
        self.assertEqual(str(curr), '2')
        curr = curr.next
        self.assertTrue(curr is None)

        curr = poly4.head
        self.assertEqual(str(curr), '3X^3')
        curr = curr.next
        self.assertEqual(str(curr), 'X')
        curr = curr.next
        self.assertEqual(str(curr), '2')
        curr = curr.next
        self.assertTrue(curr is None)

    def test_polynom_illegal_create(self):
        with self.assertRaises(ValueError):
            Polynomial(2)
        with self.assertRaises(ValueError):
            Polynomial((3))
        with self.assertRaises(ValueError):
            Polynomial([3])
        with self.assertRaises(ValueError):
            Polynomial(['tree', (2, 5)])
        with self.assertRaises(ValueError):
            Polynomial([(2, 5), (2)])
        with self.assertRaises(ValueError):
            Polynomial([(2, 5), (3, 3.0, 1)])
        with self.assertRaises(ValueError):
            Polynomial([(2, 5), 2])

    def test_polynom_repr(self):
        poly1 = Polynomial([])
        poly2 = Polynomial([(2, 0)])
        poly3 = Polynomial([(2, 0), (4, 4), (6, 3), (1, 6), (2, 5), (3, 13)])
        poly4 = Polynomial([(2, 0), (4, 4), (6, 3), (1, 6), (2, 5), (0, 1)])
        poly5 = Polynomial([(2, 0), (4, 4), (6, 3), (1, 6), (1, -6), (0, 2)])
        poly6 = Polynomial([(2, 0), (4, -4), (6, 1), (1, -6), (2, 5), (3, -13)])

        self.assertEqual(str(poly1), 'P(X)=0')
        self.assertEqual(str(poly2), 'P(X)=0')
        self.assertEqual(str(poly3), 'P(X)=3X^6+4X^4+13X^3+5X^2+6X')
        self.assertEqual(str(poly4), 'P(X)=3X^6+4X^4+5X^2+6X+1')
        self.assertEqual(str(poly5), 'P(X)=3X^6+4X^4+2')
        self.assertEqual(str(poly6), 'P(X)=X^6+(-4X^4)+(-13X^3)+5X^2+(-6X)')

    def test_polynom_rank(self):
        poly1 = Polynomial([])
        poly2 = Polynomial([(2, 2)])
        poly3 = Polynomial([(2, 2), (1, 2), (5, 2), (3, 2)])
        poly4 = Polynomial([(2, 0)])
        poly5 = Polynomial([(2, 2), (1, 2), (5, 0), (3, 2)])
        self.assertEqual(poly1.rank(), 0)
        self.assertEqual(poly2.rank(), 2)
        self.assertEqual(poly3.rank(), 5)
        self.assertEqual(poly4.rank(), 0)
        self.assertEqual(poly5.rank(), 3)

    def test_polynom_calculate_value(self):
        poly1 = Polynomial([])
        poly2 = Polynomial([(0, 2), (4, 4), (3, 3), (1, 1)])
        poly3 = Polynomial([(0, 2), (4, 4), (3, 3), (1, 1), (4, 1)])
        poly4 = Polynomial([(0, 2), (4, 4), (3, 3), (1, 1), (4, -4)])
        poly5 = Polynomial([(4, 4), (3, 3), (1, 1), (4, -4)])

        self.assertEqual(poly1.calculate_value(14), 0)
        self.assertEqual(poly2.calculate_value(1), 10)
        self.assertEqual(poly2.calculate_value(0), 2)
        self.assertEqual(poly3.calculate_value(5), 3507)
        self.assertEqual(poly4.calculate_value(3), 86)
        self.assertEqual(poly5.calculate_value(0), 0)

    def test_polynom_neg(self):
        poly1 = Polynomial([])
        poly2 = Polynomial([(2, 0)])
        poly3 = Polynomial([(2, 0), (4, 4), (6, 3), (1, 6), (2, 5), (3, 13)])
        poly4 = Polynomial([(2, 0), (4, 4), (6, 3), (1, 6), (2, 5), (0, 1)])
        poly5 = Polynomial([(2, 0), (4, 4), (6, 3), (1, 6), (1, -6), (0, 2)])
        poly6 = Polynomial([(2, 0), (4, -4), (6, 1), (1, -6), (2, 5), (3, -13)])

        poly1 = -poly1
        poly2 = -poly2
        poly3 = -poly3
        poly4 = -poly4
        poly5 = -poly5
        poly7 = -poly6

        self.assertEqual(str(poly1), 'P(X)=0')
        self.assertEqual(str(poly2), 'P(X)=0')
        self.assertEqual(str(poly3), 'P(X)=(-3X^6)+(-4X^4)+(-13X^3)+(-5X^2)+(-6X)')
        self.assertEqual(str(poly4), 'P(X)=(-3X^6)+(-4X^4)+(-5X^2)+(-6X)+(-1)')
        self.assertEqual(str(poly5), 'P(X)=(-3X^6)+(-4X^4)+(-2)')
        self.assertEqual(str(poly7), 'P(X)=(-1X^6)+4X^4+13X^3+(-5X^2)+6X')
        self.assertEqual(str(poly6), 'P(X)=X^6+(-4X^4)+(-13X^3)+5X^2+(-6X)')

    def test_polynom_sub(self):
        poly1 = Polynomial([])
        poly2 = Polynomial([(2, 0)])
        poly3 = Polynomial([(2, 0), (4, 4), (6, 3), (1, 6), (2, 5), (3, 13)])
        poly4 = Polynomial([(2, 0), (4, 4), (6, 3), (1, 6), (2, 5), (0, 1)])
        poly5 = Polynomial([(2, 0), (4, 4), (6, 3), (1, 6), (1, -6), (0, 2)])
        poly6 = Polynomial([(2, 0), (4, -4), (6, 3), (1, -6), (2, 5), (3, -13)])

        self.assertEqual(str(poly1 - poly2), 'P(X)=0')
        self.assertEqual(str(poly1 - poly3), str(-poly3))
        self.assertEqual(str(poly4 - poly1), str(poly4))
        self.assertEqual(str(poly4 - poly4), 'P(X)=0')
        self.assertEqual(str(poly3 - poly4), 'P(X)=13X^3+(-1)')
        self.assertEqual(str(poly4 - poly5), 'P(X)=5X^2+6X+(-1)')
        self.assertEqual(str(poly5 - poly6), 'P(X)=8X^4+13X^3+(-5X^2)+6X+2')

    def test_polynom_mul(self):
        poly1 = Polynomial([])
        poly2 = Polynomial([(4, 4), (6, 3), (1, 6), (2, 5), (3, 13)])
        poly3 = Polynomial([(4, 4), (6, 3), (1, 6), (2, 5), (0, 1)])
        poly4 = Polynomial([(5, 5), (3, 3), (0, 2)])

        self.assertEqual(str(poly1 * 4), 'P(X)=0')
        self.assertEqual(str(4 * poly1), 'P(X)=0')
        self.assertEqual(str(poly4 * 0), 'P(X)=0')
        self.assertEqual(str(0 * poly4), 'P(X)=0')
        self.assertEqual(str(poly2 * 2), 'P(X)=6X^6+8X^4+26X^3+10X^2+12X')
        self.assertEqual(str(2 * poly2), 'P(X)=6X^6+8X^4+26X^3+10X^2+12X')
        self.assertEqual(str(poly2 * 1), str(poly2))
        self.assertEqual(str(1 * poly2), str(poly2))
        self.assertEqual(str(poly2 * 1.5), 'P(X)=4.5X^6+6X^4+19.5X^3+7.5X^2+9X')
        self.assertEqual(str(1.5 * poly2), 'P(X)=4.5X^6+6X^4+19.5X^3+7.5X^2+9X')
        self.assertEqual(str(poly2 * -1), str(-poly2))
        self.assertEqual(str(-1 * poly2), str(-poly2))
        self.assertEqual(str(poly3 * poly4), 'P(X)=15X^11+29X^9+37X^7+36X^6+20X^5+26X^4+3X^3+10X^2+12X+2')
        self.assertEqual(str(poly4 * poly3), 'P(X)=15X^11+29X^9+37X^7+36X^6+20X^5+26X^4+3X^3+10X^2+12X+2')

    def test_polynom_derivative(self):
        poly1 = Polynomial([])
        poly2 = Polynomial([(1, 4)])
        poly3 = Polynomial([(0, 4)])
        poly4 = Polynomial([(4, 4), (6, 3), (1, 6), (2, 5), (3, 13)])
        poly5 = Polynomial([(4, 4), (6, -3), (1, 6), (2, -5), (0, -1)])

        self.assertEqual(str(poly1.derivative()), 'P(X)=0')
        self.assertEqual(str(poly2.derivative()), 'P(X)=4')
        self.assertEqual(str(poly3.derivative()), 'P(X)=0')
        self.assertEqual(str(poly4.derivative()), 'P(X)=18X^5+16X^3+39X^2+10X+6')
        self.assertEqual(str(poly5.derivative()), 'P(X)=(-18X^5)+16X^3+(-10X)+6')

    def test_polynom_integral(self):
        poly1 = Polynomial([])
        poly2 = Polynomial([(1, 4)])
        poly3 = Polynomial([(0, 4)])
        poly4 = Polynomial([(4, 4), (6, 3), (1, 6), (2, 5), (3, 13)])
        poly5 = Polynomial([(4, 4), (6, -3), (1, 6), (2, -5), (0, -1)])

        self.assertEqual(str(poly1.integral()), 'P(X)=0')
        self.assertEqual(str(poly2.integral()), 'P(X)=2X^2')
        self.assertEqual(str(poly3.integral(15)), 'P(X)=4X+15')
        self.assertEqual(str(poly4.integral(-6)), 'P(X)=0.43X^7+0.8X^5+3.25X^4+1.67X^3+3X^2+(-6)')
        self.assertEqual(str(poly5.integral()), 'P(X)=(-0.43X^7)+0.8X^5+(-1.67X^3)+3X^2+(-1X)')

    def test_polynom_equals(self):
        poly1 = Polynomial([])
        poly2 = Polynomial([(2, 0)])
        poly3 = Polynomial([(4, 3)])
        poly4 = Polynomial([(3, 4)])
        poly5 = Polynomial([(4, 2)])
        poly6 = Polynomial([(4, 3), (3, 2)])
        poly7 = Polynomial([(4, 3), (2, 2)])
        poly8 = Polynomial([(4, 3), (3, 2), (2, 2)])
        poly9 = Polynomial([(4, 3), (3, 2), (1, 2)])

        self.assertTrue(poly1 == poly2)
        self.assertFalse(poly3 == poly2)
        self.assertFalse(poly3 == poly1)
        self.assertTrue(poly3 > poly2)
        self.assertTrue(poly3 >= poly2)
        self.assertTrue(poly1 != poly3)
        self.assertTrue(poly4 <= poly3)
        self.assertTrue(poly4 < poly3)
        self.assertTrue(poly3 > poly5)
        self.assertTrue(poly5 <= poly3)
        self.assertTrue(poly3 < poly6)
        self.assertTrue(poly6 != poly7)
        self.assertTrue(poly3 < poly6)
        self.assertTrue(poly7 < poly6)
        self.assertTrue(poly7 < poly8)
        self.assertTrue(poly8 > poly9)
        self.assertTrue(poly9 > poly6)

    def test_BST_all(self):
        p1 = Polynomial([(1, 2), (2, 1), (5, 6), (6, 5), (1, 2), (2, 1)])
        p2 = Polynomial([])
        p3 = Polynomial([(8, 0), (3, -5), (3, 5), (0, 18)])
        p4 = Polynomial([(1, 1), (2, 2), (3, 3)])
        p5 = Polynomial([(1, 4), (2, 5), (3, 6)])
        p6 = Polynomial([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])
        p7 = Polynomial([(1, -1), (2, -2), (3, 3), (4, -4), (5, -5), (6, -6)])
        p8 = Polynomial([(1, 4), (2, 5), (3, 6)])
        p9 = Polynomial([(1, 4), (2, 5), (3, 6)])
        p10 = Polynomial([(1, 4.1), (2, 5), (3, 6)])
        p11 = Polynomial([(4, 5)])
        t1 = PolynomialBST()
        t1.insert(p1)
        t1.insert(p2)
        t1.insert(p3)
        t1.insert(p4)
        t1.insert(p5)
        order1 = t1.in_order()
        order1 = [str(order) for order in order1]
        self.assertEqual(order1,
                         ['P(X)=0', 'P(X)=18', 'P(X)=3X^3+2X^2+X', 'P(X)=6X^3+5X^2+4X', 'P(X)=5X^6+6X^5+2X^2+4X'])
        t2 = PolynomialBST()
        order2 = t2.in_order()
        order2 = [str(order) for order in order2]
        self.assertEqual(order2, [])
        t2.insert(p6)
        t2.insert(p7)
        t2.insert(p8)
        t2.insert(p9)
        t2.insert(p10)
        t2.insert(p11)
        order3 = t2.in_order()
        order3 = [str(order) for order in order3]
        self.assertEqual(order3, ['P(X)=6X^3+5X^2+4X', 'P(X)=6X^3+5X^2+4X',
                                  'P(X)=6X^3+5X^2+4.1X', 'P(X)=5X^4',
                                  'P(X)=(-6X^6)+(-5X^5)+(-4X^4)+3X^3+(-2X^2)+(-1X)',
                                  'P(X)=6X^6+5X^5+4X^4+3X^3+2X^2+X'])
        t3 = t1 + t2
        order4 = t3.in_order()
        order4 = [str(order) for order in order4]
        self.assertEqual(order4, ['P(X)=0', 'P(X)=18', 'P(X)=3X^3+2X^2+X', 'P(X)=6X^3+5X^2+4X',
                                  'P(X)=6X^3+5X^2+4X', 'P(X)=6X^3+5X^2+4X', 'P(X)=6X^3+5X^2+4.1X', 'P(X)=5X^4',
                                  'P(X)=(-6X^6)+(-5X^5)+(-4X^4)+3X^3+(-2X^2)+(-1X)', 'P(X)=5X^6+6X^5+2X^2+4X',
                                  'P(X)=6X^6+5X^5+4X^4+3X^3+2X^2+X'])


if __name__ == "__main__":
    unittest.main()
