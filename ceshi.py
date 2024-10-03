import openslide 
from openslide.deepzoom import DeepZoomGenerator
import os
import numpy
from PIL import Image


output_folder='./result/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

slide=openslide.open_slide('./test1.svs')

dz_generator=DeepZoomGenerator(slide,tile_size=256,overlap=0)

for level in range(dz_generator.level_count):
    tiles=dz_generator.level_tiles[level]
    for col in range(tiles[0]):
        for row in range(tiles[1]):
            tile=dz_generator.get_tile(level,(col,row))
            output=os.path.join(output_folder,f'output_tile_level_{level}_col_{col}_row_{row}.jpg')
            tile.save(output,'JPEG')

slide.close()











