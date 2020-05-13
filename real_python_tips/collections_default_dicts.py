student_grades_a = {
    'LJ':  [100, 99, 89],
    'BE': [100, 99, 100]
}

def get_grade_brute(name):
    if name in student_grades_a:
        return student_grades_a[name]
    return []

def get_grades_better(name):
    return student_grades_a.get(name, [])

def get_grades_assign_if_none(name):
    return student_grades_a.setdefault(name, [])


print(get_grade_brute("LJ"))  # => [100, 99, 89]
print(student_grades_a)  # => {'LJ': [100, 99, 89], 'BE': [100, 99, 100]}
print(get_grades_better('BE'))
print(student_grades_a)  # => {'LJ': [100, 99, 89], 'BE': [100, 99, 100]}
print(get_grades_better('JO'))  # => []
print(student_grades_a)  # => {'LJ': [100, 99, 89], 'BE': [100, 99, 100]}
print(get_grades_assign_if_none('JO'))  # => []
print(student_grades_a)  # => {'LJ': [100, 99, 89], 'BE': [100, 99, 100], 'JO': []}

from collections import defaultdict
student_grades = defaultdict(list)
def set_grade_best(name, score):
    student_grades[name].append(score)

print(student_grades)  #=> defaultdict(<class 'list'>, {})
set_grade_best("Yeti", 100)
print(student_grades)  # => defaultdict(<class 'list'>, {'Yeti': [100]})


### USING DEFAULTDICT WITH AN INITIAL VALUE/DICT
student_grades = defaultdict(list, student_grades_a)
print(student_grades)  # => defaultdict(<class 'list'>, {'LJ': [100, 99, 89], 'BE': [100, 99, 100], 'JO': []})

student_score = defaultdict(lambda: 85)
print(student_score)  # => defaultdict(<function <lambda> at 0x10f455b90>, {})
print(student_score["Reg"] + 15)  # => 100
print(student_score)  # => defaultdict(<function <lambda> at 0x10f455b90>, {'Reg': 85})
student_score["Jojo"] += 15
print(student_score)  # => defaultdict(<function <lambda> at 0x10f455b90>, {'Reg': 85, 'Jojo': 100})
