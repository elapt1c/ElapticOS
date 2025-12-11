# --------ELAPTIC DESKTOP ENVIRONMENT--------
# REQUIRED MODULES:
pixel = __elaptic_registry__['pixel']
ansi = __elaptic_registry__['ansi']
asyncio = __elaptic_registry__['asyncio']
time = __elaptic_registry__['time']

async def desktop_main():
    screen = pixel.Screen(32, 16)
    background = pixel.Bitmap(32, 32, ([0x000000]) * 32 * 32)  # black background fill
    background.set_position(0, 0)
    screen.add_sprite(background)

    # Create a 1x1 white pixel sprite
    pixel_sprite = pixel.Bitmap(1, 1, [0xffffff])
    x, y = 3, 5
    dx, dy = 2, 1
    pixel_sprite.set_position(x, y)
    screen.add_sprite(pixel_sprite)
    while True:
        await asyncio.sleep(0.25)
        print(f"\n\n\n\n{ansi.ansi['clear']}{screen.render()}")

        # Move pixel
        x += dx
        y += dy

        # Bounce logic
        if x < 0:
            x = 0
            dx = -dx
        if y < 0:
            y = 0
            dy = -dy
        if x >= screen.width_pixels:
            x = screen.width_pixels - 1
            dx = -dx
        if y >= screen.height_pixels:
            y = screen.height_pixels - 1
            dy = -dy

        pixel_sprite.set_position(x, y)