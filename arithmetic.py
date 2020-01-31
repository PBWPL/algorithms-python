# -*- coding: utf-8 -*-


from ArithmeticCode import ArithmeticCode as AC

arithmetic = AC("Piotr#", [0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667])
print (arithmetic.getAutor())
print (arithmetic.coding(), arithmetic.decoding(arithmetic.coding()))

arithmetic = AC("Bęc#", [1 / 4, 1 / 4, 1 / 4, 1 / 4])
print (arithmetic.coding(), arithmetic.decoding(arithmetic.coding()))

arithmetic = AC.word("RAPAPARA#")
print (arithmetic.coding(), arithmetic.decoding(arithmetic.coding()))
print (arithmetic.S)

arithmetic = AC.code(0.21787985888157896,
                     [['A', 0.4166666666666667], ['B', 0.16666666666666666], ['R', 0.16666666666666666],
                      ['C', 0.08333333333333333], ['D', 0.08333333333333333], ['#', 0.08333333333333333]])
print (arithmetic.decoding(), arithmetic.coding())
