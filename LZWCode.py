# -*- coding: utf-8 -*-


from io import StringIO


class LZWCode:
    __autor = '{}{}{}'.format("|-*****-***-|\n| ", "Piotr Bęc", " |\n|-*****-***-|")

    def __init__(self):
        self.char_arr_size = 0
        self.encoded_word, self.decoded_code = [], 0
        self.char_arr, self.char_arr_invert = {}, {}

    def coding(self, word):
        w, self.encoded_word = "", []
        self.char_arr_size = len(word)

        try:
            self.char_arr = dict((word[i], i) for i in range(self.char_arr_size))
            for c in word:

                wc = w + c
                if wc in self.char_arr:
                    w = wc
                else:
                    self.encoded_word.append(self.char_arr[w])
                    self.char_arr[wc] = self.char_arr_size
                    self.char_arr_size += 1
                    w = c

            if w:
                self.encoded_word.append(self.char_arr[w])
                self.char_arr_invert = {v: k for k, v in self.char_arr.items()}

        except Exception as e:
            print (e.__class__.__name__, ':', str(e))
        return self.encoded_word

    def decoding(self, code, dictionary):
        self.decoded_code = StringIO()
        self.char_arr_invert, self.char_arr_size = dictionary, len(code)

        try:
            for d in code:

                if d in self.char_arr_invert:
                    entry = self.char_arr_invert[d]
                else:
                    raise ValueError('Bad compressed d: %s' % d)

                self.decoded_code.write(entry)

            self.decoded_code = self.decoded_code.getvalue()
        except Exception as e:
            self.decoded_code = 0
            print (e.__class__.__name__, ':', str(e))
        return self.decoded_code

    def get_autor(self):
        return self.__autor
