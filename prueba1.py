import time
from matplotlib import pyplot as plt
import itertools
import matplotlib.pyplot as plot 
from pypot.creatures import PoppyHumanoid
poppy = PoppyHumanoid(simulator='vrep')

def run():
        poppy.goto_position({'l_hip_y': -39,
                                  'r_hip_y': -39,
                                  'l_knee_y': 134,
                                  'r_knee_y': 134,
                                  'abs_x': 0,
                                  'abs_y': 3,
                                  'abs_z': 0,
                                  'bust_x': 0,
                                  'bust_y': 0,
                                  },
                                 2,
                                 wait=True)


        for m in poppy.motors:
            m.compliant = True

        for m in poppy.motors:
            m.torque_limit = 20

        time.sleep(2)



def run2():
    poppy.goto_position(dict(zip((m.name for m in poppy.motors), itertools.repeat(0))), 2, wait=True)

        # Specified some motor positions to keep the robot balanced
    poppy.goto_position({'r_hip_z': -2,
                                  'l_hip_z': 2,
                                  'r_hip_x': -2,
                                  'l_hip_x': 2,
                                  'l_shoulder_x': 20,
                                  'r_shoulder_x': -20,
                                  'l_shoulder_y': 10,
                                  'r_shoulder_y': 10,
                                  'l_elbow_y': -20,
                                  'r_elbow_y': -20,
                                  'l_ankle_y': -3,
                                  'r_ankle_y': -2,
                                  'abs_y': -2,
                                  'head_y': 1,
                                  'head_z': 0},
                                 3,
                                 wait=True)

        # Restore the motor speed
    poppy.power_up()

        # Reduce max torque to keep motor temperature low
    for m in poppy.motors:
        m.torque_limit = 70

    time.sleep(1)

def setup():
    poppy.compliant = False
    poppy.power_up()

        # Change PID of Dynamixel MX motors
    for m in [m for m in poppy.motors if hasattr(m, 'pid')]:
        m.pid = (4, 2, 0)
    for m in poppy.torso:
        m.pid = (6, 2, 0)

        # Reduce max torque to keep motor temperature low
    for m in poppy.motors:
        m.torque_limit = 70

    time.sleep(0.5)

    def run(self):
        pass
    
def Saludar():
    for m in poppy.motors:
        m.moving_speed = 40 #velocidad del motor
        poppy.r_shoulder_x.goal_position = 0 #posicion ideal del hombro
        poppy.r_shoulder_x.compliant = False #
        tr = 0.6
        poppy.r_shoulder_x.goto_position(-90, tr, wait=True)
        poppy.r_arm_z.goto_position(-90, tr, wait=True)
        poppy.r_elbow_y.goto_position(-90, tr, wait=True)
        for i in range(2):
            poppy.r_elbow_y.goto_position(+90, tr, wait=True)
            poppy.r_elbow_y.goto_position(-90, tr, wait=True)


        poppy.l_shoulder_x.goal_position = 0 #posicion ideal del hombro
        poppy.l_shoulder_x.compliant = False #
        tr = 0.6
        poppy.l_shoulder_x.goto_position(90, tr, wait=True)
        poppy.l_arm_z.goto_position(195, tr, wait=True)
        poppy.l_elbow_y.goto_position(-90, tr, wait=True)
        for i in range(2):
                    poppy.l_elbow_y.goto_position(+90, tr, wait=True)
                    poppy.l_elbow_y.goto_position(-90, tr, wait=True)
       
        break

""" las piernas
r_hip_z
r_hip_y
r_hip_X

l_hip_z
l_hip_y
l_hip_x
"""
def caminar():
    tr = 0.6
    poppy.r_hip_z.goto_position(1, tr, wait=True)
    poppy.r_hip_y.goto_position(1, tr, wait=True)
    poppy.r_hip_x.goto_position(1, tr, wait=True)


    poppy.l_hip_z.goto_position(2, tr, wait=True)
    poppy.l_hip_y.goto_position(2, tr, wait=True)
    poppy.l_hip_x.goto_position(2, tr, wait=True)
    
    poppy.l_hip_z.goto_position(10, tr, wait=True)
    
 
def pruebas():
    print (poppy.l_ankle_y.present_load)
    print (poppy.r_ankle_y.present_load)
    print (poppy.l_hip_y.present_load)
    print (poppy.r_hip_y.present_load)

def inicial():       
     poppy.r_shoulder_x.goal_position = 0
     poppy.r_arm_z.goal_position = 0
     poppy.l_shoulder_x.goal_position = 0
     poppy.l_arm_z.goal_position = 0
     tr = 0.6

     poppy.r_elbow_y.goto_position(0, tr, wait=True)
     poppy.l_elbow_y.goto_position(0, tr, wait=True)

def alias():
    print(poppy.alias)

def test():
    l_hip_x=10
    for m in poppy.l_leg_sagitall:
        m.goal_position = 30

        for p in poppy.r_leg_sagitall:
            p.goal_position = 30
            
#Por defecto, cada motor imprime su nombre, su id y su posición actual
def motores():
    print(poppy.motors,"\n")

#task_saludar = Saludar()
#task_saludar

#task_caminar=caminar()
#motores()
#alias()
#test()
"""
inicial()
"""

setup()
#run()
run2()
#Mover = move()
#Mover
