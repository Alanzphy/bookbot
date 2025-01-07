def main():
  path_to_file      = "./books/frankenstein.txt"
  text              = read_file(path_to_file)
  counted_words     = count_words(text)
  dictionary_report = count_characters(text)
  dictionary_sorted = sort_dictionary(dictionary_report)

  print(f"--- Begin report of {path_to_file} ---")
  print(f"{counted_words} words found in the document")
  print()
  for item in dictionary_sorted:
    if item['char'].isalpha():
      print(f"The '{item['char']}' character was found {item['count']} times")
  print("--- End report ---")


def read_file(path):
  with open(path) as f:
    file_contents = f.read()
  return file_contents

def count_words(text):
  words = text.split()
  return len(words)

def count_characters(text):
  count_dict = {}
  string_lowercase = text.lower()
  for char in string_lowercase:
    if char.isalpha():
      if char in count_dict:
        count_dict[char] += 1
      else:
        count_dict[char] = 1
  return count_dict

def sort_dictionary(count_dict):
  sorted_list = []
  for key in count_dict:
    sorted_list.append({'char': key, 'count': count_dict[key]})
  sorted_list.sort(reverse=True, key=lambda x: x['count'])
  return sorted_list



main()
