import base64


IMAGE_FALLBACK_NAME = 'static/image/Pokeball.png'
IMAGE_FALLBACK_B64 = base64.b64encode(open(IMAGE_FALLBACK_NAME, 'rb').read())
IMAGE_FALLBACK = f"data:image/png;base64,{IMAGE_FALLBACK_B64.decode()}"
