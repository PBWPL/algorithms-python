# -*- coding: utf-8 -*-


from HuffmanCode import HuffmanCode as HC

huffman = HC()
print (huffman.get_autor())
print ('Coding word: "Bęc" -->', huffman.coding("Bęc"))
print ("Set: ", huffman.codes)
print ('Decoding code: "' + huffman.coding("Bęc") + '" -->', huffman.decoding(huffman.coding("Bęc")))

del huffman
print ("----------")

huffman = HC()
print ('Coding word: "Piotr" -->', huffman.coding("Piotr"))
print ("Set: ", huffman.codes)
print ('Decoding code: "' + huffman.coding("Piotr") + '" -->', huffman.decoding(huffman.coding("Piotr")))
