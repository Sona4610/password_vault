from django.db import models

class Member(models.Model):
    firstname=models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return self.firstname 

# COMMENT FOR CREATE,UPDATE,DELETE
# py manage.py makemigration
# py manage.py migrate
# py manage.py shell
# from members.models import Memeber
# m1=Memeber(firstname='aa',lastname='jj')-->insert query this is orm
# m1.save()
# Member.objects.all().values()--->view query/select 
# Member.objects.all()[0]
# #update
# m1=Member.objects.all()[0]
# m1.firstname
# m1.firstname='kaviya'
# m1.save()
# #delete
# m1.delete()