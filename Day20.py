
import re

epsilon = 10000

def add_particle(particles, p, v, a):
    particles.append((p, v, a))

def tick(particle):
    p = particle[0]
    v = particle[1]
    a = particle[2]

    v = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
    p = (p[0] + v[0], p[1] + v[1], p[2] + v[2])    
    
    return (p, v, a)

def distance(p):    
    return abs(p[0]) + abs(p[1]) + abs(p[2])

def tick_all(collisions, particles):    
    min_d = None
    for i, particle in enumerate(particles):
        particles[i] = tick(particle)           
        p = particles[i][0]     
        d = distance(p)

        if p not in collisions:
            l = []
            l.append(i)
            collisions[p] = l
        else:
            l = collisions[p]
            l.append(i)

        if ((not min_d) or (d < min_d)):
            min_d = d
            idx = i            

    return (min_d, idx)
    
def read():
    particles = []
    with open("input") as f:
        for line in f:
            line_regex = re.compile("^p=<(-?\d+),(-?\d+),(-?\d+)>,\sv=<(-?\d+),(-?\d+),(-?\d+)>,\sa=<(-?\d+),(-?\d+),(-?\d+)>$")
            c = line_regex.match(line)
       
            add_particle(particles, (int(c.group(1)), int(c.group(2)), int(c.group(3))), 
                                    (int(c.group(4)), int(c.group(5)), int(c.group(6))), 
                                    (int(c.group(7)), int(c.group(8)), int(c.group(9))))
    
    return particles

def remove_collision(particles):
     for i in range(epsilon):
        collisions = {}
        tick_all(collisions, particles)        
        indexes = []
        for key, value in collisions.items():
            if (len(collisions[key]) > 1):
                indexes.extend(collisions[key])
        if (len(indexes) > 0):
            particles = [element for i, element in enumerate(particles) if i not in indexes]
           
     print("Particles left:", len(particles))

def closest_to_zero(particles):
    min_d = None
    idx = None
    collisions = {}
    for i in range(epsilon):
        (min_d, new_idx) = tick_all(collisions, particles)
        if (new_idx != idx):
            idx = new_idx
    
    print ("Closest to zero: ", idx)

particles = read()    
#closest_to_zero(particles)
remove_collision(particles)