#  �������� ����������� ��������� if,elif, else.
# ��������� USER_Pasha
first=int(input()) #������ �����
second=int(input()) #������ �����
third=int(input()) #������ �����


# 1.1 ����� ������� �����
## ������� ���� �������� ��� �����
#if first == second == third:
#    print("3")
## ������� ����� 2 ����� ���������
#elif first == second != third:
#    print("2")
#elif first == third !=second:
#    print("2")
#elif second == third != first:
#    print("2")
## ������� ��� �������� �� ����� ��� ������� ������� False
#else:
#    print("0")
# ����� 2 ����� ������� )))))
if second != first and third !=first:
    print("0")
elif first == second and second == third:
    print("3")
elif first != second or first == third:
    print("2")