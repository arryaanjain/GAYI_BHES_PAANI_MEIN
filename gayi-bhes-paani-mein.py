from PIL import Image, ImageSequence

def buffalo_underwater(buffalo_path, background_path, output_path, frames=30, descend_speed=5):
    # Load images
    buffalo = Image.open(buffalo_path).convert("RGBA")
    background = Image.open(background_path).convert("RGBA")
    
    # Resize buffalo to fit background if needed
    buffalo = buffalo.resize((int(background.width * 0.4), int(background.height * 0.4)))

    # Start position
    x = int((background.width - buffalo.width) / 2)
    y_start = int(background.height * 0.4)
    
    frame_list = []

    for i in range(frames):
        frame = background.copy()
        y = y_start + i * descend_speed
        
        # Optional: fade out as it goes deeper
        alpha = max(0, 255 - i * int(255 / frames))
        buffalo_with_alpha = buffalo.copy()
        buffalo_with_alpha.putalpha(alpha)

        frame.paste(buffalo_with_alpha, (x, y), buffalo_with_alpha)
        frame_list.append(frame)

    # Save as GIF
    frame_list[0].save(output_path, save_all=True, append_images=frame_list[1:], duration=100, loop=0)
    print(f"Animation saved as {output_path}")

# Example usage
buffalo_underwater(
    buffalo_path='buffalo.png',
    background_path='water_background.png',
    output_path='buffalo_descending.gif'
)
