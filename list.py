def find_all_hobbyists(hobby, hobbies):
  for key, value in hobbies.items():
      if hobby in value:
          key1 = key
  return key1
if __name__ == "__main__":
    hobbies = {
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga']
    }
print(find_all_hobbyists('Yoga', hobbies))
print(find_all_hobbyists('Drama', hobbies))

