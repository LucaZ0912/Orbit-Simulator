import math
from turtle import *
import turtle

wn = turtle.Screen()
wn.title = "HelloWorld"
wn.bgcolor("black")
wn.tracer(5)

# The gravitational constant G
G = 6.67428e-11

#Scale Variable (change A to zoom)
A = 100
i = 1

# Assumed scale: 100 pixels = 1AU.
AU = (149.6e6 * 1000)  # 149.6 million km, in meters.
SCALE = A / AU


class Body(Turtle):

    name = 'Body'
    mass = None
    vx = vy = 0.0
    px = py = 0.0
    T = 0
    i = 0

    def attraction(self, other):

        # Report an error if the other object is the same as this one.
        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)

        # Compute the distance of the other body.
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox - sx)
        dy = (oy - sy)
        d = math.sqrt(dx ** 2 + dy ** 2)

        # if the distance between bodies get 0 we'll
        # get a ZeroDivisionError exception further down.
        if d == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other.name))

        #absolute force of attraction
        f = G * self.mass * other.mass / (d ** 2)

        #direction of the force.
        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy



def update_info(step, bodies):
    """(int, [Body])

    Displays the status of the simulation
    """
    print('Step #{}'.format(step))
    for body in bodies:
        s = '{:<8}  Pos.={:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f}'.format(
            body.name, body.px / AU, body.py / AU, body.vx, body.vy)
        print(s)
    print()

def loop(bodies):
    """([Body])

    Never returns; loops the simulation and updating the information
    for all bodies.
    """
    timestep = 24 * 3600  # One day

    for body in bodies:
        body.penup()
        body.hideturtle()
    step = 1
    while True:

        update_info(step, bodies)
        step += 1

        force = {}
        for body in bodies:
            # Add up all of the forces on 'body'.
            total_fx = total_fy = 0.0
            for other in bodies:
                # Don't calculate the body's attraction to itself
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                total_fx += fx
                total_fy += fy

            # the total force.
            force[body] = (total_fx, total_fy)

        # Update velocities with the given force information
        for body in bodies:
            fx, fy = force[body]
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep

            # Update positions
           # body.clear()
            body.i += 1
            if body.i == body.T:
                body.clear()
                body.i = 0
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px * SCALE, body.py * SCALE)
            body.dot(4)







def main():

    sun = Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10 ** 30
    sun.pencolor('yellow')
    sun.T = 1

    earth = Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10 ** 24
    earth.px = -1 * AU
    earth.vy = 29.783 * 1000 #times 1000 to get m/sec
    earth.pencolor('blue')
    earth.T = 365

    venus = Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10 ** 23
    venus.px = 0.723 * AU
    venus.vy = -35.02 * 1000
    venus.pencolor('red')
    venus.T = 225

    mars = Body()
    mars.name = 'Mars'
    mars.mass = 6.419 * 10 ** 23
    mars.py = 1.524 * AU
    mars.vx = 24.13 * 1000
    mars.pencolor('white')
    mars.T = 687

    merkur = Body()
    merkur.name = 'Merkur'
    merkur.mass = 3.301 * 10 ** 23
    merkur.px = 0.387 * AU
    merkur.vy = 47.36 * 1000
    merkur.pencolor('grey')
    merkur.T = 88

    jupiter = Body()
    jupiter.name  = 'Jupiter'
    jupiter.mass = 1.889 * 10 ** 27
    jupiter.px = 5.203 * AU
    jupiter.vy = 13.07 * 1000
    jupiter.pencolor("orange")
    jupiter.T = 4329

    saturn = Body()
    saturn.name = 'Saturn'
    saturn.mass = 5.62 * 10 ** 26
    saturn.px = 9.58 *AU
    saturn.vy = 9.62 * 1000
    saturn.pencolor('brown')
    saturn.T = 10751

    uranus = Body()
    uranus.name = 'Uranus'
    uranus.mass = 8.68 * 10 ** 25
    uranus.px = 19.201 * AU
    uranus.vy = 6.81 * 1000
    uranus.pencolor('green')
    uranus.T = 30664

    neptun = Body()
    neptun.name = 'Neptun'
    neptun.mass = 1.02 * 10 ** 26
    neptun.py = 30.07 * AU
    neptun.vx = 5.43 * 1000
    neptun.pencolor('blue')
    neptun.T = 60184

    
    sun2 = Body()
    sun2.name = "SecondSun"
    sun2.mass = 2 * 10 ** 30
    sun2.px =  8 *AU
    sun2.py =  3 *AU
    sun2.vx = -20 * 1000
    sun2.pencolor("yellow")
    sun.T = 10000000
    
    
    #you can add other objects here! in form of
    
    #planet = Body()                    
    #planet.name = Planetname               the planet's name
    #planet.mass = xx * xx ** xx            the planet's mass
    #planet.py = xx * AU                    the plant's start distance to the sun
    #planet.vx = xx * 1000                  the planet's start velocity
    #planet..pencolor("color")              the planet's display color
    #planet.T = xxxxx                       Time until the "line" will be deleted
    
    
    #you have call the bodies you want to display in the loop function!

    loop([sun, earth, venus, mars, merkur, jupiter, saturn, uranus, neptun])


if __name__ == '__main__':
    main()
