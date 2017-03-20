def main():# this function is used here to import this module in main.py
    grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5] # list of grades


    def print_grades(grades): # this prints list of grades
        for grade in grades:
            print "    " + str(grade)


    def grades_sum(grades): # this prints sum of grades
        total = 0
        for grade in grades:
            total += grade
        return total


    def grades_average(grades): # this prints average of grades
        sum_of_grades = grades_sum(grades)
        average = sum_of_grades / float(len(grades))
        return average


    def grades_variance(scores): # this prints variance
        average = grades_average(scores)
        variance = 0
        for score in scores:
            variance = variance + (average - score) ** 2
        variance = variance / len(scores)
        return variance


    def grades_std_deviation(variance):
        return variance ** 0.5


    variance = grades_variance(grades)
    list_of_grades = print_grades(grades)

    print "Grades : " + str(list_of_grades)
    print "Total :" + str(grades_sum(grades))
    print "Average : " + str(grades_average(grades))
    print "Variance : " + str(variance)
    print "Standard Deviation : " + str(grades_std_deviation(variance))

