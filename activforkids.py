# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

# For example, Jay ran like a fool! or Chantelle slid down the slide!.

# The following lists of children should be iterated, and the names sent to the appropriate functions.

# running_kids = ["Pam", "Sam", "Andrea", "Will"]
# swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
# sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
# hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]


def run_function(name_of_child):
    print(f'{name_of_child} is running')


def swing_function(name_of_child):
    print(f'{name_of_child} is swinging')


def slide_function(name_of_child):
    print(f'{name_of_child} is sliding')


def hide_function(name_of_child):
    print(f'{name_of_child} is hiding')


running_kids = ["Pam", "Sam", "Andrea", "Will"]

swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]

sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]

hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for eachkid in running_kids:
    run_function(eachkid)

for eachkid in swinging_kids:
    swing_function(eachkid)

for eachkid in sliding_kids:
    slide_function(eachkid)

for eachkid in hiding_kids:
    hide_function(eachkid)
