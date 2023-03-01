from PIL import Image
import face_recognition
import os

PRE_FILTER_DIR_PATH = "pre_filter/"
POST_FILTER_DIR_PATH = "post_filter/"

# Create post_filter folder if it doesn't already exist
if not (os.path.exists(POST_FILTER_DIR_PATH)):
    os.mkdir(POST_FILTER_DIR_PATH)

# Save each image in pre_filter folder to post_filter folder if a face is detected
num_images_saved = 0
for filename in os.listdir(PRE_FILTER_DIR_PATH):

    image = face_recognition.load_image_file(PRE_FILTER_DIR_PATH + filename)
    face_locations = face_recognition.face_locations(image)

    if len(face_locations) > 0:
        print("Face detected, saving image " + filename)
        image = Image.fromarray(image)
        image.save(POST_FILTER_DIR_PATH + filename)
        num_images_saved += 1

print("Saved " + str(num_images_saved) + " images in total")
