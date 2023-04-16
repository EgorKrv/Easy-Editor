#создай тут фоторедактор Easy Editor!
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QVBoxLayout,
                             QListWidget, QPushButton,
                             QLabel, QFileDialog)
from PyQt5.QtGui import QPixmap
from PIL import Image
import os
from PyQt5.QtCore import Qt
from PIL import ImageFilter
from PIL import ImageEnhance
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.image = None
        self.filename = None
        self.save_dir = 'Modified/'

    def LoadImage(self,filename):
        self.filename = filename
        image_path = os.path.join(workdir,self.filename)
        self.image = Image.open(image_path)

    def ShowImage(self,path):
        image_label.hide()
        PixmapImage = QPixmap(path)
        w,h = image_label.width(),image_label.height()
        PixmapImage = PixmapImage.scaled(w,h,Qt.KeepAspectRatio)
        image_label.setPixmap(PixmapImage)
        image_label.show()

    def do_bw(self):
        self.image = self.image.convert('L')
        self.SaveImage()
        image_path = os.path.join(workdir,self.save_dir,self.filename)
        self.ShowImage(image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.SaveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.ShowImage(image_path)

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.SaveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.ShowImage(image_path)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.SaveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.ShowImage(image_path)

    def do_sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.SaveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.ShowImage(image_path)

    def do_bright(self):
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(1.1)
        self.SaveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.ShowImage(image_path)

    def do_dark(self):
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(0.9)
        self.SaveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.ShowImage(image_path)

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.SaveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.ShowImage(image_path)

    def SaveImage(self):
        path = os.path.join(workdir,self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(workdir,self.save_dir,self.filename)
        self.image.save(image_path)
    
WorkImage = ImageProcessor()

def ShowChoosenImage():
    filename = list_image.currentItem().text()
    WorkImage.LoadImage(filename)
    image_path = os.path.join(workdir,filename)
    WorkImage.ShowImage(image_path)

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Easy editor')

#лайауты
main_layout = QHBoxLayout()
row_tools = QHBoxLayout()
row_tools2 = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

btn_dir =  QPushButton('Папка')
list_image = QListWidget()
image_label = QLabel('Картинка')

btn_left = QPushButton('⭯')
btn_right = QPushButton('⭮')
btn_mirror = QPushButton('Отзеркалить')
btn_sharp = QPushButton('Резкость')
btn_bw = QPushButton('Ч/Б')
btn_bright = QPushButton('Увеличить яркость')
btn_dark = QPushButton('Уменьшить яркость')
btn_blur = QPushButton('Размыть изображение')

row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_mirror)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools2.addWidget(btn_bright)
row_tools2.addWidget(btn_dark)

col1.addWidget(btn_dir)
col1.addWidget(list_image)

col2.addWidget(image_label)
col2.addLayout(row_tools)

col2.addLayout(row_tools2)

main_layout.addLayout(col1)
main_layout.addLayout(col2)
main_win.setLayout(main_layout)

extensions = ['.jpg','.png','.jpeg']
def filter(files,extensions):
    results = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                results.append(filename)
    return results

workdir = ''
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
import os
def showFilenameList():
    extensions = ['.jpg','.png','.jpeg']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir),extensions)
    list_image.clear()
    list_image.addItems(filenames)
btn_dir.clicked.connect(showFilenameList)

main_layout.addLayout(col1,20)
main_layout.addLayout(col2,80)
main_win.resize(700,400)

btn_bw.clicked.connect(WorkImage.do_bw)
btn_mirror.clicked.connect(WorkImage.do_flip)
btn_right.clicked.connect(WorkImage.do_right)
btn_left.clicked.connect(WorkImage.do_left)
btn_sharp.clicked.connect(WorkImage.do_sharp)
btn_bright.clicked.connect(WorkImage.do_bright)
btn_dark.clicked.connect(WorkImage.do_dark)

list_image.currentRowChanged.connect(ShowChoosenImage)

main_win.show()
app.exec_()