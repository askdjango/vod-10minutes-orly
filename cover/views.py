from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from PIL import Image, ImageFont, ImageDraw
from .forms import CoverForm
from .utils import COLOR_CODES


def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CoverForm()
    return render(request, 'cover/index.html', {
        'form': form,
    })


def image_generator(request):
    title = request.GET['title']
    top_text = request.GET['top_text']
    author = request.GET['author']
    animal_code = request.GET['animal_code']
    color_index = request.GET['color_code']
    guide_text = request.GET['guide_text']
    guide_text_placement = request.GET['guide_text_placement']

    animal_path = settings.ROOT('assets', 'animal', '{}.png'.format(animal_code))
    animal_im = Image.open(animal_path)
    animal_im = animal_im.resize((200, 200))

    color = COLOR_CODES[int(color_index)]

    canvas_im = Image.new('RGB', (500, 700), color)
    canvas_im.paste(animal_im, (0, 0))  # left/top 지정

    ttf_path = settings.ROOT('assets', 'fonts', 'NanumGothicCoding.ttf')
    d = ImageDraw.Draw(canvas_im)

    fnt = ImageFont.truetype(ttf_path, 40)
    d.text((10, 10), title, font=fnt, fill=(0, 255, 0, 128))

    fnt = ImageFont.truetype(ttf_path, 20)
    d.text((10, 60), top_text, font=fnt, fill=(0, 255, 0, 255))

    fnt = ImageFont.truetype(ttf_path, 10)
    d.text((10, 110), author, font=fnt, fill=(0, 255, 0, 255))

    response = HttpResponse(content_type='image/png')  # file-like
    canvas_im.save(response, format='PNG')
    return response

