from itertools import product


# main_courses = ['beef stew', 'fried fish']
# price_main_courses = [28, 23]
#
# desserts = ['ice-cream', 'cake']
# price_desserts = [2, 4]
#
# drinks = ['cola', 'wine']
# price_drinks = [3, 10]

main_tup = list(zip(main_courses, price_main_courses))
dess_tup = list(zip(desserts, price_desserts))
drinks_tup = list(zip(drinks, price_drinks))

for elem1, elem2, elem3 in product(main_tup, dess_tup, drinks_tup):
    s = elem1[1] + elem2[1] + elem3[1]
    if s <= 30:
        print(elem1[0], elem2[0], elem3[0], s)
