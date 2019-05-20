#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# [START vision_quickstart]
import io
import os
#import socket
#import requests
#import socks

# Imports the Google Cloud client library
# [START vision_python_migration_import]
from google.cloud import vision
from google.cloud.vision import types
# [END vision_python_migration_import]


def run_quickstart():

    # Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        't3.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # Performs label detection on the image file
    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('{}\n'.format(block.confidence))
            print('{}\n'.format(block.blockType))

            # f.write('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                f.write('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    f.write('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        f.write('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))


'''
    texts = response.text_annotations
    f.write('Texts:')

    for text in texts:
        f.write('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in text.bounding_poly.vertices])

        f.write('bounds: {}'.format(','.join(vertices)))
    # [END vision_quickstart]
'''


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


if __name__ == '__main__':

    f = open('ans.txt', 'w')

    '''
    socks5_proxy_host = '127.0.0.1'
    socks5_proxy_port = 1080
    socks.set_default_proxy(socks.SOCKS5, socks5_proxy_host, socks5_proxy_port)
    socket.socket = socks.socksocket
    '''
    os.system("export GOOGLE_APPLICATION_CREDENTIALS=\"/root/mykey.json\"")
    run_quickstart()

    #f.write("\n=======using uri========\n")

    # detect_text_uri("https://storage.googleapis.com/store_plane1/t3.png")

    f.close()
