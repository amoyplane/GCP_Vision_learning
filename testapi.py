import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """

    print("marker")

    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    print("marker")

    response = client.text_detection(image=image)

    print("marker")

    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))


detect_text_uri("https://storage.googleapis.com/store_plane1/t.png")
