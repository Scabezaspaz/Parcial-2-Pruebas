Feature: Calculo de recargas de celular
  Como usuario de RecargaYa
  Quiero recargar mi celular
  Para recibir datos con posibles bonificaciones

  Scenario: Monto invalido por debajo del minimo
    Given un monto de recarga de 500
    When proceso la recarga
    Then debe lanzar un error de monto fuera de rango

  Scenario: Recarga valida sin bonificacion
    Given un monto de recarga de 5000
    When proceso la recarga
    Then la bonificacion debe ser 0

  Scenario: Recarga valida con bonificacion del 10 por ciento
    Given un monto de recarga de 15000
    When proceso la recarga
    Then la bonificacion debe ser 10

  Scenario: Recarga valida con bonificacion del 25 por ciento
    Given un monto de recarga de 35000
    When proceso la recarga
    Then la bonificacion debe ser 25

  Scenario: Usuario premium obtiene bonificacion adicional
    Given un monto de recarga de 15000
    And el usuario es premium
    When proceso la recarga
    Then la bonificacion debe ser 15

  Scenario Outline: Valores limite del monto de recarga
    Given un monto de recarga de <monto>
    When proceso la recarga
    Then el resultado debe ser <resultado>

    Examples:
      | monto | resultado |
      | 999   | error     |
      | 1000  | valido    |
      | 50000 | valido    |
      | 50001 | error     |