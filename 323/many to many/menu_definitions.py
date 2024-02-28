# Import required modules
from Menu import Menu
from Option import Option
from constants import *

# The main options for operating on Departments and Courses.
menu_main = Menu('main', 'Please select one of the following options:', [
    Option("Add", "add(sess)"),
    Option("List", "list_objects(sess)"),
    Option("Delete", "delete(sess)"),
    Option("Boilerplate Data", "boilerplate(sess)"),
    Option("Commit", "sess.commit()"),
    Option("Rollback", "session_rollback(sess)"),
    Option("Exit this application", "pass")
])

# The menu for adding new records with "Add" option.
add_menu = Menu('add', 'Please indicate what you want to add:', [
    Option("Department", "add_department(sess)"),
    Option("Course", "add_course(sess)"),
    Option("Major", "add_major(sess)"),
    Option("Student", "add_student(sess)"),
    Option("Student to Major", "add_student_major(sess)"),
    Option("Major to Student", "add_major_student(sess)"),
    Option("Section", "add_section(sess)"),
    Option("Enroll Student in Section", "add_student_to_section(sess)"),
    Option("Exit", "pass")
])

# The menu for deleting records with "Delete" option.
delete_menu = Menu('delete', 'Please indicate what you want to delete from:', [
    Option("Department", "delete_department(sess)"),
    Option("Course", "delete_course(sess)"),
    Option("Major", "delete_major(sess)"),
    Option("Student", "delete_student(sess)"),
    Option("Student to Major", "delete_student_major(sess)"),
    Option("Major to Student", "delete_major_student(sess)"),
    Option("Section", "delete_section(sess)"),
    Option("Unenroll Student from Section", "delete_student_from_section(sess)"),
    Option("Exit", "pass")
])

# The menu for listing records with "List" option.
list_menu = Menu('list', 'Please indicate what you want to list:', [
    Option("Department", "list_department(sess)"),
    Option("Course", "list_course(sess)"),
    Option("Major", "list_major(sess)"),
    Option("Student", "list_student(sess)"),
    Option("Student to Major", "list_student_major(sess)"),
    Option("Major to Student", "list_major_student(sess)"),
    Option("Sections", "list_sections(sess)"),
    Option("List Enrollments by Student", "list_student_enrollments(sess)"),
    Option("List Enrollments by Section", "list_department_courses(sess)"),
    Option("Exit", "pass")
])

# A menu to prompt for the amount of logging information to go to the console.
debug_select = Menu('debug select', 'Please select a debug level:', [
    Option("Informational", "logging.INFO"),
    Option("Debug", "logging.DEBUG"),
    Option("Error", "logging.ERROR")
])

# A menu to prompt for whether to create new tables or reuse the old ones.
introspection_select = Menu("introspection selectt", 'To introspect or not:', [
    Option('Start all over', START_OVER),
#   Option("Reuse tables", INTROSPECT_TABLES),
    Option("Reuse without introspection", REUSE_NO_INTROSPECTION)
])