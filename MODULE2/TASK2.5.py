leiviska = float(input('please enter the talents:\n'))
naula = float(input('please enter the pounds:\n'))
luoti = float(input('please enter the lots:\n'))

total_leiviska = (leiviska * 20 * 32) + (naula * 32) + luoti
total_grams =  total_leiviska * 13.3
kilograms = total_grams / 1000
grams = total_grams % 1000

print(f'The weight in modern units would be :\n{int(kilograms)} kilograms and {grams:.2f} grams')

