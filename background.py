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


def make_figure(background: Image, path) -> Image:
    figure = Image.open(path)
    figure = figure.resize(background.size)
    tr = Image.new('RGBA', (figure.size[0], figure.size[1]), (0,0,0,0))
    tr_pixels = tr.load()
    pixels_fig = figure.load()
    pixels_bgrnd = background.load()
    for i in range(figure.size[0]):
        for j in range(figure.size[1]):
            if pixels_fig[i, j] == (0, 0, 0):
                tr_pixels[i, j] = (pixels_bgrnd[i, j][0], pixels_bgrnd[i, j][1], pixels_bgrnd[i, j][2], 255)
    return tr





if __name__ == '__main__':
    bgrnd = make_background('template2.png')
    fig = make_figure(bgrnd, 'figure.png')
    fig.show()