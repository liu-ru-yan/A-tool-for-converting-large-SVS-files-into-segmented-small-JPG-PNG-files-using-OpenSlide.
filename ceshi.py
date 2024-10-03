import openslide 
from openslide.deepzoom import DeepZoomGenerator
import os
from PIL import Image
from tqdm import tqdm







output_folder='/mnt/c/Users/Jhong/Desktop/result/result_floor_of_mouth_2/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

slide=openslide.open_slide('./test2.svs')

dz_generator=DeepZoomGenerator(slide,tile_size=256,overlap=0)


for level in tqdm(range(dz_generator.level_count),desc='Processing 1',colour='red'):
    
    tiles=dz_generator.level_tiles[level]
    for col in tqdm(range(tiles[0]),desc='Processing 2',colour='green'):
        
        for row in tqdm(range(tiles[1]),desc='Processing 3',colour='blue'):
            
            tile=dz_generator.get_tile(level,(col,row))
            output=os.path.join(output_folder,f'output_tile_level_{level}_col_{col}_row_{row}.jpg')
            tile.save(output,'JPEG')
            

slide.close()











