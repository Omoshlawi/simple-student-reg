from django.db import models


# Create your models here.


class Students(models.Model):
    tt_number = models.CharField(max_length=50, primary_key=True)
    full_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)
    centre_code = models.CharField(max_length=50)
    centre_name = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    trade_code = models.CharField(max_length=50)
    trade_name = models.CharField(max_length=50)
    test_series = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    photo_link = models.CharField(max_length=50)

    def get_field_values(self):
        return map(
            lambda field: {'name': str(field).upper().replace("_", " "), 'value': getattr(self, field)},
            [field.name for field in Students._meta.fields]
        )

    def get_image(self):
        return "-".join(str(self.tt_number).split("/")[1:]) + ".jpg"
