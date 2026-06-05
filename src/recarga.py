def calcular_recarga(monto, premium=False):
    if monto < 1000 or monto > 50000:
        raise ValueError("Monto fuera de rango")
    
    if monto >= 30000:
        bonificacion = 25
    elif monto >= 10000:
        bonificacion = 10
    else:
        bonificacion = 0
    
    if premium and bonificacion > 0:
        bonificacion += 5
    
    return {
        "monto": monto,
        "bonificacion": bonificacion,
        "total": monto * (1 + bonificacion / 100)
    }