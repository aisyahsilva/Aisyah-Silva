# test_employee.py
import pytest
from employee import Employee

@pytest.fixture
def employee_instance():
    """Membuat instance Employee agar dapat digunakan kembali oleh fungsi tes."""
    employee = Employee("budi", "santoso", 60000)
    return employee

def test_give_default_raise(employee_instance):
    """Menguji bahwa kenaikan gaji default sebesar $5,000 bekerja dengan benar."""
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 65000

def test_give_custom_raise(employee_instance):
    """Menguji bahwa kenaikan gaji kustom bekerja dengan benar."""
    employee_instance.give_raise(10000)
    assert employee_instance.annual_salary == 70000  # Gaji awal fixture adalah 60.000 + 10.000