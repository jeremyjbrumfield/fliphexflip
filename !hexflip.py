import pygame
import math

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# Create a surface for the hexagon
hexagon_surface = pygame.Surface((160, 160), pygame.SRCALPHA)

# Define hexagon points
points = []
for i in range(6):
    angle = i * math.pi / 3
    x = 80 + 80 * math.cos(angle)
    y = 80 + 80 * math.sin(angle)
    points.append((x, y))

# Colors
heads_color = (255, 0, 0)  # Red
tails_color = (0, 0, 255)  # Blue
current_color = heads_color  # Start color
animating = False
scale_direction = 1  # 1 for expanding, -1 for contracting
current_scale = 160

def draw_hexagon(color):
    hexagon_surface.fill((0, 0, 0, 0))  # Clear the surface
    pygame.draw.polygon(hexagon_surface, color, points)
    pygame.draw.polygon(hexagon_surface, (128, 128, 0), points, 5)  # Outline

draw_hexagon(current_color)  # Initial draw

run = True
while run:
    clock.tick(60)
    window.fill(0)  # Clear the window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not animating:  # Start animation on click
                animating = True
                scale_direction = -1  # Start contracting

    if animating:
        current_scale += scale_direction * 10  # Adjust scale

        if current_scale <= 0:
            current_scale = 0
            # Change color at narrowest point
            current_color = tails_color if current_color == heads_color else heads_color
            scale_direction = 1  # Start expanding
        
        if current_scale >= 160:
            current_scale = 160
            animating = False  # End of animation

    # Draw the hexagon with the current color
    draw_hexagon(current_color)
    scaled_hexagon = pygame.transform.scale(hexagon_surface, (current_scale, 160))
    window.blit(scaled_hexagon, scaled_hexagon.get_rect(center=hexagon_surface.get_rect(center=window.get_rect().center).center))
    pygame.display.flip()

pygame.quit()
exit()
