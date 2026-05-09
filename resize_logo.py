from PIL import Image

img = Image.open("images/logo.png").convert("RGBA")

# Crop the blue symbol (left region, full height)
symbol = img.crop((0, 0, 245, 273))

# Crop the text region with a little padding
text = img.crop((285, 60, 905, 190))

# Scale the text so its height matches the symbol's content height (~270px)
target_h = 270
scale = target_h / text.height
text_new_w = int(text.width * scale)
text_resized = text.resize((text_new_w, target_h), Image.LANCZOS)

# Compose: symbol | gap | resized text, vertically centred
gap = 30
canvas_w = symbol.width + gap + text_new_w
canvas_h = 273
out = Image.new("RGBA", (canvas_w, canvas_h), (255, 255, 255, 0))

out.paste(symbol, (0, 0), symbol)
text_y = (canvas_h - target_h) // 2
out.paste(text_resized, (symbol.width + gap, text_y), text_resized)

out.save("images/logo_modified.png")
print(f"Saved images/logo_modified.png  ({canvas_w}x{canvas_h})")
