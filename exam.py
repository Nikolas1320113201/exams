class Calculator:

  def max_in_list(lst):
      assert lst
      m = lst[0]
      for i in lst:
          if i > m:
              m = i
      return m
 
  max_in_list([1, 5, 3, 12, 4, 8])

