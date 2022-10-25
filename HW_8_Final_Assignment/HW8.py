import copy
from functools import total_ordering


@total_ordering
class Monom:
    def __init__(self, power: float, coef=1.0):
        self.power = power
        self.coef = round(coef, 2)
        self.next = None

    def __repr__(self):
        s = ''
        if self.coef == 1 and self.power == 0:
            return '1'
        if self.coef == 0:
            return '0'
        if self.coef != 1:
            if self.coef - int(self.coef) == 0:
                s += str(int(self.coef))
            else:
                s += str(self.coef)
        if self.power != 0:
            s += 'X'
            if self.power != 1:
                s += '^' + str(self.power)
        if self.coef < 0:
            return '(' + s + ')'
        return s

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Monom(self.power, self.coef * other)
        elif isinstance(other, Monom):
            return Monom(self.power + other.power, self.coef * other.coef)
        raise TypeError("Multiplication only with Scalar or Monom")

    def __rmul__(self, other):
        return self * other

    def derivative(self):
        if self.power == 0:
            return Monom(0, 0)
        return Monom(self.power - 1, self.coef * self.power)

    def integral(self):
        return Monom(self.power + 1, self.coef / (self.power + 1))

    def __eq__(self, other):
        return other is not None and self.power == other.power and self.coef == other.coef

    def __gt__(self, other):
        return self.power > other.power or (self.power == other.power and self.coef > other.coef)


# print("=" * 20 + "\nDefine Monom\n" + "=" * 20)
# m1 = Monom(6, 2)
# m2 = Monom(8)
# m3 = Monom(0, 19.5)
# m4 = Monom(1, 5)
# m5 = Monom(8, -4.0)
# m6 = Monom(8, 0)
# print('m1-m6:')
# print('m1:', m1)
# print('m2:', m2)
# print('m3:', m3)
# print('m4:', m4)
# print('m5:', m5)
# print('m6:', m6)
#
# print("\n" + "=" * 20 + "\nMultiples Monoms\n" + "=" * 20)
# m7 = m1 * 3.5
# m8 = 4 * m1
# m9 = m7 * m8
# print('m7-m9:')
# print('m7:', m7)
# print('m8:', m8)
# print('m9:', m9)
#
# print("\n" + "=" * 20 + "\nDerivatives Monoms\n" + "=" * 20)
# m10 = m9.derivative()
# m11 = m5.derivative()
# m12 = m4.derivative()
# m13 = m12.derivative()
# print('m10-m13:')
# print("m10=m9'(" + str(m9) + "'):")
# print('m10:', m10)
# print("m11=m5'(" + str(m5) + "'):")
# print('m11:', m11)
# print("m12=m4'(" + str(m4) + "'):")
# print('m12:', m12)
# print("m13=m12'(" + str(m12) + "'):")
# print('m13:', m13)
#
# print("\n" + "=" * 20 + "\nIntegrate Monoms\n" + "=" * 20)
# m14 = m10.integral()
# m15 = m11.integral()
# m16 = m12.integral()
# m17 = m13.integral()
# print('m14-m17:')
# print('integral(' + str(m10) + ')=' + str(m14))
# print('integral(' + str(m11) + ')=' + str(m15))
# print('integral(' + str(m12) + ')=' + str(m16))
# print('integral(' + str(m13) + ')=' + str(m17))


