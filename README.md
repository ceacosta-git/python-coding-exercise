# python-coding-exercise

## Problem description for count_duplicates.py
*Given* a list of items
<br>*When* processing the list provided above
<br>*Then* return each item and the number of times it appears in the list

Examples:

Given list ["apple", "orange", "watermelon", "apple"]
<br>Return apple 2, orange 1, watermelon 1

### Additional requirements

#### Scenario: items is None
*Given* None as a list
<br>*When* counting duplicates
<br>*Then* raise an error

#### Scenario: counting duplicates is case-sensitive
*Given* a list with string items
<br>*When* processing a string list item provided above
<br>*Then* return each item and the number of times it appears in the list
<br>*And* string items should only count as duplicates if they match their casing

Examples:

Given list ["apple", "orange", "watermelon", "apple", "Orange"]
<br>Return apple 2, orange 1, watermelon 1, Orange 1


## Problem description for exercise.py

*Given* a list of numbers and a target number
<br>*When* the target number is in the list
<br>*Then* return the neighbors (i.e., item at left of target, and item at the right of target)

Examples:

Given list [15, 3, 76, 78, 5, 3, 1] and target is 3
<br>Return [15, 76]

Given list [15, 3, 76, 78, 5, 3, 1] and target is 78
<br>Return [76, 5]

### Additional requirements

#### Scenario: target not found
*Given* a list of numbers and a target number
<br>*When* the target number is not in the list
<br>*Then* raise an error

#### Scenario: target is the first element of the list
*Given* a list of numbers and a target number
<br>*When* the target number is the first element in the list
<br>*Then* return its neighbor (i.e., item at the right of target)

Example:

Given list [15, 3, 76, 78, 5, 3, 1] and target is 15
<br>Return [3]

#### Scenario: target is the last element of the list
*Given* a list of numbers and a target number
<br>*When* the target number is the last element in the list
<br>*Then* return its neighbor (i.e., item at the left of target)

Example:

Given list [15, 3, 76, 78, 5, 33, 1] and target is 1
<br>Return [33]

#### Scenario: target is the only element of the list
*Given* a list of numbers and a target number
<br>*When* the target number is the only element in the list
<br>*Then* return no neighbors (i.e., empty list)

Example:

Given list [15] and target is 15
<br>Return []
