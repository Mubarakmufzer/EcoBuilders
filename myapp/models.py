from django.db import models

# Create your models here.
#1. user_login - id, uname, passwd, u_type
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.uname},{self.id}'


#2. staff_details - id, user_id, fname, lname, desg_id, addr, pin, email, contact, status
class staff_details(models.Model):
    #id
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    desg_id = models.IntegerField()
    addr = models.CharField(max_length=500)
    pin = models.CharField(max_length=10)
    email = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    status = models.CharField(max_length=10)

#3. customer_details - id, user_id, fname, lname, dob, gender, addr, pin, email, contact, status
class customer_details(models.Model):
    # id
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    addr = models.CharField(max_length=1000)
    pin = models.CharField(max_length=10)
    email = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    status = models.CharField(max_length=10)

#4. designation_master - id, designation_name
class designation_master(models.Model):
    #id
    designation_name = models.CharField(max_length=100)

#5. category_master - id, category_name
class category_master(models.Model):
    #id
    category_name = models.CharField(max_length=100)

#6. quotation_master - id, user_id, customer_id, q_descp, q_file, dt, tm, status
class quotation_master(models.Model):
    #id
    user_id = models.IntegerField()
    category_id = models.IntegerField()
    q_descp = models.CharField(max_length=1000)
    q_file = models.CharField(max_length=100)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=10)

#7. quotation_details - id, quotation_id, user_id, remarks, dt, tm
class quotation_details(models.Model):
    #id
    quotation_id = models.IntegerField()
    user_id = models.IntegerField()
    remarks = models.CharField(max_length=1000)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)

#8. quotation_reply - id, user_id, quotation_id, reamrks, amt, amt_details, plan_file, dt, tm
class quotation_reply(models.Model):
    #id
    user_id = models.IntegerField()
    quotation_id = models.IntegerField()
    remarks = models.CharField(max_length=1000)
    amt = models.FloatField()
    amt_details = models.CharField(max_length=1000)
    plan_file = models.CharField(max_length=100)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    esdt = models.CharField(max_length=20)
    eedt = models.CharField(max_length=20)


#9. messages - id, user1_id, user2_id, msg, dt, tm, status
class messages(models.Model):
    #id
    user1_id = models.IntegerField()
    user2_id = models.IntegerField()
    msg = models.CharField(max_length=1000)
    dt = models.CharField(max_length=20)
    tm = models.CharField(max_length=20)
    status = models.CharField(max_length=10)

class contact_us(models.Model):
    #id
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=100)
    msg = models.CharField(max_length=1000)
