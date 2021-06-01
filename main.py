import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import tools

app = Flask(__name__)
images_dir = app.config['IMAGE_UPLOADS'] = './static/images/uploads'

images = []
undos = []


def img_path():
    return '{}/{}'.format(images_dir, images[-1])


@app.route('/load-img', methods=['GET', 'POST'])
def load_img():
    if request.method == 'POST':
        if request.files:
            picture = request.files['picture']
            picture.save(os.path.join(images_dir, picture.filename))
            images.clear()
            images.append(picture.filename)
            images.append(tools.read_image(f'{images_dir}/{picture.filename}'))
            return redirect('/')
    else:
        return


@app.route('/')
def home():
    if len(images) == 2:
        return render_template('home.html', picture=f'{images_dir}/{images[0]}')
    elif len(images) > 2:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{tools.img_enc(images[-1])}')
    else:
        return render_template('home.html')


@app.route('/init')
def initialize():
    if len(images) >= 2:
        images.append(images[1])
        return render_template('home.html', picture=f'{images_dir}/{images[0]}')
    else:
        pass


@app.route('/undo')
def undo():
    if len(images) >= 2:
        img = images.pop()
        undos.append(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{tools.img_enc(images[-1])}')
    else:
        return render_template('home.html', picture=f'{images_dir}/{images[0]}')


@app.route('/restore')
def restore():
    if len(undos) >= 1:
        img = undos.pop()
        images.append(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{tools.img_enc(images[-1])}')
    else:
        return render_template('home.html', picture=f'{images_dir}/{images[0]}')


@app.route('/save-img')
def save_img():
    if len(images) > 1:
        tools.save_image(images[-1])
        images.clear()
        return redirect('/')
    else:
        return "Vous n'avez encore applique une modification"


@app.route('/gray-scale')
def gray_scale():
    try:
        img = images[-1]
        img = tools.to_gray_scale(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


@app.route('/binary')
def binary_inv():
    try:
        img = images[-1]
        img = tools.to_binary_inv(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


@app.route('/truncate')
def truncate():
    try:
        img = images[-1]
        img = tools.to_truncate(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


@app.route('/zero')
def zero():
    try:
        img = images[-1]
        img = tools.to_zero(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


@app.route('/zero-inv')
def zero_inv():
    try:
        img = images[-1]
        img = tools.to_zero_inv(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


# MORPHOLOGY
# ***********

@app.route('/erosion')
def erosion():
    try:
        img = images[-1]
        img = tools.erosion(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


@app.route('/dilatation')
def dilatation():
    try:
        img = images[-1]
        img = tools.dilatation(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


@app.route('/open')
def to_open():
    try:
        img = images[-1]
        img = tools.open(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


@app.route('/close')
def to_close():
    try:
        img = images[-1]
        img = tools.close(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


@app.route('/gradient')
def gradient():
    try:
        img = images[-1]
        img = tools.gradient(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


@app.route('/gaussian')
def gaussian():
    try:
        img = images[-1]
        img = tools.gaussian_blur(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


@app.route('/median')
def median():
    try:
        img = images[-1]
        img = tools.median_blur(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


@app.route('/edges')
def edges():
    try:
        img = images[-1]
        img = tools.edge_detect(img)
        images.append(img)
        img_enc = tools.img_enc(img)
        return render_template('home.html', picture=f'data:image/jpeg;base64,{img_enc}')
    except:
        return render_template('home.html', picture=f'data:image/jpeg;base64,{images[-1]}')


if __name__ == '__main__':
    app.run(debug=True)
