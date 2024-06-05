import visualize
import pygame
import pandas as pd


def pil_to_pygame(image):
    """Convert a Pillow image to a Pygame surface.

    Args:
        image (PIL.Image): The Pillow image to convert.

    Returns:
        pygame.Surface: The converted Pygame surface.
    """
    mode = image.mode
    size = image.size
    data = image.tobytes()

    return pygame.image.fromstring(data, size, mode)


# Initialize pygame
pygame.init()

df = pd.read_csv(f'./data/current_state.csv', header=None)
game_image = visualize.df_to_image(df, visualize.colors, cell_size=visualize.LIFE_SIZE)

# Set up display
width, height = game_image.size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Image Display')

# Convert Pillow image to Pygame surface
game_surface = pil_to_pygame(game_image)

# Main loop to display the image
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    try:
        df = pd.read_csv(f'./data/current_state.csv', header=None)
        game_image = visualize.df_to_image(df, visualize.colors, cell_size=visualize.LIFE_SIZE)
        game_surface = pil_to_pygame(game_image)

        # Draw the image
        screen.blit(game_surface, (0, 0))
        pygame.display.flip()
    except Exception as e:
        print(e)

# Quit pygame
pygame.quit()
