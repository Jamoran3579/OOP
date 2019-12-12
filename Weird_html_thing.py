
file1 = open("gettysburg.txt", "r")
file2 = open("tester.html", "w")
file3 = open("stopwords.txt", "r")
file2.write("!DOCTYPE html>\n<html>\n<head lang=\"en\">\n<meta charset=\"UTF-8\">\n<title>Tag Cloud Generator</title>"
            "\n</head>\n<body>\n<div style=\"text-align: center; vertical-align: middle;\nfont-family: arial; color: "
            "white; background-color:black;\nborder:1px solid black\">")

string2 = file3.read()
list2 = string2.split()
my_dictionary = {}
string1 = file1.read()
list1 = string1.split()
for word in list1:
    if word in string2:
        word = word
    else:
        if word not in my_dictionary:
            my_dictionary[word] = 0
        my_dictionary[word] += 1

file2.write("\n<")
for key in my_dictionary:
    file2.write("<span style=\"font-size: " + str(my_dictionary[key]*10) + "px\"> " + key + " </span>")

file2.write(">\n</div>\n</body>\n</html>")

file1.close()
file2.close()
file3.close()

print("Please run file tester.html")
