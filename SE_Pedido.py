# Import Libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def define_SE_Pedido(inventario_value, demanda_value):

    # Definir los antecedentes (inputs) y consecuentes (outputs)
    inventario = ctrl.Antecedent(np.arange(0, 101, 1), 'inventario')
    demanda = ctrl.Antecedent(np.arange(0, 101, 1), 'demanda')
    pedido = ctrl.Consequent(np.arange(0, 101, 1), 'pedido')

    # Definir las funciones de membresía
    inventario['bajo'] = fuzz.trimf(inventario.universe, [0, 0, 50])
    inventario['medio'] = fuzz.trimf(inventario.universe, [0, 50, 100])
    inventario['alto'] = fuzz.trimf(inventario.universe, [50, 100, 100])
    inventario.view()

    demanda['baja'] = fuzz.trimf(demanda.universe, [0, 0, 50])
    demanda['media'] = fuzz.trimf(demanda.universe, [0, 50, 100])
    demanda['alta'] = fuzz.trimf(demanda.universe, [50, 100, 100])
    demanda.view()

    pedido['bajo'] = fuzz.trimf(pedido.universe, [0, 0, 50])
    pedido['medio'] = fuzz.trimf(pedido.universe, [0, 50, 100])
    pedido['alto'] = fuzz.trimf(pedido.universe, [50, 100, 100])
    pedido.view()

    # Definir las reglas difusas
    rule1 = ctrl.Rule(inventario['bajo'] & demanda['alta'], pedido['alto'])
    rule2 = ctrl.Rule(inventario['medio'] & demanda['media'], pedido['medio'])
    rule3 = ctrl.Rule(inventario['alto'] & demanda['baja'], pedido['bajo'])
    rule1.view()
    rule2.view()
    rule3.view()

    # Crear el sistema de control difuso
    sistema_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

    # Proveer entradas al sistema y calcular
    sistema.input['inventario'] = inventario_value
    sistema.input['demanda'] = demanda_value
    sistema.compute()

    # Resultado
    print(sistema.output['pedido'])
    pedido.view(sim=sistema)
    plt.show()

    return sistema.output['pedido']