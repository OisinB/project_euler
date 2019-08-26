import sys
n = int(sys.argv[1])

singles = {
1: 'one'
, 2: 'two'
, 3: 'three'
, 4: 'four'
, 5: 'five'
, 6: 'six'
, 7: 'seven'
, 8: 'eight'
, 9: 'nine'
, 0: ''
}

tens = {
2: 'twenty'
, 3: 'thirty'
, 4: 'forty'
, 5: 'fifty'
, 6: 'sixty'
, 7: 'seventy'
, 8: 'eighty'
, 9: 'ninety'
, 0: ''
}

teens = {
1: 'eleven'
, 2: 'twelve'
, 3: 'thirteen'
, 4: 'fourteen'
, 5: 'fifteen'
, 6: 'sixteen'
, 7: 'seventeen'
, 8: 'eighteen'
, 9: 'nineteen'
, 0: 'ten'
}

def construct_word(n):
    if n == 1000:
        return 'onethousand'
    first_digit = n//100
    second_digit = (n//10)%10
    third_digit = n%10

    word = ''

    if first_digit > 0:
        word = word + singles[first_digit] + 'hundred'
        if second_digit > 0 or third_digit > 0:
            word += 'and'
    if second_digit == 1:
        word += teens[third_digit]
    elif second_digit > 0:
        word += tens[second_digit]

    if second_digit != 1:
        word += singles[third_digit]

    return word

total = 0
for i in range(1, n+1):
    total += len(construct_word(i))

print(total)
