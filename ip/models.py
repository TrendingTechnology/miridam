from django.db import models


class Base(models.Model):
    register_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)
    activated = models.BooleanField(default=True)

    class Meta:
        abstract = True


class IPv4(Base):
    ipv4_address = models.GenericIPAddressField(unique=True, protocol='IPv4', verbose_name='Endereço IPv4:',
                                         help_text='Exemplo: <a>192.168.0.12</a>.')
    department = models.CharField(max_length=80, verbose_name='Departamento:',
                                  help_text='Departamento: <a>Administração</a>')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('ip:list_ipv4', kwargs={'pk': self.pk})

    def __str__(self):
        return self.ipv4_address

    class Meta:
        verbose_name = 'Endereço IPv4'
        verbose_name_plural = 'Endereços IPv4'
        ordering = ['register_in']
