#Barna Alimu

import urllib.request

website = "http://cs1110.cs.virginia.edu/files/louslist/"
url = website
course_list = []


def instructor_lectures(department, instructor):
    """
    this function is going to go through the link, and search for the classes that the instructor teaches
    :param department: str name of the department
    :param instructor: str name of the instructor
    :return: a list of classes the instructor teaches
    """
    global url
    global course_list
    link = url + department
    s = urllib.request.urlopen(link)
    course_list = s.read().decode('utf-8').strip().split('\n')
    for i in range(len(course_list)):
        course_list[i] = course_list[i].split('|')

    result = []
    for course in course_list:
        if instructor in course[4] and course[5] == 'Lecture':
            if course[3] not in result:
                result.append(course[3])
    s.close()
    return result

def compatible_classes(first_class, second_class, needs_open_space = False):
    """
    this function is going to check if first and second class has open space and compatible time wise
    :param first_class: str name of first class
    :param second_class: str name of second class
    :param needs_open_space: boolean which indicates if there is open space
    :return: boolean true or false if two classes are compatible
    """
    global url
    global course_list
    class1 = first_class.replace("-", " ")
    class1 = class1.split(" ")
    class2 = second_class.replace("-", " ")
    class2 = class2.split(" ")

    link = url + class1[0]
    s = urllib.request.urlopen(link)
    course_list = s.read().decode('utf-8').strip().split('\n')
    for i in range(len(course_list)):
        course_list[i] = course_list[i].split('|')
    for course in course_list:
        if course[0] == class1[0] and course[1] == class1[1] and course[2] == class1[2]:
            class1 = course

    link = url + class2[0]
    s = urllib.request.urlopen(link)
    course_list = s.read().decode('utf-8').strip().split('\n')
    for i in range(len(course_list)):
        course_list[i] = course_list[i].split('|')
    for course in course_list:
        if course[0] == class2[0] and course[1] == class2[1] and course[2] == class2[2]:
            class2 = course

    if needs_open_space:
        if int(class1[16])-int(class1[15]) <= 0 or int(class2[16]) - int(class2[15]) <= 0:
            return False

    for day in range(7,13):
        if class1[day] == class2[day]:
            if class1[12] == class2[12]:
                return False
            if class1[12] in range(int(class2[12]),int(class2[13])):
                return False
    s.close()
    return True
















