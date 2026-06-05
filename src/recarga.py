MONTO_MINIMO = 1000
MONTO_MAXIMO = 50000
UMBRAL_BONO_ALTO = 30000
UMBRAL_BONO_MEDIO = 10000
BONO_ALTO = 25
BONO_MEDIO = 10
BONO_PREMIUM = 5


def _validar_monto(monto):
    if monto < MONTO_MINIMO or monto > MONTO_MAXIMO:
        raise ValueError(f"Monto fuera de rango. Debe estar entre ${MONTO_MINIMO} y ${MONTO_MAXIMO}")


def _calcular_bonificacion_base(monto):
    if monto >= UMBRAL_BONO_ALTO:
        return BONO_ALTO
    if monto >= UMBRAL_BONO_MEDIO:
        return BONO_MEDIO
    return 0


def calcular_recarga(monto, premium=False):
    _validar_monto(monto)
    bonificacion = _calcular_bonificacion_base(monto)

    if premium and bonificacion > 0:
        bonificacion += BONO_PREMIUM

    return {
        "monto": monto,
        "bonificacion": bonificacion,
        "total": monto * (1 + bonificacion / 100)
    }