@total_ordering
class Polynomial:
    def __init__(self, l):
        if not isinstance(l, list):
            raise ValueError("invalid polynomic initiation.")
        for monom in l:
            if (not isinstance(monom, tuple)) or len(monom) != 2:
                raise ValueError("invalid polynomic initiation.")
            if (not isinstance(monom[0], int)) or monom[0] < 0:
                raise ValueError('Invalid polynomial initialization.')
        self.head = None
        for monom in l:
            self.add_monom(Monom(monom[0], monom[1]))
        self.remove_coef_0_monom()

    def add_monom(self, monom):
        if self.head is None or self.head.power < monom.power:
            monom.next = self.head
            self.head = monom
        elif self.head.power == monom.power:
            self.head.coef += monom.coef
        else:
            p = self.head
            while p.next != None and p.next.power > monom.power:
                p = p.next
            if p.next == None or p.next.power < monom.power:
                monom.next = p.next
                p.next = monom
            else:
                p.next.coef += monom.coef

    def remove_coef_0_monom(self):
        while self.head is not None and self.head.coef == 0:
            self.head = self.head.next
        if self.head is not None:
            p = self.head
            while p is not None and p.next is not None:
                while p.next is not None and p.next.coef == 0:
                    p.next = p.next.next
                p = p.next

    def rank(self):
        return self.head.power if self.head is not None else 0

    def calculate_value(self, x):
        res = 0
        p = self.head
        while p is not None:
            res += p.coef * x ** p.power
            p = p.next
        return res

    def derivative(self):
        l = []
        p = self.head
        while p is not None:
            derivative = Monom.derivative(p)
            l.append((derivative.power, derivative.coef))
            p = p.next
        return Polynomial(l)

    def integral(self, const=0):
        l = []
        p = self.head
        while p is not None:
            integral = Monom.integral(p)
            l.append((integral.power, integral.coef))
            p = p.next
        l.append((0, const))
        return Polynomial(l)

    def __repr__(self):
        if self.head is None:
            return 'P(X)=0'
        s = 'P(X)='
        p = self.head
        while p is not None:
            # s += str(p)  # str also return what __repr__ return
            s += Monom.__repr__(p)  # str also return what __repr__ return
            if p.next is not None:
                s += '+'
            p = p.next
        return s

    def __neg__(self):
        l = []
        p = self.head
        while p is not None:
            l.append((p.power, -p.coef))
            p = p.next
        return Polynomial(l)

    def __add__(self, other):
        l = []
        p = self.head
        while p is not None:
            l.append((p.power, p.coef))
            p = p.next

        p = other.head
        while p is not None:
            l.append((p.power, p.coef))
            p = p.next
        return Polynomial(l)

    def __sub__(self, other):
        return self + (- other)

    def __mul__(self, other):
        l = []
        if isinstance(other, (int, float)):
            p = self.head
            while p is not None:
                l.append((p.power, p.coef * other))
                p = p.next
            return Polynomial(l)
        if isinstance(other, Polynomial):
            p = self.head
            while p is not None:
                po = other.head
                while po is not None:
                    tmp_monom = p * po
                    l.append((tmp_monom.power, tmp_monom.coef))
                    po = po.next
                p = p.next
            return Polynomial(l)

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        p = self.head
        po = other.head
        while p is not None and po is not None:
            if p != po:
                return False
            p = p.next
            po = po.next
        return p is None and po is None

    def __gt__(self, other):
        if self.head is None or self.rank() < other.rank():
            return False
        if other.head is None or self.rank() > other.rank():
            return True
        p = self.head
        po = other.head
        while p is not None or po is not None:
            if po is None:
                return True
            if p is None:
                return False
            if p>po:
                return True
            if p<po:
                return False
            p = p.next
            po = po.next
        return False


