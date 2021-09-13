from django.db import models


class Base(models.Model):
    register_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)
    activated = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        abstract = True


class Department(Base):
    department = models.CharField(max_length=80, verbose_name='Departamento')
    supervisor = models.CharField(max_length=100, verbose_name='Surpervisor')

    def __str__(self):
        return self.department

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('departments:department_list')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
