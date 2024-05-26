# Import Libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def define_SE_Disponibilidad_Personal(pedido, cap_almacen):

    pedido_pers = ctrl.Antecedent(np.arange(0, 101, 1), 'pedido_pers')
    capacidad_almacen = ctrl.Antecedent(np.arange(0, 101, 1), 'capacidad_almacen')
    disponibilidad_personal = ctrl.Consequent(np.arange(0, 101, 1), 'disponibilidad_personal')

    pedido_pers['bajo'] = fuzz.trimf(pedido_pers.universe, [0, 0, 50])
    pedido_pers['medio'] = fuzz.trimf(pedido_pers.universe, [0, 50, 100])
    pedido_pers['alto'] = fuzz.trimf(pedido_pers.universe, [50, 100, 100])

    capacidad_almacen['baja'] = fuzz.trimf(capacidad_almacen.universe, [0, 0, 50])
    capacidad_almacen['media'] = fuzz.trimf(capacidad_almacen.universe, [0, 50, 100])
    capacidad_almacen['alta'] = fuzz.trimf(capacidad_almacen.universe, [50, 100, 100])
    capacidad_almacen.view()

    disponibilidad_personal['baja'] = fuzz.trimf(disponibilidad_personal.universe, [0, 0, 50])
    disponibilidad_personal['media'] = fuzz.trimf(disponibilidad_personal.universe, [0, 50, 100])
    disponibilidad_personal['alta'] = fuzz.trimf(disponibilidad_personal.universe, [50, 100, 100])
    disponibilidad_personal.view()

    # Definir las reglas difusas
    rule4 = ctrl.Rule(pedido_pers['alto'] & capacidad_almacen['baja'], disponibilidad_personal['alta'])
    rule5 = ctrl.Rule(pedido_pers['bajo'] & capacidad_almacen['alta'], disponibilidad_personal['media'])
    rule6 = ctrl.Rule(pedido_pers['medio'] & capacidad_almacen['media'], disponibilidad_personal['alta'])
    rule4.view()
    rule5.view()
    rule6.view()

    # Crear el sistema de control difuso
    sistema_ctrl_pers = ctrl.ControlSystem([rule4, rule5, rule6])
    sistema_pers = ctrl.ControlSystemSimulation(sistema_ctrl_pers)

    # Proveer entradas al sistema y calcular
    sistema_pers.input['pedido_pers'] = pedido
    sistema_pers.input['capacidad_almacen'] = cap_almacen
    sistema_pers.compute()

    # Resultado
    print(sistema_pers.output['disponibilidad_personal'])
    disponibilidad_personal.view(sim=sistema_pers)
    plt.show()
    return sistema_pers.output['disponibilidad_personal']