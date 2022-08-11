# python-coding-exercise

## Problem description

*Given* a list of numbers and a target number
<br>*When* the target number is in the list
<br>*Then* return the neighbors (i.e., item at left of target, and item at the right of target)

Examples:

Given list [15, 3, 76, 78, 5, 3, 1] and target is 3
<br>Return [15, 76]

Given list [15, 3, 76, 78, 5, 3, 1] and target is 78
<br>Return [76, 5]

## Additional requirements

### Scenario: target not found
*Given* a list of numbers and a target number
<br>*When* the target number is not in the list
<br>*Then* raise an error

### Scenario: target is the first element of the list
*Given* a list of numbers and a target number
<br>*When* the target number is the first element in the list
<br>*Then* return its neighbor (i.e., item at the right of target)

Example:

Given list [15, 3, 76, 78, 5, 3, 1] and target is 15
<br>Return [3]

### Scenario: target is the last element of the list
*Given* a list of numbers and a target number
<br>*When* the target number is the last element in the list
<br>*Then* return its neighbor (i.e., item at the left of target)

Example:

Given list [15, 3, 76, 78, 5, 33, 1] and target is 1
<br>Return [33]