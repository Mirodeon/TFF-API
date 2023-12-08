import math
import random
import requests
from TFF.settings import CLAN_CHOICES, GET_IMG_AI_GUIDANCE, GET_IMG_AI_KEY, GET_IMG_AI_MODEL, GET_IMG_AI_NEGATIVE_PROMPT, GET_IMG_AI_SIZE, GET_IMG_AI_STEP, GET_IMG_AI_URL, JOB_CHOICES
import cloudinary
import cloudinary.uploader

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

def getJobChoices():
    jobs = []
    for x in JOB_CHOICES.split(" "):
        jobs.append((x, x))
    return tuple(jobs)

def getClanChoices():
    clans = []
    for x in CLAN_CHOICES.split(" "):
        clan_name=x.split(",")[0]
        clans.append((clan_name, clan_name))
    return tuple(clans)

def getColorClan(name):
    listClans = CLAN_CHOICES.split(" ")
    return listClans[[y.split(",")[0] for y in listClans].index(name)].split(",")[1]

def getImgAI(prompt, seed):
    payload = {
        "model": GET_IMG_AI_MODEL,
        "prompt": prompt,
        "negative_prompt": GET_IMG_AI_NEGATIVE_PROMPT,
        "width": GET_IMG_AI_SIZE,
        "height": GET_IMG_AI_SIZE,
        "steps": GET_IMG_AI_STEP,
        "guidance": GET_IMG_AI_GUIDANCE,
        "output_format": "png"
    }

    if seed!=0:
        payload["seed"] = seed

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + GET_IMG_AI_KEY
    }
    response = requests.post(GET_IMG_AI_URL, json=payload, headers=headers)
    return response

def getCatImgAI(job, color, lvl, seed):
    prompt = "cat "+job+color
    for i in range(lvl-1):
        prompt = prompt+" stronger"
    response = getImgAI(prompt, seed)
    return response

def getAvatarImgAI(color, animal, landscape, hobby):
    prompt = color+" "+animal+" in "+landscape+" playing "+hobby
    response = getImgAI(prompt, 0)
    return response

def uploadImgToCloud(image_id, image64):
    cloudinary.uploader.upload(
        "data:image/png;base64," + image64,
        public_id=image_id,
        overwrite=True,
        invalidate=True
    )