import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Merlin@1998',
    database="chatbot2_db")
mydb.autocommit = True

class queryresource:
    def __init__(self):
        self.result = None

    def save_hiring(self, compy_name, poc, mail, num, req_tech, num_of_cand):
        mycursor = mydb.cursor()
        insert_stmt = "INSERT INTO hiring( recruiter_company, place_of_contact, Mail, phn_number, required_technology, number_of_candidates_required ) VALUES (%s,%s, %s, %s,%s,%s)"
        data = [compy_name, poc, mail, num, req_tech, num_of_cand]
        mycursor.execute(insert_stmt, data)

    def pull_data(self):
        sql = "SELECT course_name FROM courses"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        result = []
        for row in myresult:
            print(row[0])

    def course_details(self, course):
        sql = ("SELECT students_placed, hiring_partners FROM courses WHERE course_name = '%s'" %course)
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for row in myresult:
            print("Good choice; " + str(row[0]) + " students have attended this course in past. " + row[1] + " are the key hiring companies for this technology.")

    def save_student(self,name, email, phn_num, on_or_off):
        mycursor = mydb.cursor()
        insert_stmt = "INSERT INTO student_details( student_name, student_mail, student_phn, online_or_offline ) VALUES (%s,%s, %s, %s)"
        data = [name, email, phn_num, on_or_off]
        mycursor.execute(insert_stmt, data)

    def virtual_booking(self, date, comments):
        mycursor = mydb.cursor()
        insert_stmt = "INSERT INTO virtual_bookings( date, comments) VALUES (%s,%s)"
        data = [date, comments]
        mycursor.execute(insert_stmt, data)

