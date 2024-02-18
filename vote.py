age=int(input('enter your age-'))
if age>=18:
    print('Eligible')
elif age in range(1,19):
    print('you eligible after' ,18-age,'year')
else :
    print('not eligible') 