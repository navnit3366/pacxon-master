import pygame
import tilemap
from abc import ABC
import random
import threading
import time
import control
import tilemap_objects


ID_LIST = [11, 12, 13, 14]


def get_position():
    x = random.randint(3, tilemap.WIDTH - 3)
    y = random.randint(5, tilemap.HEIGHT - 5)

    while tilemap.tile_map[y][x]:
        x = random.randint(3, tilemap.WIDTH - 3)
        y = random.randint(5, tilemap.HEIGHT - 5)
    return x, y


def draw_on_a_map(x, y):
    id = random.choice(ID_LIST)
    tilemap.tile_map[y][x] = id

def erase_from_a_map(x, y):
    tilemap.tile_map[y][x] = tilemap.tile_map[y][x+1]

def control_fruit():
    while not control.done:
        t = random.randint(2, 10)
        while t:
            time.sleep(1)
            if control.done:
                return
            t -= 1
        x, y = get_position()
        draw_on_a_map(x, y)
        time.sleep(random.randint(4, 6))
        erase_from_a_map(x, y)


def start_fruit_thread():
    thread_1 = threading.Thread(target=control_fruit, daemon = True)
    thread_1.start()
    thread_2 = threading.Thread(target=control_fruit, daemon = True)
    thread_2.start()
    thread_3 = threading.Thread(target=control_fruit, daemon = True)
    thread_3.start()


def fruit_action(id):
    thread = threading.Thread(target=control_action, args=(id,))
    thread.start()


def control_action(id):
    if id == 11:
        tilemap_objects.set_pacman_speed(12)
    if id == 12:
        tilemap_objects.set_pacman_speed(12)
    if id == 13:
        tilemap_objects.set_ghost_speed(0)
    if id == 13:
        tilemap_objects.set_ghost_speed(0)

    time.sleep(5)

    tilemap_objects.set_pacman_speed(6)
    tilemap_objects.set_ghost_speed(3)
