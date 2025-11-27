from waves import generate, modulation, waveform_to_sound
import matplotlib.pyplot as plt
import pygame

# Initialize pygame mixer with default stereo settings
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2)
screen = pygame.display.set_mode((200, 100))

# ---------------------------------------------------
# PUT YOUR WAVEFORM GENERATING CODE HERE
# ---------------------------------------------------

notes = {
    "LA": 440,   # key: value
    "FA": 698,
    }

notes_inv = {value: key for key, value in notes.items()}

waveform_LA = generate(amplitude=0.5, frequency=440, duration=0.5)
waveform_FA = generate(amplitude=0.5, frequency=698, duration=0.5)

gamma = 5000

waveform_LA_modulated = [waveform_LA[i] * modulation(i, gamma) for i in range(len(waveform_LA))]
waveform_FA_modulated = [waveform_FA[i] * modulation(i, gamma) for i in range(len(waveform_LA))]

sound_LA = waveform_to_sound(waveform_LA_modulated)
sound_FA = waveform_to_sound(waveform_FA_modulated)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            sound_LA.play()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            sound_FA.play()
