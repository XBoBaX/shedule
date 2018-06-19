from config import *

API_URL = "https://artncoprojects.000webhostapp.com/Raspisanie/api/{0}".format(SECURITY_API)

TEACHER_LIST = "{0}/teacherList".format(API_URL)
TEACHER_LIST_UKR = "{0}/teacherListUkr".format(API_URL)

TEACHER_SCHEDULE = "{0}/teacherSchedule/all".format(API_URL)
STUDENT_SHEDULE = "{0}/schedule/all".format(API_URL)

STUDENT_LIST = "{0}/groupList".format(API_URL)

