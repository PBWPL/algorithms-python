# -*- coding: utf-8 -*-


class ArithmeticCode:
    __autor = '{}{}{}'.format("|-*****-***-|\n| ", "Piotr Bęc", " |\n|-*****-***-|")

    def __init__(self, x, y):
        if isinstance(x, str):
            if round(sum(y), 1) != 1:
                exit("Error - bad fractions")

            self.word, self.p, self.break_char = x, y, x[-1]
            self.S, self.__P = self.__createS(x), self.__createP(y)
        elif isinstance(x, float):
            self.code, tmp_1, tmp_2 = x, [], []

            for i in range(len(y)):
                tmp_1.append(y[i][0])
                tmp_2.append(y[i][1])

            self.S, self.p = tmp_1, tmp_2
            self.__P = self.__createP(self.p)
            self.break_char = self.S[-1]
        else:
            exit("Error")

    @classmethod
    def word(cls, word):
        test, p = [], []
        for i in range(len(word)):
            if word[i] not in test:
                test.append(word[i])
                p.append(word.count(word[i]) / len(word))

        return cls(word, p)

    @classmethod
    def code(cls, code, letters):

        return cls(code, letters)

    @staticmethod
    def __charSection(L, R, P, code, S):
        index, ZP, ll, x = len(S), [], L, 0

        for i in range(index):
            if i != 0:
                ZP.append([L, ll + (R - ll) * P[i]])
                if L <= code < ll + (R - ll) * P[i]:
                    x = i
                    break

                L = ll + (R - ll) * P[i]
            else:
                ZP.append([L, L + (R - L) * P[i]])
                if L <= code < L + (R - L) * P[i]:
                    x = i
                    break

                L = L + (R - L) * P[i]

        return ZP[-1][0], ZP[-1][1], S[x]

    @staticmethod
    def __calcSection(L, R, P, index):
        ZP, ll = [], L

        for i in range(index):
            if i != 0:
                ZP.append([L, ll + (R - ll) * P[i]])
                L = ll + (R - ll) * P[i]
            else:
                ZP.append([L, L + (R - L) * P[i]])
                L = L + (R - L) * P[i]

        return ZP[-1][0], ZP[-1][1]

    @staticmethod
    def __createP(p):
        P, value = [], 0

        for i in range(len(p)):
            value += p[i]
            P.append(value)

        return P

    @staticmethod
    def __createS(word):
        S = []

        for i in range(len(word)):
            if word[i] not in S:
                S.append(word[i])

        return S

    def coding(self):
        L, R, P = 0, 1, self.__P

        for i in range(len(self.word)):
            index = self.S.index(self.word[i]) + 1
            L, R = self.__calcSection(L, R, P, index)

        self.code = L

        return self.code

    def decoding(self, *code):

        if code == ():
            code = self.code
        else:
            code = code[0]

        i, L, R, P = 0, 0, 1, self.__P
        self.word = ''

        while True:
            L, R, x = self.__charSection(L, R, P, code, self.S)
            self.word += x
            if x == self.break_char:
                break

            i += 1

        return self.word

    def setWord(self, word):
        self.word = word

    def setp(self, p):
        self.p = p

    def getP(self):
        return self.__createP

    def getAutor(self):

        return self.__autor
