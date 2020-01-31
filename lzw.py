# -*- coding: utf-8 -*-


from LZWCode import LZWCode as LZW

lzw = LZW()
print(lzw.get_autor())
print ('Coding string: "aaa aa1 a1b" -->', lzw.coding("aaa aa1 a1b"))
print ('Dictionary:', lzw.char_arr)
print ('Dictionary invert:', lzw.char_arr_invert)
print ('Decoding code: ' + str(lzw.coding("aaa aa1 a1b")) + ' -->',
       lzw.decoding(lzw.coding("aaa aa1 a1b"), lzw.char_arr_invert))
