# -*- coding: utf-8 -*-


import heapq

from HTNode import HTNode


class HuffmanCode:
    __autor = '{}{}{}'.format("|-*****-***-|\n| ", "Piotr Bęc", " |\n|-*****-***-|")

    def __init__(self):
        self.heap, self.codes, self.reverse_codes, self.x = [], {}, {}, []

    @staticmethod
    def counter_char(word):
        freq = {}
        for character in word:
            if character not in freq:
                freq[character] = 0
            freq[character] += 1

        return freq

    def coding(self, word):
        try:
            freq = self.counter_char(word)  # tworzy zestaw: {znak - ilosc_wystapien}
            self.make_heap(freq)  # tworzy wezly (obiekty klasy HTNode)
            self.merge_nodes()  # łączy wezly (obiekty klasy HTNode)
            self.make_codes()  # tworzy zestaw: {znak - kod_bitowy}, {kod_bitowy - znak}
            encoded_word = self.get_encoded_word(word)  # koduje znaki na kod bitowy
        except Exception as e:
            encoded_word = 0
            print (e.__class__.__name__, ':', str(e))

        return encoded_word

    def decoding(self, code):
        try:
            decoded_word = self.get_decoded_code(code)  # dekoduje kod bitowy na znaki

        except Exception as e:
            decoded_word = 0
            print (e.__class__.__name__, ':', str(e))

        return decoded_word

    def make_heap(self, freq):
        for character in freq:
            node = HTNode(character, freq[character])
            heapq.heappush(self.heap, node)
            heapq.heappush(self.x, node)

    def merge_nodes(self):
        while len(self.heap) > 1:
            n1, n2 = heapq.heappop(self.heap), heapq.heappop(self.heap)
            merged = HTNode(None, n1.freq + n2.freq)
            merged.left, merged.right = n1, n2
            heapq.heappush(self.heap, merged)
            heapq.heappush(self.x, merged)

    def make_codes(self):
        root, current_code = heapq.heappop(self.heap), ""

        self.make_codes_helper(root, current_code)

    def make_codes_helper(self, root, current_code):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_codes[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def get_encoded_word(self, word):
        encoded_word = ""

        for character in word:
            encoded_word += self.codes[character]

        return encoded_word

    def get_decoded_code(self, code):
        word = ""
        tmp = ""
        for bit in code:
            tmp += bit
            if tmp in self.reverse_codes:
                word += self.reverse_codes[tmp]
                tmp = ""

        return word

    def get_autor(self):

        return self.__autor
