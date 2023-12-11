from const import *
from maths import *
import setting


'''
LIST OF PARTICLE OBJECTS
'''
particles = []


'''
PARTICLE CLASS:
    ATRIBUTES:
        - id => PARTICLE ID
        - x => COORDINATE X
        - y => COORDINATE Y
        - vx => VELOCITY IN X AXLE
        - vy => VELOCITY IN Y AXLE
        - color => PARTICLE COLOR
        - density => PARTICLE DENSITY
        - density_gradient => RATE OF CHANGE OF THE PARTICLE RELATIVE TO DISTANCE
        - force => FORCE APPLIED IN THE PARTICLE
'''
class Particle():
    def __init__(self, id, x, y) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.color = (40,40,255)
        self.density = 0.0001
        self.density_gradient = [0,0]
        self.force = [0,0]

    #UPDATES POSITION 
    def update_position(self) -> None:
        self.x += self.vx * DELTA
        self.y += self.vy * DELTA
    
    #UPDATES VELOCITY
    def update_velocity(self) -> None:
        self.vx = self.force[0] * DELTA / self.density
        self.vy = self.force[1] * DELTA / self.density

    #APPLY GRAVITY IN PARTICLE
    def gravity(self) -> None:
        self.force[1] += G * MASS
    
    #DETECT COLISION WITH WALLS AND UPDATES VELOCITY
    def wall_colision(self) -> None:
        if self.x < RAD or self.x > X_RES - RAD:
            self.vx = -self.vx
        if self.y < RAD or self.y > Y_RES - RAD:
            self.vy = -self.vy

    #CALCULATE DENSITY
    def calc_density(self) -> None:
        self.density = 0.000001

        for particle in particles:
            if particle.id != self.id:
                dst = distance(self.x, particle.x, self.y, particle.y)
                if dst <= S_RAD:
                    self.density += MASS * CSK[int(dst)]

    #CALCULATE PRESSURE VALUE WITH DENSITY
    def convert_density_to_pressure(self) -> float:
        delta_density = self.density - TARGET_DENSITY
        pressure = delta_density * PRESSURE_MULTIPLIER
        return pressure

    #CALCULATE PRESSURE
    def calculate_pressure_force(self) -> None:
        self.force = [0,0]

        for particle in particles:
            if self.id != particle.id:
                dst = distance(self.x, particle.x, self.y, particle.y)
                if dst < S_RAD:
                    dir = [(particle.x - self.x) / dst, (particle.y - self.y) / dst]
                    slope = CSKG[int(dst)]
                    pressure = self.convert_density_to_pressure() * slope * MASS 
                    pressure_x = dir[0] * pressure
                    pressure_y = dir[1] * pressure
                    particle.force[0] -= pressure_x / particle.density
                    particle.force[1] -= pressure_y / particle.density
                    self.force[0] += pressure_x / self.density
                    self.force[1] += pressure_y / self.density
                    
    #UPDATES COLOR OF THE PARTICLE ACCORDING TO THE PARTICLE DENSITY
    def update_color(self) -> None:
        self.color = (min(max(80,255 * 1000 * (self.density - TARGET_DENSITY)), 255), 80, min(max(80, 255 * 1000 *(TARGET_DENSITY - self.density)), 255))

    #UPDATES PARTICLE PHYSICS
    def update(self) -> None:     
        self.calc_density()
        self.update_color()
        self.calculate_pressure_force()
        if setting.GRAVITY == 1:
            self.gravity()
        self.update_velocity()
        self.wall_colision()
        self.update_position()

'''
UPDATES ALL PARTICLES
'''
def update() -> None:
    for particle in particles:
        particle.update()
