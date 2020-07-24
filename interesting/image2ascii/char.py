from PIL import Image, ImageDraw, ImageFont
import argparse


# 命令行参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output')

# 获取参数
#args = parser.parse_args()

IMG = r"xx.png"#args.file
OUTPUT = "output.png"#args.output
FONT_SIZE = 40
SCALE_FACTOR = 0.1


ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def rgb_to_gray(r, g, b):
    '将rgb值转化为灰度值'
    return int(0.2126 * r + 0.7152 * g + 0.0722 * b)


def get_char(r, g, b, alpha=256):
    '将256个灰度映射到字符列表上'
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = rgb_to_gray(r, g, b)

    unit = 256.0 / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    '主函数'
    im = Image.open(IMG)
    WIDTH, HEIGHT = im.size
    WIDTH_A, HEIGHT_A = int(WIDTH * SCALE_FACTOR), int(HEIGHT * SCALE_FACTOR)
    im = im.resize((WIDTH_A, HEIGHT_A), Image.ANTIALIAS)

    # 创建图片对象
    img = Image.new('RGB', (int(WIDTH * FONT_SIZE * SCALE_FACTOR),
                            int(HEIGHT * FONT_SIZE * SCALE_FACTOR)),
                    (255, 255, 255))

    # 创建font对象
    #font = ImageFont.truetype('Arial.ttf', FONT_SIZE)

    # 创建Draw对象
    draw = ImageDraw.Draw(img)

    for i in range(HEIGHT_A):
        for j in range(WIDTH_A):
            c = get_char(*im.getpixel((j, i)))
            pixel = im.getpixel((j, i))
            draw.text((j * FONT_SIZE, i * FONT_SIZE),
                      c, fill=pixel)# , font=font

    if not OUTPUT:
        OUTPUT = IMG[0:IMG.find('.')] + "_char.png"
    img.save(OUTPUT)