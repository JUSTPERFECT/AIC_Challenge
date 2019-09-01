# Enter your code here. Read input from STDIN. Print output to STDOUT
email = input()
valid_flag = False

if '@' in email:
    part1 = email.split('@')[0]
    part2 = email.split('@')[1]
    try:
        if part1.isalnum() and part1[0].isalpha():
            part2_sep_count = part2.count('.')
            if part2_sep_count == 1 and part2.split('.')[0].isalnum() and part2.split('.')[1].isalpha() and (len(part2.split('.')[1]) == 2 or len(part2.split('.')[1]) == 3):
                valid_flag = True
            elif part2_sep_count == 2 and part2.split('.')[0].isalnum() and part2.split('.')[1].isalnum() and part2.split('.')[2].isalpha() and (len(part2.split('.')[2]) == 2 or len(part2.split('.')[2]) == 3):
                valid_flag = True
        else:
            valid_flag = False
    except:
        print('exceptions raised')
else:
    valid_flag = False

if(valid_flag):
    print("Valid")
else:
    print("Invalid")
