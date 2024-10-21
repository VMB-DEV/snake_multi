# from typing import List
#
# import pygame
#
# # Initialize Pygame (required for key.name to work)
# pygame.init()
#
# # Function to get key name
# def get_key_name(key_constant: pygame.key):
#     return pygame.key.name(key_constant)
#
# # Examples
# keys_to_test: List[int] = [
#     105,
#     pygame.K_i,
#     pygame.K_SPACE,
#     pygame.K_RETURN,
#     pygame.K_UP,
#     pygame.K_LSHIFT,
#     pygame.K_F1
# ]
#
# # Print key names
# for key in keys_to_test:
#     print(f"Key constant: {key}, Key name: {get_key_name(key)}")
#
# # Clean up
# pygame.quit()
import pygame

print(f"{pygame.K_l}")