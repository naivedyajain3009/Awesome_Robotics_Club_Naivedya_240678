import math

def inverse_kinematics(x, y, z):
    alpha = math.atan2(y, x) #alpha angle is the angle that is made when coxa rotates only about the z-axis in the x-y plane this angle is angle moved in that plane this is calculated using tan inverse of y divided by x.

    hordist = math.sqrt(x**2 + y**2) - 5 #calculating the distance of the point from the point of coxa and finding its projrction in the x-y plane
    dis = math.sqrt(hordist**2 + z**2) #distance of the point from the coxa point

    if dis > 25 or dis < 5:  # checking the conditions if the point will be reachable if we form a triangle or simple add or subtract the distances
        return None  

    cosg = (325 - dis**2) / (300) #Cosine law application taking femur,tibia and distance and finding angle between femur and tibia
    gamma = math.acos(cosg)

    cosb = (dis**2 -125) / (20 * dis) #Finding the angle beta
    beta_offset = math.acos(cosb)
    angle_to_target = math.atan2(z, hordist)
    beta = angle_to_target + beta_offset

    alpha_deg = math.degrees(alpha) # converting the angles into degrees
    beta_deg = math.degrees(beta)
    gamma_deg = 180-math.degrees(gamma)

    return alpha_deg, beta_deg, gamma_deg

def test_inverse_kinematics():
    abc=inverse_kinematics(x, y, z)
    print("The coordinates are",x,y,z)
    print(abc)
    if inverse_kinematics(x, y, z)==None:
        print("Point is not reachable")
    else:
        print("Point is reachable")

x = 10
y = 5
z = -5
test_inverse_kinematics()

x = 3
y = 2
z = 1
test_inverse_kinematics()

x = 20
y = 0
z = 0
test_inverse_kinematics()

x = 31
y = 0
z = 0
test_inverse_kinematics()

x = 10
y = 0
z = -20
test_inverse_kinematics()
