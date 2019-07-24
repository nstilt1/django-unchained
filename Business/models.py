from django.db import models

# Create your models here.


#- the model itself has `title`, `description`, `address` and `employees`.

#- Use `drf` to create crud for that model.
#- Use Postgres for database.
#- Use `Postman` for testing the APIs and when they work flawlessly generate documentations with postman docs.
class Business(models.Model):
    employees = models.ForeignKey(
        'Employee',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=150)
    id = models.AutoField(primary_key=True)
    

class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)