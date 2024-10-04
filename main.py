import openslide 
from openslide.deepzoom import DeepZoomGenerator
import os
from PIL import Image
from tqdm import tqdm
import sys
import argparse
from process_files import process_file




def main():
    parser=argparse.ArgumentParser(description="Process some files.")
    parser.add_argument('-i', '--input',required=True,help="Input file")
    parser.add_argument('-o', '--output',help="Output file path")
    args=parser.parse_args()
    

    process_file(args.input,args.output)

if __name__=="__main__":
    main()















