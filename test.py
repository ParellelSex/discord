from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import web

urls = (
    '/(.*)', 'index.html'
)
app = web.application(urls, globals())

img = Image.new("RGBA", (450, 135), (255, 255, 255, 255))

if __name__ == "__main__":
    app.run()
