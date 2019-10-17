

def gcd(bigger, smaller):
    if bigger < smaller:
        bigger, smaller = smaller, bigger

    if smaller == 0:
        return bigger
    else:
        return gcd(smaller, bigger % smaller)


def lcm(first, second):
    lcm_num = (first * second) / gcd(first, second)
    return lcm_num


def addfrac(fraction1, fraction2):
    denominator = lcm(fraction1[1], fraction2[1])
    numerator = (fraction1[0] * (denominator / fraction1[1])) + (fraction2[0] * (denominator / fraction2[1]))

    answer_frac = numerator, denominator

    return answer_frac


def subfrac(fraction1, fraction2):
    denominator = lcm(fraction1[1], fraction2[1])
    numerator = (fraction1[0] * (denominator / fraction1[1])) - (fraction2[0] * (denominator / fraction2[1]))

    answer_frac = numerator, denominator

    return answer_frac


def reduce(fraction):
    gcd_num = gcd(fraction[0], fraction[1])

    answer_frac = (fraction[0] / gcd_num), (fraction[1] / gcd_num)

    return answer_frac


frac1 = 92, 34
frac2 = 54, 37


print("The gcd of 92 and 34 is " + str(gcd(frac1[0], frac1[1])))

print("\nThe lcm of 92 and 34 is " + str(lcm(frac1[0], frac1[1])))

frac_answer1 = addfrac(frac1, frac2)
print("\nThe answer to 92/34 + 54/37 is equal to " + str(frac_answer1[0]) + "/" + str(frac_answer1[1]))

frac_answer2 = subfrac(frac1, frac2)
print("\nThe answer to 92/34 - 54/37 is equal to " + str(frac_answer2[0]) + "/" + str(frac_answer2[1]))

frac_answer3 = reduce(frac1)
print("\nThe simplest form of 92/34 is equal to " + str(frac_answer3[0]) + "/" + str(frac_answer3[1]))
