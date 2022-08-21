def first_word(sentence='Hello World'):
    if sentence == str(sentence):
        return sentence.split()[0]
    else:
        return False


print(first_word('Good Day'))




def average(*args):
    sum_of_numbers = sum(args)
    answer = sum_of_numbers / len(args)

    return int(answer)
print(average(2,3,6,7,8,9,3,5))



def check_password(password):
    if len(password) >= 6 and not password.isdigit() and not password.isalpha():
        return True
    else:
        return False
print(check_password('bxf456jd'))





