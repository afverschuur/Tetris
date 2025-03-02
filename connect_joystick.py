import sys
import pygame
import time

pygame.init()

pygame.joystick.init() 

# Display: Fullscreen 
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
# Figure out rectangle of screen (needed in other classes, eg CenterTextScreen)
screen_rect = screen.get_rect()
# Update settings
screen_width = screen_rect.width
screen_height = screen_rect.height

# Settings
bg_color = (0, 0, 0)
font = "assets/fonts/SpaceMono-Regular.ttf"
font_color = (255,255,255)

joystick = None
    
def check_events():
    global joystick
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Key 'q' to exit  
            if event.key == pygame.K_q:
                sys.exit()

        if event.type == pygame.JOYDEVICEADDED:
            # Add joystick
            joystick = pygame.joystick.Joystick(event.device_index)

def draw_text_centered(text, size, pos_y):
    text_bitmap = pygame.font.Font(font, size).render(text, True, font_color)
    # Figure out rectangle
    rect = text_bitmap.get_rect()
    # Center in screen
    rect.center = screen_rect.center
    # Set position on y-axis of screen
    rect.top = pos_y
    screen.blit(text_bitmap, rect)


def update_screen() -> None:
    """ Redraw assets and flip the screen"""
    global joystick
    # Background
    screen.fill(bg_color)

    if joystick:
        draw_text_centered(f"{joystick.get_name()} CONNECTED!", 60, 220)
    else:
        draw_text_centered("CONNECT A JOYSTICK", 60, 220)
    

# Main loop
while True:

    if joystick:
        # Wait 1 sec
        time.sleep(3)
        sys.exit()

    # Check input
    check_events()

    # update screen
    update_screen()   
    
    # Make the last drawn screen visible
    pygame.display.flip()