import pandas as pd
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os

LIFE_SIZE = 30
output_path = './data/animated.gif'

# List all CSV files in the directory
csv_files = [f for f in os.listdir('./data') if f.endswith('.csv')]

# Define colors for numbers 0-9
colors = list(mcolors.TABLEAU_COLORS.keys())


# Define function to convert dataframe to image
def df_to_image(df, colors, cell_size):
    rows, cols = df.shape
    img = Image.new('RGB', (cols * cell_size, rows * cell_size), color='white')
    draw = ImageDraw.Draw(img)

    for r in range(rows):
        for c in range(cols):
            num = df.iloc[r, c]
            color = colors[num % len(colors)]
            draw.rectangle([(c * cell_size, r * cell_size),
                            (c * cell_size + cell_size - 1, r * cell_size + cell_size - 1)],
                            fill=mcolors.TABLEAU_COLORS[color])

    return img


# Read all CSV files and create images
images = []
for file in sorted(csv_files):
    try:
        df = pd.read_csv(f'./data/{file}', header=None)
        images.append(df_to_image(df, colors, cell_size=LIFE_SIZE))
    except:
        print("error")

# Save as animated GIF
images[0].save(output_path, save_all=True, append_images=images[1:], duration=500, loop=0)
