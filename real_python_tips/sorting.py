# SORTED preserves original list
animals = ['cat', 'dog', 'cheetah', 'ox']
print(sorted(animals))  # => ['cat', 'cheetah', 'dog', 'ox']
print(animals)  # => 'cat', 'dog', 'cheetah', 'ox']
# to mutate original list use SORT
animals.sort()  # => None, but modifies list in place
print(animals)  # => ['cat', 'cheetah', 'dog', 'ox']

## USE LAMBDA to sort on key of dict objects in list
animals_house = [
    {'type': 'dog', 'name': 'Yeti', 'age': 5},
    {'type': 'person', 'name': 'Bridge', 'age': 42},
    {'type': 'bird', 'name': 'Warbler', 'age': 17}
    ]
print(sorted(animals_house, key=lambda animal : animal['age']))
# => [{'type': 'dog', 'name': 'Yeti', 'age': 5}, {'type': 'bird', 'name': 'Warbler', 'age': 17}, {'type': 'person', 'name': 'Bridge', 'age': 42}]
print(sorted(animals_house, key=lambda animal : animal['type']))
# => [{'type': 'bird', 'name': 'Warbler', 'age': 17}, {'type': 'dog', 'name': 'Yeti', 'age': 5}, {'type': 'person', 'name': 'Bridge', 'age': 42}]