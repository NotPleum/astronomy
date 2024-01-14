#! /usr/bin/env python3
from math import pi, sqrt

# Generic astronomic object
class AstroObject():
    def __init__(self, name, radius, mass):
        self.name = name
        self.radius = radius    #km
        self.mass = mass        #kg
    
    def say_hello(self):
        print("%"*10)
        print(f'object: {self.name}\nradius: {self.radius:.2e} km\nmass: {self.mass:.2e} kg')
    
    def get_volume(self):
        volume =  4 / 3 * pi * self.radius ** 3
        print(f'The volume of {self.name} is {volume:.2e} km3.')

    # surface area
    def get_surface_area(self):
        s_area = 4 * pi * self.radius ** 2
        print(f'The surface area of {self.name} is {s_area:.2e} km2.')

# planet object
class Planet(AstroObject):
    # override method
    def say_hello(self):
        print("%"*10)
        print(f'planet: {self.name}\nradius: {self.radius:.2e} km\nmass: {self.mass:.2e} kg')



class Moon(AstroObject):
    
    def __init__(self, name, radius, mass, semimajor_axis, planet):
        self.planet_name = planet.name
        self.planet_mass = planet.mass           # kg
        self.semimajor_axis = semimajor_axis    #km
        super().__init__(name, radius, mass)

    # override method
    def say_hello(self):
        print("%"*10)
        print(f'moon: {self.name}\norbit around: {self.planet_name}\nradius: {self.radius:.2e} km\nmass: {self.mass:.2e} kg')


    def get_period_rotation(self):

        # TASK 1: WRITE YOUR CODE HERE
        # BEGIN
        # Gravitational constant
        G = 6.67e-11
        # calculation
        period_rotation_squared = (4 * pi ** 2 / G / self.planet_mass) * self.semimajor_axis ** 3
        period_rotation_seconds = sqrt(period_rotation_squared)
        period_rotation = period_rotation_seconds / 86400
        # END

        # complete this code so that this line runs
        # UNCOMMENT THE NEXT LINE
        print(f'period of rotation around {self.planet_name} is {period_rotation:.2e} days.')


# THIS IS AN EXAMPLE OF THE THINGS YOU SHOULD DO
# I'LL DEFINE THE OBJECTS FOR THE EARTH AND OUR MOON
# AND PRINT THE RELEVANT INFORMATION
earth = Planet(name="Earth", radius=6_371, mass=5.972e24 ) # <- this is an object
moon = Moon(name="Moon", radius=3_476/2, mass=735*10**20, semimajor_axis=384400*10**3, planet=earth) # <- this is also an object

# THESE ARE THE THINGS YOU SHOULD CALL
earth.say_hello()
earth.get_volume()
earth.get_surface_area()

moon.say_hello()
moon.get_volume()
moon.get_surface_area()
# UNCOMMENT THE NEXT LINE AFTER FINISHING TASK 1
moon.get_period_rotation()


# TASK 2: CREATE THE PLANET JUPITER 
jupiter = Planet(name="Jupiter", radius=69_911, mass=1.898e27)

# TASK 3: CREATE THE 4 GALLILEAN MOONS
io = Moon(name="Io", radius=1815, mass=894, semimajor_axis=422, planet=jupiter)
europa = Moon(name="Europa", radius=1569, mass=480, semimajor_axis=671, planet=jupiter)
ganymede = Moon(name="Ganymede", radius=2631, mass=1482, semimajor_axis=1070, planet=jupiter)
callisto = Moon(name="Callisto", radius=2400, mass=1077, semimajor_axis=1883, planet=jupiter)

# TASK 4: CALL THE FUNCTIONS say_hello(), get_volume(), and get_surface_area() for JUPITER
jupiter.say_hello()
jupiter.get_volume()
jupiter.get_surface_area()

# TASK 5: CALL THE FUNCTIONS say_hello(), get_volume(), get_surface_area(), and get_period_rotation() for gallilean moons
#io
io.say_hello()
io.get_volume()
io.get_surface_area()
io.get_period_rotation()
#europa
europa.say_hello()
europa.get_volume()
europa.get_surface_area()
europa.get_period_rotation()
#ganymede
ganymede.say_hello()
ganymede.get_volume()
ganymede.get_surface_area()
ganymede.get_period_rotation()
#callisto
callisto.say_hello()
callisto.get_volume()
callisto.get_surface_area()
callisto.get_period_rotation()

# TASK 6: CREATE THE PLANET PLUTO
pluto = Planet(name="Pluto", radius=1_188.3, mass=1.31e22)

# TASK 7: CREATE THE 5 MOONS OF PLUTO
charon = Moon(name="Charon", radius=600, mass=0, semimajor_axis=19.7, planet=pluto)
nix = Moon(name="Nix", radius=23, mass=0, semimajor_axis=48, planet=pluto)
styx = Moon(name="Styx", radius=10, mass=0, semimajor_axis=42, planet=pluto)
kerberos = Moon(name="Kerberos", radius=14, mass=0, semimajor_axis=58, planet=pluto)
hydra = Moon(name="Hydra", radius=30.5, mass=0, semimajor_axis=65, planet=pluto)

# TASK 8: CALL THE FUNCTIONS say_hello(), get_volume(), and get_surface_area() for PLUTO
pluto.say_hello()
pluto.get_volume()
pluto.get_surface_area()

# TASK 9: CALL THE FUNCTIONS say_hello(), get_volume(), get_surface_area(), and get_period_rotation() for the moons of PLUTO
#charon
charon.say_hello()
charon.get_volume()
charon.get_surface_area()
charon.get_period_rotation()
#nix
nix.say_hello()
nix.get_volume()
nix.get_surface_area()
nix.get_period_rotation()
#styx
styx.say_hello()
styx.get_volume()
styx.get_surface_area()
styx.get_period_rotation()
#kerberos
kerberos.say_hello()
kerberos.get_volume()
kerberos.get_surface_area()
kerberos.get_period_rotation()
#hydra
hydra.say_hello()
hydra.get_volume()
hydra.get_surface_area()
hydra.get_period_rotation()


# TASK 10: CREATE A GITHUB ACCOUNT, CREATE A REPOSITORY, AND PUSH YOUR CODE TO GITHUB (MAKE SURE YOU SELECT PUBLIC AND NOT PRIVATE REPOSITORY)

# TASK 11: TAKE A SCREENSHOT OF YOUR TERMINAL WITH THE ALL ANSWERS AND UPLOAD THE SCREENSHOT AND GITHUB LINK TO GOOGLE CLASSROOM