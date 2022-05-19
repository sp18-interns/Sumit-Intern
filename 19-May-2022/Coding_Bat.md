def double_char(str):
  """
  Given a string, return a string where for every char in the original, 
  there are two chars. 
  """
  new_str = ""
  for char in str:
    new_str += char*2
  return new_str

def count_hi(str):
  """
  Return the number of times that the string "hi" appears anywhere 
  in the given string. 
  """
  return str.count("hi")

def cat_dog(str):
  """
  Return True if the string "cat" and "dog" appear the same number of 
  times in the given string. 
  """
  return str.count("cat") == str.count("dog")