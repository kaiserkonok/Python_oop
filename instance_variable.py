class BestCourses:
    website = 'http://www.example.com'

    def __init__(self, course_name):
        self.course_name = course_name


best_course_1 = BestCourses('Python All you Need to Know')

print(best_course_1.website)

print(best_course_1.course_name)
