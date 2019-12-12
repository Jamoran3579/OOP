def get_data_list(file_name):
    data_file = open(file_name, "r")
    data_list = []  #start with an empty list
    for line_str in data_file:   # strip end-of-line, split on commas, and append items to list
        data_list.append(line_str.strip().split(','))
    return data_list


def get_monthly_averages(data_list1):
    monthly_average = 0
    divisor = 0

    new_list = []

    for n in data_list:

        monthly_average = 0
        divisor = 0

        for i in data_list[n]:
            monthly_average = monthly_average + (data_list1[n][5] * data_list1[n][6])
            divisor = divisor + data_list1[n][5]

        monthly_average = monthly_average / divisor

        new_list[n][1] = monthly_average


    return new_list


data_list = get_data_list('GOOG.csv')
average_price = get_monthly_averages(data_list)

print(data_list)
