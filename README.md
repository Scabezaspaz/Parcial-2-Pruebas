# RecargaYa S.A.S. — Modulo de Recargas

## Reglas de negocio
- El monto debe estar entre $1.000 y $50.000
- Recargas de $10.000 o mas reciben 10% de datos de bonificacion
- Recargas de $30.000 o mas reciben 25% de datos de bonificacion
- Usuarios premium obtienen 5% adicional sobre cualquier bonificacion

## Tecnologia
- **Lenguaje:** Python 3.13
- **Tests unitarios:** pytest
- **BDD:** pytest-bdd con Gherkin
- **API REST:** FastAPI
- **Rendimiento:** Locust
- **CI/CD:** GitHub Actions

## Comandos para ejecutar cada tipo de prueba

### Tests unitarios
```bash
pytest tests/test_recarga.py -v
```

### Tests BDD
```bash
pytest tests/features/steps/steps_recarga.py -v
```

### API REST
```bash
uvicorn src.main:app --reload
```

### Tests de rendimiento
```bash
locust -f locustfile.py --headless -u 30 -r 5 --run-time 30s --host http://localhost:8000
```

---

## Tabla de casos de prueba

### Particion de equivalencia — Monto de recarga

| ID | Particion | Monto | Resultado esperado | Tipo |
|---|---|---|---|---|
| CP01 | Invalida baja | 500 | Error: monto fuera de rango | Negativo |
| CP02 | Valida sin bono | 5000 | Sin bonificacion | Positivo |
| CP03 | Valida con bono 10% | 15000 | 10% bonificacion | Positivo |
| CP04 | Valida con bono 25% | 35000 | 25% bonificacion | Positivo |
| CP05 | Invalida alta | 60000 | Error: monto fuera de rango | Negativo |

### Valores limite — Monto de recarga

| ID | Valor | Dentro del rango | Resultado esperado | Tipo |
|---|---|---|---|---|
| CP06 | 999 | No | Error: monto fuera de rango | Borde |
| CP07 | 1000 | Si | Sin bonificacion | Borde |
| CP08 | 1001 | Si | Sin bonificacion | Borde |
| CP09 | 9999 | Si | Sin bonificacion | Borde |
| CP10 | 10000 | Si | 10% bonificacion | Borde |
| CP11 | 50000 | Si | 25% bonificacion | Borde |
| CP12 | 50001 | No | Error: monto fuera de rango | Borde |