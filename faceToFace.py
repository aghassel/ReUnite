import os
import io
import json
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw, ImageFont

credential = json.load(open('AzureCloudKeys.json'))
API_KEY = '5fa48a8796664c4a8130b16c1d0215f3'
ENDPOINT = 'https://mycognitiveservicesresourcefacecomp.cognitiveservices.azure.com/'
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

response_detected_faces = face_client.face.detect_with_stream(
    image=open('.\images\mj1.jpg', 'rb'),
    detection_model='detection_03',
    recognition_model='recognition_04',  
 )

face_ids = [face.face_id for face in response_detected_faces]

img_tim_duncan = open(r'.\images\mj2.jpg','rb')
response_face_tim_duncan = face_client.face.detect_with_stream(
    image = img_tim_duncan,
    detection_model='detection_03',
    recognition_model='recognition_04'
)

face_id_tim_duncan = response_face_tim_duncan[0].face_id

matched_face_ids=face_client.face.find_similar(
    face_id=face_id_tim_duncan,
    face_ids = face_ids
)


# face_ids = [face.face_id for face in response_detected_faces]

# img_source = open('.\images\mj1.jpg', 'rb')
# response_face_source = face_client.face.detect_with_stream(
#     image=img_source,
#     detection_model='detection_03',
#     recognition_model='recognition_04'    
# )
# face_id_source = response_face_source[0].face_id

# matched_faces = face_client.face.find_similar(
#     face_id=face_id_source,
#     face_ids=face_ids
# )

# img = Image.open(open('.\images\group1.jpg', 'rb'))
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype('C:\Windows\Fonts\OpenSans-Bold.ttf', 25)

# for matched_face in matched_faces:
#     for face in response_detected_faces:
#         if face.face_id == matched_face.face_id:
#             rect = face.face_rectangle
#             left = rect.left
#             top = rect.top
#             right = rect.width + left
#             bottom = rect.height + top
#             draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)
# ## img.show()

# face_verified = face_client.face.verify_face_to_face(
#     face_id1=matched_faces[0].face_id,
#     face_id2='371e00f4-b5a5-4030-8473-3388d7016423'
# )
# print(face_verified.is_identical) #never gonna give you up , never gonna let you down never gonna stand around and desert you pappi 