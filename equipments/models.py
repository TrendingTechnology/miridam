from django.db import models

from department.models import Department

EQUIPMENT_TYPE_CHOICES = (
    ('TV', 'TV'),
    ('DESKTOP', 'DESKTOP'),
    ('NOTEBOOK', 'NOTEBOOK'),
    ('SOM', 'SOM'),
    ('ROTEADOR', 'ROTEADOR'),
    ('CÀMERA', 'CÂMERA'),
    ('OUTROS', 'OUTROS'),
)


class Base(models.Model):
    register_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)
    activated = models.BooleanField(default=True, verbose_name='IP ativado?')

    class Meta:
        abstract = True


class IP(Base):
    ips_address = models.GenericIPAddressField(unique=True, protocol='IPv4', verbose_name='Endereço IP')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('ip:detail_ip', kwargs={'pk': self.pk})

    def __str__(self):
        return self.ips_address

    class Meta:
        verbose_name = 'Endereço IP'
        verbose_name_plural = 'Endereços IPs'
        ordering = ['register_in']


class ElectronicEquipment(Base):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, max_length=80,
                                   verbose_name='Departamento')
    equipment = models.CharField(max_length=80, verbose_name='Identificação')
    type = models.CharField(max_length=8, choices=EQUIPMENT_TYPE_CHOICES, verbose_name='Tipo')
    ip = models.OneToOneField(IP, on_delete=models.CASCADE, verbose_name='IP')

    def __str__(self):
        return self.equipment

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
        ordering = ['register_in']
