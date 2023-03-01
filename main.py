import face_recognition
import os

PRE_FILTER_DIR_PATH = "/pre_filter"
POST_FILTER_DIR_PATH = "/post_filter"

for filename in os.listdir(PRE_FILTER_DIR_PATH):
    image = face_recognition.load_image_file(PRE_FILTER_DIR_PATH + "/" + filename)
    
    face_locations = face_recognition.face_locations(image)
    if len(face_locations) > 0:
        image.save(POST_FILTER_DIR_PATH + "/" + filename)