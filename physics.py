from const import *
from maths import *
import setting

particles = []
border_particles = []

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

    def update_position(self) -> None:
        self.x += self.vx * DELTA
        self.y += self.vy * DELTA
    
    def update_velocity(self) -> None:
        self.vx = self.force[0] * DELTA / self.density
        self.vy = self.force[1] * DELTA / self.density

    def gravity(self) -> None:
        self.force[1] += G * MASS
    
    def wall_colision(self) -> None:
        if self.x < RAD or self.x > X_RES - RAD:
            self.vx = -self.vx
        if self.y < RAD or self.y > Y_RES - RAD:
            self.vy = -self.vy

    def calc_density(self) -> None:
        self.density = 0.0001

        for particle in particles:
            if particle.id != self.id:
                dst = distance(self.x, particle.x, self.y, particle.y)
                influence = smothing_kernel(dst)
                self.density += MASS * influence
    
    def calc_density_gradient(self) -> None:
        self.density_gradient = [0,0]
        for particle in particles:
            if self.id != particle.id:
                dst = distance(self.x, particle.x, self.y, particle.y)
                if dst < S_RAD:
                    dir = [(particle.x - self.x) / dst, (particle.y - self.y) / dst]
                    slope = smothing_kernel_gradient(dst)
                    self.density_gradient[0] += MASS * slope * dir[0]
                    self.density_gradient[1] += MASS * slope * dir[1]

    def convert_density_to_pressure(self) -> float:
        delta_density = self.density - TARGET_DENSITY
        pressure = delta_density * PRESSURE_MULTIPLIER
        return pressure

    def calculate_pressure_force(self) -> None:
        self.force = [0,0]

        for particle in particles:
            if self.id != particle.id:
                dst = distance(self.x, particle.x, self.y, particle.y)
                if dst < S_RAD:
                    dir = [(particle.x - self.x) / dst, (particle.y - self.y) / dst]
                    slope = smothing_kernel_gradient(dst)
                    particle.force[0] -= self.convert_density_to_pressure() * dir[0] * slope * MASS / particle.density
                    particle.force[1] -= self.convert_density_to_pressure() * dir[1] * slope * MASS / particle.density
                    self.force[0] += self.convert_density_to_pressure() * dir[0] * slope * MASS / self.density
                    self.force[1] += self.convert_density_to_pressure() * dir[1] * slope * MASS / self.density
                    
        
    def update_color(self) -> None:
        self.color = (min(max(80,255 * 1000 * (self.density - TARGET_DENSITY)), 255), 80, min(max(80, 255 * 1000 *(TARGET_DENSITY - self.density)), 255))


    def update(self) -> None:     
        self.calc_density()
        self.update_color()
        self.calc_density_gradient()
        self.calculate_pressure_force()
        if setting.GRAVITY == 1:
            self.gravity()
        self.update_velocity()
        self.wall_colision()
        self.update_position()

def update():
    for particle in particles:
        particle.update()
