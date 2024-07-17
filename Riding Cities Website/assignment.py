cost = input('Cost of good: ')
cost1 = float(cost)
discount = 0.1
tax = 0.08

if cost1 >= 100:
    print('Price over $100, eligible for discount')
    discount *= cost1
    
    print('Discount: ' + str(discount))
    
    total = cost1 - discount
    
    print('')
    
    total = ((cost1 * tax) + cost1)
    print('Total: ' + str(total))
else:
    print('Price under $100, not eligible for discount')
    cost1 *= tax

    print('Total: ' + str(cost1))