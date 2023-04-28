import math

from PIL import Image


def make_background(path) -> Image:
    template = Image.open(path)
    width, height = template.size
    print(width, height)
    template = template.resize((200, int(height * 200 / width)))
    width, height = template.size
    WT = 10
    HT = 10
    background = Image.new('RGB', (width * WT, height * HT))
    for i in range(0, WT * width, width):
        for j in range(0, HT * height, height):
            background.paste(template, (i, j))
    return background


def make_strip(path) -> Image:
    template = Image.open(path)
    width, height = template.size
    print(width, height)
    template = template.resize((200, int(height * 200 / width)))
    width, height = template.size
    HT = 5
    background = Image.new('RGB', (width, height * HT))
    for j in range(0, HT * height, height):
        background.paste(template, (0, j))
    return background

def make_stigs(fig:str, strip):
    width, height = strip.size
    mask = Image.open(fig)
    width2, height2 = mask.size
    mask.resize((int(width2*height/height2), height))
    width2, height2 = mask.size
    res = Image.new('RGB', (math.ceil(width2/width) * width, height))
    res_pixls = res.load()
    mask_pxls = mask.load()
    new_strip = strip
    nstrp_pixels = new_strip.load()
    for k in range(0, math.ceil(width2/width)):
        for i in range(0, height):
            for j in range(width * k, width * (k + 1)):
                if j < width2 and i < height2 and mask_pxls[j,i] == (0,0,0):
                    nstrp_pixels[j-8 - k * width,i] = nstrp_pixels[j - k * width,i]
                    # res_pixls[j,i]=(255,0,0)
        res.paste(new_strip,(k * width, 0))
    return res




# def make_figure(background: Image, path) -> Image:
#     figure = Image.open(path)
#     figure = figure.resize(background.size)
#     tr = Image.new('RGBA', (figure.size[0], figure.size[1]), (0, 0, 0, 0))
#     tr_pixels = tr.load()
#     pixels_fig = figure.load()
#     pixels_bgrnd = background.load()
#     for i in range(figure.size[0]):
#         for j in range(figure.size[1]):
#             if pixels_fig[i, j] == (0, 0, 0):
#                 tr_pixels[i, j] = (pixels_bgrnd[i, j][0], pixels_bgrnd[i, j][1], pixels_bgrnd[i, j][2], 255)
#     return tr


# def homotetia(pic: Image):


if __name__ == '__main__':
    bgrnd = make_strip('template2.png')
    # fig = make_figure(bgrnd, 'figure.png')
    # fig.show()
    # fig2 = fig.resize((int(fig.size[0] + 10), int(fig.size[1] + 10)))
    # bgrnd.show()
    # bgrnd.paste(fig2)
    res = make_stigs('figure.png', bgrnd)
    res.show('NIGGERS')
    bgrnd.show()

# print(__name__)