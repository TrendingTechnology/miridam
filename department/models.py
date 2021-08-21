from django.db import models


class Department(models.Model):
    department = models.CharField(max_length=80, verbose_name='Departamento')

    def __str__(self):
        return self.department

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'