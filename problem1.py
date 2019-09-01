# Enter your code here. Read input from STDIN. Print output to STDOUT
arthmetic_expression = input()
acceptable_brackets = ['(', '{', '[', ')', '}', ']']
opening_acceptable_brackets = ['(', '{', '[']
closing_acceptable_brackets = [')', '}', ']']
bracket_match = {'(': ')', '{': '}', '[': ']'}
opening_found_brackets = []
closing_found_brackets = []
found_brackets = []
decision_flag = ""
brackets_in_order = ""

for char in arthmetic_expression:
    if char in opening_acceptable_brackets:
        found_brackets.append(char)
        opening_found_brackets.append(char)
    elif char in closing_acceptable_brackets:
        found_brackets.append(char)
        closing_found_brackets.append(char)
for bracket in found_brackets:
    brackets_in_order += bracket
counter = 0
closing_found_brackets.reverse()
if len(found_brackets) % 2 == 0 and len(opening_found_brackets) == len(closing_found_brackets):
    for opening_bracket, closing_bracket in zip(opening_found_brackets, closing_found_brackets):
        if bracket_match[opening_bracket] == closing_bracket:
            counter += 1
    if len(opening_found_brackets) == counter:
        decision_flag = 'Y'
else:
    decision_flag = 'N'

print(decision_flag+' '+brackets_in_order)
