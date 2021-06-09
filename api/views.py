from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from . import serializers
from django.http import JsonResponse
import numpy as np
import cv2
import urllib.request
from PIL import Image
from keras_preprocessing import image
from tensorflow import keras


def compare(imgURL1, imgURL2):
    localfile1, headers = urllib.request.urlretrieve(imgURL1)
    localfile2, headers = urllib.request.urlretrieve(imgURL2)

    percentage_list = []

    img1 = cv2.imread(localfile1, 4)
    img2 = cv2.imread(localfile2, 4)

    sift = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
            a = len(good)
            percent = (a*100)/len(kp2)
            #print("{} % similarity".format(percent))
            percentage_list.append(percent)
            # if percent >= 75.00:
            #print('Match Found')
            # if percent < 75.00:
            #print('Match not Found')

    sim_value = max(percentage_list)
    if sim_value >= 1.00:
        return True
    else:
        return False


def getCompare(request):
    url1 = "https://firebasestorage.googleapis.com/v0/b/japor-45077.appspot.com/o/report-images%2Fc786a60a-0572-4ed5-9324-e9cdefed8413?alt=media&token=12ae9993-90f3-49f9-8ff1-bdd4c5376396"
    result = compare(
        url1, "https://firebasestorage.googleapis.com/v0/b/japor-45077.appspot.com/o/report-images%2Fc786a60a-0572-4ed5-9324-e9cdefed8413?alt=media&token=12ae9993-90f3-49f9-8ff1-bdd4c5376396")
    if result == True:
        data = {
            "response": "True"
        }
        return JsonResponse(data)
    else:
        data = {
            "response": "False"
        }
        return JsonResponse(data)


def getRecommendation(request):
    model = keras.models.load_model('./models/model.h5')

    url1 = "https://firebasestorage.googleapis.com/v0/b/japor-45077.appspot.com/o/report-images%2Fc786a60a-0572-4ed5-9324-e9cdefed8413?alt=media&token=12ae9993-90f3-49f9-8ff1-bdd4c5376396"
    localfile3, headers = urllib.request.urlretrieve(url1)
    img = image.load_img(localfile3, target_size=(150, 150))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)

    data = {
        "jalan": str(classes[0][0]),
        "kebakaran": str(classes[0][1]),
        "pohon": str(classes[0][2]),
    }
    return JsonResponse(data)


class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class LaporViewset(viewsets.ModelViewSet):
    queryset = models.Lapor.objects.all()
    serializer_class = serializers.LaporSerializer
