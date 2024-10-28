#  Условная конструкция Операторы if,elif, else.
# переменые USER_Pasha
first=int(input()) #первое число
second=int(input()) #второе число
third=int(input()) #третие число


# 1.1 Самый простой метод
## Условие если значения все равны
#if first == second == third:
#    print("3")
## Условия когда 2 числа одинаковы
#elif first == second != third:
#    print("2")
#elif first == third !=second:
#    print("2")
#elif second == third != first:
#    print("2")
## Условия все значения не равны или верхние условия False
#else:
#    print("0")
# Метод 2 самый удобный )))))
if second != first and third !=first:
    print("0")
elif first == second and second == third:
    print("3")
elif first != second or first == third:
    print("2")