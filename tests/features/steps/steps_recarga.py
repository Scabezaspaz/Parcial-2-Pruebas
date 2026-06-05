import pytest
from pytest_bdd import given, when, then, scenarios, parsers

scenarios('../recarga.feature')


@given(parsers.parse('un monto de recarga de {monto:d}'), target_fixture='monto_recarga')
def monto_recarga(monto):
    return monto


@given('el usuario es premium', target_fixture='usuario_premium')
def usuario_premium():
    return True


@when('proceso la recarga', target_fixture='procesar_recarga')
def procesar_recarga(monto_recarga, usuario_premium):
    from src.recarga import calcular_recarga
    try:
        resultado = calcular_recarga(monto_recarga, premium=usuario_premium)
        return {"ok": True, "data": resultado}
    except ValueError as e:
        return {"ok": False, "error": str(e)}


@then('debe lanzar un error de monto fuera de rango')
def verificar_error(procesar_recarga):
    assert procesar_recarga["ok"] is False


@then(parsers.parse('la bonificacion debe ser {bono:d}'))
def verificar_bonificacion(procesar_recarga, bono):
    assert procesar_recarga["data"]["bonificacion"] == bono


@then(parsers.parse('el resultado debe ser {resultado}'))
def verificar_resultado_limite(procesar_recarga, resultado):
    if resultado == "error":
        assert procesar_recarga["ok"] is False
    else:
        assert procesar_recarga["ok"] is True