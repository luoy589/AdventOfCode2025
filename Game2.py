# This is a sample Python script.
from math import floor

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

input_list = "824-1475,967620-1012917,2727216511-2727316897,56345-141494,8811120-8999774,5727326-5922513,935306-961989,76751455-76787170,723458-849157,144648-162230,1597-3207,326085-472746,14-34,66-132,9453977670-9454023729,959903262-960027272,17168-26699,190-332,3351-5602,1-11,371280315-371448887,6252062-6312899,9696887156-9697040132,37-58,32770-52161,6443650762-6443689882,473092-582157,3309726-3347079,852735-912990,8294840594-8294926063,3773964-3884030,7718304-7809359,601947-677833,3434304207-3434405118,449-673,64525269-64702774,31545468-31784543,184451-308951,5771-11485"
# input_list = "123456789-123456800"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #extract ranges
    range_list_str  = input_list.split(",")
    range_list_start = []
    range_list_end = []
    for elem in range_list_str:
        range_lims = elem.split("-")
        range_list_start.append(int(range_lims[0]))
        range_list_end.append(int(range_lims[1]))
######### Part 1 solution
    #process ranges
    solution1 = 0
    for i in range(len(range_list_start)):
        for num in range(range_list_start[i], range_list_end[i]+1):
            found = False
            power = 1
            num_figures = 0
            while not found:
                if num < pow(10,power) :
                    num_figures = power
                    found = True
                else:
                    power += 1
            if num_figures % 2 == 0:
                upper_part = int(num/pow(10, num_figures/2))
                lower_part = int(num-upper_part*pow(10, num_figures/2))
                if upper_part == lower_part:
                    solution1 += num
    print(solution1)
######### Part 2 solution
    # process ranges
    solution2 = 0
    for i in range(len(range_list_start)):
        for num in range(range_list_start[i], range_list_end[i] + 1):
            found = False
            power = 1
            num_figures = 0
            while not found:
                if num < pow(10, power):
                    num_figures = power
                    found = True
                else:
                    power += 1
            for divider in range(2, num_figures+1):
                pieces = []
                if num_figures % divider == 0:
                    num_figures_cpy = num_figures
                    num_cpy = num
                    for j in range(divider):
                        pieces.append(int(num_cpy / pow(10, num_figures_cpy - num_figures/ divider)))
                        num_cpy = int(num_cpy - pieces[-1] * pow(10, num_figures_cpy - num_figures/ divider))
                        num_figures_cpy -= int(num_figures / divider)
                    all_equal = True
                    for k in range (len(pieces)-1):
                        if pieces[k] != pieces[k+1] :
                            all_equal = False
                    if all_equal:
                        solution2 += num
                        break
    print(solution2)