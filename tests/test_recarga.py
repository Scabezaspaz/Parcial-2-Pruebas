import pytest
from src.recarga import calcular_recarga

# --- Particion de equivalencia ---

def test_monto_invalido_bajo():
    with pytest.raises(ValueError):
        calcular_recarga(500)

def test_monto_invalido_alto():
    with pytest.raises(ValueError):
        calcular_recarga(60000)

def test_monto_valido_sin_bonificacion():
    resultado = calcular_recarga(5000)
    assert resultado["bonificacion"] == 0

def test_monto_valido_bono_10():
    resultado = calcular_recarga(15000)
    assert resultado["bonificacion"] == 10

def test_monto_valido_bono_25():
    resultado = calcular_recarga(35000)
    assert resultado["bonificacion"] == 25

# --- Valores limite ---

def test_limite_inferior_invalido():
    with pytest.raises(ValueError):
        calcular_recarga(999)

def test_limite_inferior_valido():
    resultado = calcular_recarga(1000)
    assert resultado["bonificacion"] == 0

def test_limite_bono_10_exacto():
    resultado = calcular_recarga(10000)
    assert resultado["bonificacion"] == 10

def test_limite_bono_25_exacto():
    resultado = calcular_recarga(30000)
    assert resultado["bonificacion"] == 25

def test_limite_superior_valido():
    resultado = calcular_recarga(50000)
    assert resultado["bonificacion"] == 25

def test_limite_superior_invalido():
    with pytest.raises(ValueError):
        calcular_recarga(50001)

# --- Premium ---

def test_premium_agrega_5_sobre_bono_10():
    resultado = calcular_recarga(15000, premium=True)
    assert resultado["bonificacion"] == 15

def test_premium_agrega_5_sobre_bono_25():
    resultado = calcular_recarga(35000, premium=True)
    assert resultado["bonificacion"] == 30

def test_premium_sin_bono_base():
    resultado = calcular_recarga(5000, premium=True)
    assert resultado["bonificacion"] == 0