# print("=" * 20 + "\nDefine Polynoms\n" + "=" * 20)
# p1 = Polynomial([(1, 2), (2, 1), (5, 6), (6, 5), (1, 2), (2, 1)])
# p2 = Polynomial([])
# p3 = Polynomial([(8, 0), (3, -5), (3, 5), (0, 18)])
# print('p1-p3:')
# print(p1)
# print(p2)
# print(p3)
#
# print("\n" + "=" * 20 + "\nRank and Value\n" + "=" * 20)
# print(p1, ' rank', str(p1.rank()))
# print(p2, ' rank', str(p2.rank()))
# print(p3, ' rank', str(p3.rank()))
# print(p1, ' value(x=0):', str(p1.calculate_value(0)))
# print(p1, ' value(x=1):', str(p1.calculate_value(1)))
# print(p1, ' value(x=2):', str(p1.calculate_value(2)))
#
# print("\n" + "=" * 20 + "\nArithmetic Operations\n" + "=" * 20)
# p4 = Polynomial([(1, 1), (2, 2), (3, 3)])
# p5 = Polynomial([(1, 4), (2, 5), (3, 6)])
#
# p6 = Polynomial([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])
# p7 = Polynomial([(1, -1), (2, -2), (3, 3), (4, -4), (5, -5), (6, -6)])
# print('p4-pv(v1)')
# print('p4:', p4)
# print('p5:', p5)
# print('p6:', p6)
# print('p7:', p7)
# print(p6, '+', p7, '=', (p6 + p7))
# print(p4, '+', p5, '=', (p4 + p5))
# print('-(', p6, ')=', -p6)
# print(p6, '-', p7, '=', p6 - p7)
#
# print("\n" + "=" * 20 + "\nMultiplication\n" + "=" * 20)
# print('p4-p5(v2)')
# print('p4:', p4)
# print('p5:', p5)
# print(p4, '*', p5, '=', (p4 * p5))
# print(p4, '*', 5, '=', (p4 * 5))
# print(5, '*', p4, '=', (5 * p4))
#
# print("\n" + "=" * 20 + "\nDerivatives\n" + "=" * 20)
# print('p4-p5(v3)')
# print('(', p4, ")'=", p4.derivative())
# print('(', p5, ")'=", p5.derivative())
# print('integral(', p4, ")=", p4.integral())
# print('integral(', p5, ")=", p5.integral())
# print('integral(', p5, ")-18=", p5.integral(-18))
# print('integral((', p4, ")')=", p4.derivative().integral())
#
# print("\n" + "=" * 20 + "\nInequalities\n" + "=" * 20)
# print('p8-p9')
# p8 = Polynomial([(1, 4), (2, 5), (3, 6)])
# p9 = Polynomial([(1, 4), (2, 5), (3, 6)])
# p10 = Polynomial([(1, 4.1), (2, 5), (3, 6)])
# p11 = Polynomial([(4, 5)])
#
# print(p8, '==', p9, ':', str(p8 == p9))
# print(p8, '<=', p9, ':', str(p8 <= p9))
# print(p8, '>=', p9, ':', str(p8 >= p9))
# print(p8, '<', p9, ':', str(p8 < p9))
# print(p8, '>', p9, ':', str(p8 > p9))
# print(p8, '!=', p9, ':', str(p8 != p9))
#
# print('p9-p10')
# print(p9, '==', p10, ':', str(p9 == p10))
# print(p9, '<=', p10, ':', str(p9 <= p10))
# print(p9, '>=', p10, ':', str(p9 >= p10))
# print(p9, '<', p10, ':', str(p9 < p10))
# print(p9, '>', p10, ':', str(p9 > p10))
# print(p9, '!=', p10, ':', str(p9 != p10))
#
# print('p9-p11')
# print(p9, '==', p11, ':', str(p9 == p11))
# print(p9, '<=', p11, ':', str(p9 <= p11))
# print(p9, '>=', p11, ':', str(p9 >= p11))
# print(p9, '<', p11, ':', str(p9 < p11))
# print(p9, '>', p11, ':', str(p9 > p11))
# print(p9, '!=', p11, ':', str(p9 != p11))


class BinTreeNode:
    def __init__(self, val):
        self.value = val
        self.left = self.right = None


class PolynomialBST:
    def __init__(self):
        self.root = None

    def insert(self, poly):
        def insert_helper(node, poly):
            if node is None:
                node = BinTreeNode(poly)
            else:
                if node.value >= poly:
                    node.left = insert_helper(node.left, poly)
                else:
                    node.right = insert_helper(node.right, poly)
            return node

        self.root = insert_helper(self.root, poly)

    def in_order(self):
        tree_lst = list()

        def in_order_helper(node):
            if node is None:
                return
            in_order_helper(node.left)
            tree_lst.append(node.value)
            in_order_helper(node.right)

        in_order_helper(self.root)
        return tree_lst

    def __add__(self, other):
        new_tree = PolynomialBST()
        poly_lst_1 = self.in_order()
        poly_lst_2 = PolynomialBST.in_order(other)
        for poly1 in poly_lst_1:
            new_tree.insert(poly1)
        for poly2 in poly_lst_2:
            new_tree.insert(poly2)
        return new_tree


# print()
# print("=" * 20 + "\nBinary Search Tree\n" + "=" * 20)
# print('t1')
# t1 = PolynomialBST()
# t1.insert(p1)
# t1.insert(p2)
# t1.insert(p3)
# t1.insert(p4)
# t1.insert(p5)
# print(t1.in_order())
# print('t2')
# t2 = PolynomialBST()
# t2.insert(p6)
# t2.insert(p7)
# t2.insert(p8)
# t2.insert(p9)
# t2.insert(p10)
# t2.insert(p11)
# print(t2.in_order())
# print('t3')
# t3 = t1 + t2
# print(t3.in_order())

poly6 = Polynomial([(4, 3), (3, 2)])
poly7 = Polynomial([(4, 3), (2, 2)])
poly8 = Polynomial([(4, 3), (3, 2), (2, 2)])
poly9 = Polynomial([(4, 3), (3, 2), (1, 2)])
poly3 = Polynomial([(4, 3)])

print(poly3 < poly6)
