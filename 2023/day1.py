import re

#advent of code pt. 1
def trebuchet_pt1():
  calibration_value = 0

  with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      digits = ''.join(c for c in line if c.isdigit())
      curr_val = digits[0] + digits[len(digits)-1]
      calibration_value += int(curr_val)
  return calibration_value

# print(trebuchet_pt1())


      
#advent of code pt. 2
def extract_to_digits(line):
  word_to_digit = {
      'one': '1',
      'two': '2',
      'three': '3',
      'four': '4',
      'five': '5',
      'six': '6',
      'seven': '7',
      'eight': '8',
      'nine': '9',
      'zero': '0'
  }
  
  result = ""
  
  # Iterate through the input string
  i = 0
  while i < len(line):
      # Check for number words starting from the current position
      found_number = False
      for word in word_to_digit:
          if line[i:].startswith(word):
              # If a number word is found, append its digit to result
              result += word_to_digit[word]
              # Move the index to consider overlapping matches
              found_number = True
              break
  
      # If no number word is found, append the character to the result
      if not found_number:
          result += line[i]
          i += 1
      else:
          i += 1
  
  return ''.join(c for c in result if c.isdigit())

def trebuchet_pt2():
  calibration_value = 0

  with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      print(line)
      digits = extract_to_digits(line)
      print(digits)
      curr_val = digits[0] + digits[len(digits)-1]
      calibration_value += int(curr_val)
  return calibration_value

print(trebuchet_pt2())






