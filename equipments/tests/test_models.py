import unittest

from equipments.models import IP, ElectronicEquipment


class IpTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.ipv4 = IP(ips_address='192.168.0.1')
        self.ipv6 = IP(ips_address='2001:db8::')

    def test_str_return_ipv4(self):
        self.assertEquals(str(self.ipv4), '192.168.0.1')

    def test_str_return_ipv6(self):
        self.assertEquals(str(self.ipv6), '2001:db8::')

    def test_get_absolute_url(self):
        ip = IP.objects.get(id=1)
        self.assertEquals(ip.get_absolute_url(), '/detalhes/1/')


class EquipmentsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.equipment = ElectronicEquipment(equipment='Notebook')

    def test_str_return_equipment(self):
        self.assertEquals(str(self.equipment), 'Notebook')

    """expected = 'Notebook'
       result = str(self.equipment)
       self.assertEquals(expected, result)"""
