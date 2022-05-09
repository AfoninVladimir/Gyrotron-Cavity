########################################################################################################################
##
## BY: AFONIN VLADIMIR ALEKSEEVICH
##
## PROJECT: GYROTRON CAVITY GUI
##
## V: 0.6.0
##
########################################################################################################################

from import_all import *


class Auxiliary_Functions:

    # перевод в систему СИ
    def transfer_to_the_SI_system(self, list_input):
        list_out = []
        mm = 10 ** (-3)
        cm = 10 ** (-2)
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

    # заменяет "e" на "E"
    def scientific_notation(self, number):
        """
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
        If omitted, the exponent will be at least 2 digits."""
        return str(
            np.format_float_scientific(number, unique = False, precision = 12, trim = 'k', exp_digits = True)).replace("e", "E")
