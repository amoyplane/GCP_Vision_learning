
def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """

    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)

    texts = response.text_annotations
    f.write('Texts:')

    for text in texts:
        f.write('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in text.bounding_poly.vertices])

        f.write('bounds: {}'.format(','.join(vertices)))
