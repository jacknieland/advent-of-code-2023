f = open("input.txt", "r")
lines = f.readlines()
string_cats = []

NUMBERS = {
        'one' : "o1e",
        'two' : "t2o",
        'three' : "t3e",
        'four' : "f4r",
        'five' : "f5e",
        'six' : "s6x",
        'seven' : "s7n",
        'eight' : "e8t",
        'nine' : "n9e",
}

for line in lines:
    new_line = line
    for num in NUMBERS:
        new_line = new_line.replace(num, NUMBERS[num])
    nums = []
    for char in new_line:
        if char.isdigit():
            nums += char
    string_cats.append((str((str(nums[0]) + str(nums[-1])))))
    
counter = 0

for number in string_cats:
    counter += int(number)

print(counter)
            
