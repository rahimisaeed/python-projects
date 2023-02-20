# import numpy as np
# import matplotlib as plt

def over_nine_thousand(lst):
  sum_element = 0
  new_lst = []
  index = 0
  while sum_element < 9000:
    # for index in range(len(lst)):
      sum_element += lst[index]
      # print(sum_element)
      # new_lst.append(lst[index])
      # print(new_lst)
      index +=1
  return sum_element
  # sum = 0
  # for index in lst:
  #   sum +=index
  #   if sum >9000:
  #     break
  # return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))