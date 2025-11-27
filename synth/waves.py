from math import pi, sin
import math
import pygame
import numpy as np

class Note:
    pass

def linspace(start: float, end: float, num_steps: int) -> list[float]:
    # Generates a uniform range through linear steps.
    # FIXME: doesn't work for num_steps == 1
    #
    # Args:
    #   - start: The start of the range.
    #   - end: The end of the range.
    #   - num_steps: The number of steps the range gets divided into.
    #
    # Output:
    #   A uniform range.

    step_length = (end - start) / num_steps
    out = [0] * (num_steps + 1)
    for i in range(num_steps + 1):
        out[i] = start + step_length * i
    return out

def generate(amplitude: float, frequency: float, duration: float) -> list[float]:
    return [amplitude * sin(2 * pi * frequency * t) for t in linspace(0., duration, int(duration * 44100))]

def modulation(i: int, gamma: float) -> float:
    return math.exp(-i / gamma)

def waveform_to_sound(waveform: list[float]):
    # Convert to 16-bit signed integers and reshape for stereo (duplicate mono to both channels)
    samples = np.array(waveform)
    sound_array = (samples * 32767).astype(np.int16)
    sound_array = np.column_stack((sound_array, sound_array))  # Force stereo
    sound = pygame.sndarray.make_sound(sound_array)
    return sound