class Solution:
    def intToRoman(self, num: int) -> str:
        roman_number = ''
        roman_number += 'M'*int(num//1000)
        if (num//100)%10 > 0:
            if (num//100)%10 <= 3:
                roman_number += "C"*int((num//100)%10)
            elif (num//100)%10 == 4:
                roman_number += "CD"
            elif (num//100)%10 <= 8:
                roman_number += "D" +"C"*int(((num//100)%10)-5)
            elif (num//100)%10 == 9:
                roman_number += "CM"
        if (num//10)%10 >0:
            if (num//10)%10 <= 3:
                roman_number += "X"*int((num//10)%10)
            elif (num//10)%10 == 4:
                roman_number += "XL"
            elif (num//10)%10 <= 8:
                roman_number += "L" + "X"*int(((num//10)%10)-5)
            elif (num//10)%10 == 9:
                roman_number += "XC"
        if num%10 >0:
            if num%10 <=3:
                roman_number += "I"*int(num%10)
            elif num%10 ==4:
                roman_number += "IV"
            elif num%10 <=8:
                roman_number += "V" + "I"*int((num%10) - 5)
            elif num%10 ==9:
                roman_number += "IX"            


        return roman_number
