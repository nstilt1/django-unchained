from django.contrib.gis.db import models

# Create your models here.


#- the model itself has `title`, `description`, `address` and `employees`.

#- Use `drf` to create crud for that model.
#- Use Postgres for database.
#- Use `Postman` for testing the APIs and when they work flawlessly generate documentations with postman docs.
class Business(models.Model)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=150)
    employees = models.CharField(max_length=200)