from django.db import models

# Create your models here.
class Address(models.Model):
    #id = models.IntegerField()          # 全局编号,由Django自动维护
    course_id = models.CharField(max_length=100)                    # B课序号，iCenter
    class_room = models.CharField(max_length=50)                    # D教室，iCenter
    student_id = models.CharField(max_length=50)                    # E学号
    student_name = models.CharField(max_length=50)                  # F学生姓名
    weixin_group = models.CharField(max_length=20, null=True)       # G加群
    student_gender = models.CharField(max_length=50, null=True)     # H性别
    department = models.CharField(max_length=50)        # I院系
    class_name = models.CharField(max_length=50)        # J班级
    student_type = models.CharField(max_length=50, null=True)       # K学生类别：本科生
    student_phone = models.CharField(max_length=50, null=True)      # L学生联系方式
    student_email = models.CharField(max_length=100, null=True)     # M学生电子邮箱
    delivery_name = models.CharField(max_length=100, null=True)     # N收货人姓名
    delivery_phone = models.CharField(max_length=100, null=True)    # O收货人手机
    delivery_address_cn = models.CharField(max_length=200, null=True)   # P收货人地址中文
    delivery_address_en = models.CharField(max_length=200, null=True)   # Q收货人地址英文
    delivery_zipcode = models.CharField(max_length=50, null=True)       # R收货人邮编
    last_update_date = models.CharField(max_length=20, null=True)       #2020/08/30 12:30:59

    def __str__(self):
        return self.course_id

    class Meta:
        db_table = "student_address"