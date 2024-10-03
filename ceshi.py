import openslide 
from openslide.deepzoom import DeepZoomGenerator
import os
import numpy
from PIL import Image


slide=openslide.open_slide('./test1.svs')

dz_generator=DeepZoomGenerator(slide,tile_size=256,overlap=0)

for level in range(dz_generator.level_count):
    tiles=dz_generator.level_tiles[level]
    for col in range(tiles[0]):
        for row in range(tiles[1]):
            tile=dz_generator.get_tile(level,(col,row))
            #tile_image=Image.fromarray(tile)
            tile.save(f'output_tile_level_{level}_col_{col}_row_{row}.jpg','JPEG')

slide.close()











