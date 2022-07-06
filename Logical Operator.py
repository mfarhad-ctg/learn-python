#Logical Operator
print("Logical Operator")

print("\n")


name = 'Mohammad Farhad'
age = 20
 
name_matched = name== 'Mohammad Farhad' 
age_matched = age> 17


print(name_matched)
print(age_matched)

# not operator
print(not name_matched)
print(not age_matched)

#and operator
print(name_matched and age_matched)
# or operator
print(name_matched or age_matched)


# Logical Operator
# 1.and  2. or   3.not

#Truth Table
# (Condition-A)  (Condition-B)  (Result in and)  (Result in or)
#       True        True            True                True
#       True        False           False               False
#       False       True            False               True
#       False       False           False               False