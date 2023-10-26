import pytest
from .main import konwersjanaszesnasatkowy 

def test_checks_if_a_number_is_negative():
    assert konwersjanaszesnasatkowy(-3455) == "Podana liczba jest ujemna, podaj dodatnia liczbe"
    assert konwersjanaszesnasatkowy(0) == "0"