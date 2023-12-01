f = open("modified_input.txt", "r")
lines = f.readlines()
string_cats = []



for line in lines:
    nums = []
    for char in line:
        if char.isdigit():
            nums += char
    string_cats.append((str((str(nums[0]) + str(nums[-1])))))
    
counter = 0

for number in string_cats:
    counter += int(number)

print(counter)