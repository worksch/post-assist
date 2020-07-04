from django.db import models

# Create your models here.
class Address(models.Model):
    #id = models.IntegerField()          # 全局编号,由Django自动维护
    course_id = models.IntegerField()   # 课序号，iCenter
    class_room = models.CharField(max_length=20)    # 教室，iCenter
    student_id = models.CharField(max_length=16)    #  学号
    student_name = models.CharField(max_length=50)  # 学生姓名
    student_gender = models.IntegerField()          # 性别
    department = models.CharField(max_length=50)    # 院系
    class_name = models.CharField(max_length=50)    # 班级
    student_type = models.IntegerField()            # 学生类别：本科生
    student_phone = models.CharField(max_length=18) # phone
    student_email = models.CharField(max_length=50) # email

    def __str__(self):
        return self.course_id

    class Meta:
        db_table = "student_address"