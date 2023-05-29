from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import web
app = web.application(('(.*)', 'test'), globals())
img = Image.new("RGBA", (450, 135), (255, 255, 255, 255))
