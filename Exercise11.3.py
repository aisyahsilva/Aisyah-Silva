# test_employee.py
from employee import Employee

def test_give_default_raise():
    """Menguji bahwa kenaikan gaji default sebesar $5,000 bekerja dengan benar."""
    employee = Employee("budi", "santoso", 60000)
    employee.give_raise()
    assert employee.annual_salary == 65000

def test_give_custom_raise():
    """Menguji bahwa kenaikan gaji kustom bekerja dengan benar."""
    employee = Employee("siti", "aminah", 70000)
    employee.give_raise(10000)
    assert employee.annual_salary == 80000