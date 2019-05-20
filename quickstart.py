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


def sizefilter(vertices):
    minx = 999999999
    miny = 999999999
    maxx = -1
    maxy = -1
    for vertex in vertices:
        if vertex.x < minx:
            minx = vertex.x
        if vertex.x > maxx:
            maxx = vertex.x
        if vertex.y < miny:
            miny = vertex.y
        if vertex.y > maxy:
            maxy = vertex.y
    if ((maxx - minx < 15) or (maxy - miny < 15)):
        return true
    return false


def run_quickstart():

    # Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]

    # The name of the image file to annotate
    #file_name = os.path.join(os.path.dirname(__file__),'t3.jpg')
    file_name = os.path.join('/root/pic/', 't3.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # Performs label detection on the image file
    response = client.document_text_detection(image=image)

    blocki = 0
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            if (block.block_type != 1):
                continue
            # print('{}\n'.format(block.confidence))
            # print('{}\n'.format(block.block_type))

            # f.write('\nBlock confidence: {}\n'.format(block.confidence))

            blocki = blocki + 1
            f.write('Block # {} :\n'.format(blocki))
            vertices = (['({},{})'.format(vertex.x, vertex.y) for vertex in block.bounding_box.vertices])

            f.write('bounds: {} \n'.format(','.join(vertices)))

            for paragraph in block.paragraphs:
                # f.write('Paragraph confidence: {}'.format(
                #    paragraph.confidence))

                for word in paragraph.words:
                    if sizefilter(word.bounding_box.vertices):
                        continue

                    vertices = (['({},{}),'.format(vertex.x, vertex.y) for vertex in word.bounding_box.vertices])
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    f.write('Word text: {} '.format(word_text))
                    f.write('bounds: {} \n'.format(','.join(vertices)))

                    '''
                    for symbol in word.symbols:
                        f.write('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))
                    '''


if __name__ == '__main__':

    f = open('ans.txt', 'w')

    os.system("export GOOGLE_APPLICATION_CREDENTIALS=\"/root/mykey.json\"")
    run_quickstart()

    f.close()
