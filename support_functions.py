########################################################################################################################
##
## BY: AFONIN VLADIMIR ALEKSEEVICH
##
## PROJECT: GYROTRON CAVITY GUI
##
## V: 1.0.0
##
########################################################################################################################

import numpy as np


class support_functions:
    r'''
    # Вспомогательные функции
    '''

    # перевод в систему СИ
    def transfer_to_the_SI_system(self, list_input):
        r'''
        Функция для перевода параметров в систему СИ

        Если функция обнаруживает в элементе массива подстроку 'mm' или 'cm', то удаляет эту подстроку,
        переводит в числовой вид и умножает на переменную `mm` или `cm` соответственно.

        Принимает на вход:

        list_input:
        - тип: список (list)
        - тип параметров: строка (str)
        - длина: 7

        list_input = [R0, L, z_left, z_right, z_start, z_finish, dz]

        Возвращает:

        list_out:
        - тип: список (list)
        - тип параметров: число с плавающей точкой (float)
        - длина: 7

        list_out = [R0, L, z_left, z_right, z_start, z_finish, dz]
        '''

        list_out = []  # новый список, куда будут сохранятся численные значения из списка
        mm = 10 ** (-3)
        cm = 10 ** (-2)

        # Цикл по списку list_input, в котором переменные переводятся из
        # указанных единиц измерения (миллиметры или сантиметры) в метры.
        # Если в строковом параметре находится подстрока 'mm' или 'cm',
        # то переводя в число параметр умножается на соответствую переменную.
        # Число добавляется в конец списка list_out.
        for i in list_input:
            if " mm" in i:
                list_out.append(float(i.replace(' mm', '')) * mm)
            elif "mm" in i:
                list_out.append(float(i.replace('mm', '')) * mm)
            elif " cm" in i:
                list_out.append(float(i.replace(' cm', '')) * cm)
            elif "cm" in i:
                list_out.append(float(i.replace('cm', '')) * cm)
            else:
                list_out.append(i)
        return list_out

    # преобразует число в научную форму записи (для Fortran)
    def scientific_notation(self, number):
        r'''
        Функция преобразует число с плавающей точкой в экспоненциальный формат записи
        (экспоненциальная запись) числа и возвращает его в виде строки.

        Принимает на вход:

        number:
        - тип: число с плавающей точкой (float)

        Возвращает:
        - тип: строка (str)
        - длина: 18

        Пример:

            input:
            0.035

            output:
            "3.500000000000E-02"

        Ниже приведено описание функции `format_float_scientific` из библиотеки `numpy`
        которая используется для преобразования числа с плавающей точкой в экспоненциальную запись.

        `numpy.format_float_scientific(x, precision=None, unique=True, trim='k',
        sign=False, pad_left=None, exp_digits=None, min_digits=None)`

            Format a floating-point scalar as a decimal string in scientific notation.

            Provides control over rounding, trimming and padding. Uses and assumes
            IEEE unbiased rounding. Uses the "Dragon4" algorithm.

            Parameters
            ----------
            x : python float or numpy floating scalar
                Value to format.
            precision : non-negative integer or None, optional
                Maximum number of digits to print. May be None if `unique` is
                `True`, but must be an integer if unique is `False`.
            unique : boolean, optional
                If `True`, use a digit-generation strategy which gives the shortest
                representation which uniquely identifies the floating-point number from
                other values of the same type, by judicious rounding. If `precision`
                was omitted, print all necessary digits, otherwise digit generation is
                cut off after `precision` digits and the remaining value is rounded.
                If `False`, digits are generated as if printing an infinite-precision
                value and stopping after `precision` digits, rounding the remaining
                value.
            trim : one of 'k', '.', '0', '-', optional
                Controls post-processing trimming of trailing digits, as follows:
                * 'k' : keep trailing zeros, keep decimal point (no trimming)
                * '.' : trim all trailing zeros, leave decimal point
                * '0' : trim all but the zero before the decimal point. Insert the
                  zero if it is missing.
                * '-' : trim trailing zeros and any trailing decimal point
            sign : boolean, optional
                Whether to show the sign for positive values.
            pad_left : non-negative integer, optional
                Pad the left side of the string with whitespace until at least that
                many characters are to the left of the decimal point.
            exp_digits : non-negative integer, optional
                Pad the exponent with zeros until it contains at least this many digits.
                If omitted, the exponent will be at least 2 digits.
        '''

        return str(
            np.format_float_scientific(number, unique = False, precision = 12, trim = 'k', exp_digits = 2)).replace("e",
                                                                                                                    "E")
