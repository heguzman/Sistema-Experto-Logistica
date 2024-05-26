# Import Libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def define_SE_Tiempo_De_Entrega(disponibilidad_personal_value, demanda_value):

    # Definir los antecedentes (inputs) y consecuentes (outputs)
    disponibilidad_personal = ctrl.Antecedent(np.arange(0, 101, 1), 'disponibilidad_personal')
    demanda = ctrl.Antecedent(np.arange(0, 101, 1), 'demanda')
    tiempo_entrega = ctrl.Consequent(np.arange(0, 101, 1), 'tiempo_entrega')

    # Definir las funciones de membresía
    disponibilidad_personal['baja'] = fuzz.trimf(disponibilidad_personal.universe, [0, 0, 50])
    disponibilidad_personal['media'] = fuzz.trimf(disponibilidad_personal.universe, [0, 50, 100])
    disponibilidad_personal['alta'] = fuzz.trimf(disponibilidad_personal.universe, [50, 100, 100])
    disponibilidad_personal.view()

    demanda['baja'] = fuzz.trimf(demanda.universe, [0, 0, 50])
    demanda['media'] = fuzz.trimf(demanda.universe, [0, 50, 100])
    demanda['alta'] = fuzz.trimf(demanda.universe, [50, 100, 100])
    demanda.view()

    tiempo_entrega['bajo'] = fuzz.trimf(tiempo_entrega.universe, [0, 0, 50])
    tiempo_entrega['medio'] = fuzz.trimf(tiempo_entrega.universe, [0, 50, 100])
    tiempo_entrega['alto'] = fuzz.trimf(tiempo_entrega.universe, [50, 100, 100])
    tiempo_entrega.view()

    # Definir las reglas difusas
    rule1 = ctrl.Rule(disponibilidad_personal['baja'] & demanda['alta'], tiempo_entrega['alto'])
    rule2 = ctrl.Rule(disponibilidad_personal['media'] & demanda['media'], tiempo_entrega['medio'])
    rule3 = ctrl.Rule(disponibilidad_personal['alta'] & demanda['baja'], tiempo_entrega['bajo'])
    rule1.view()
    rule2.view()
    rule3.view()

    # Crear el sistema de control difuso
    sistema_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

    # Proveer entradas al sistema y calcular
    sistema.input['disponibilidad_personal'] = disponibilidad_personal_value
    sistema.input['demanda'] = demanda_value
    sistema.compute()

    # Resultado
    print(sistema.output['tiempo_entrega'])
    tiempo_entrega.view(sim=sistema)
    plt.show()

    return sistema.output['tiempo_entrega']