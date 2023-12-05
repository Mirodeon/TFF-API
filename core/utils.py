import math
import random


def degreeToRad(degree):

    return degree*(math.pi/180)


def distanceBetweenGPSPoint(lat1, lat2, lon1, lon2):

    # in meter
    R = 6371.0e3
    radLat1 = degreeToRad(lat1)
    radLat2 = degreeToRad(lat2)
    deltaRadLon = degreeToRad(lon2-lon1)

    return math.acos(
        math.sin(radLat1) * math.sin(radLat2) 
        + math.cos(radLat1) * math.cos(radLat2) * math.cos(deltaRadLon)
    ) * R

def generatePointWithinRadius(lat0, lon0, radius):
    
    w = (radius/111300) * math.sqrt(random.random())
    t = 2 * math.pi * random.random()

    x = w * math.cos(t)
    y = w * math.sin(t)

    xp = x/math.cos(lat0)

    return {
        "latitude": y+lat0,
        "longitude": xp+lon0
    }
