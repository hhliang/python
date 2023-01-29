unit = str(input('請輸入單位單位: '))
length = float(input('請輸入長度: '))

if unit == 'inch' or unit == '英吋' :
    result  = length * 2.54
    print('%.4f英吋等於%.4f公分' % (length, result))
elif unit == 'cm' or unit == '公分' :
    result  = length / 2.54
    print('%.4f公分等於%.4f英吋' % (length, result))
else :
    print('請輸入正確單位')