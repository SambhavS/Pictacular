import os
from flask import Flask, request, redirect, url_for, render_template, flash, jsonify
from werkzeug.utils import secure_filename
from math import sqrt
from PIL import Image
from mapdic import get_mapdict
import random
import shutil

###
#Pictacular
###
#Note: Numbers may need to be modified depending on the number of images and dimensions of images used.
####

class PicCore:
	def __init__(self):
		self.final_width = 6000
		self.pic_ind = 0
		self.zone_map = get_mapdict()
core = PicCore()

def run_loop(orig_name):
	def rounded_col(pic):
		if max(pic.width,pic.height)/float(min(pic.width,pic.height)) < 1.5:
			square_width = 150
			quick = 15
			ratio = float(square_width)/min(pic.height,pic.width)
			pic = pic.resize((int(ratio*pic.width)+1,int(ratio*pic.height)+1))
			pic = pic.crop((0,0,square_width,square_width))
			col=[0,0,0]
			pixels = (square_width ** 2)/(quick ** 2)
			for i in range(0,square_width, quick):
				for j in range(0,square_width, quick):
					pix = pic.getpixel((i,j))
					if(type(pix)==tuple):
						col[0], col[1], col[2] = col[0] + pix[0]/pixels, col[1] + pix[1]/pixels, col[2] + pix[2]/pixels
			return tuple([32*(int(val)//32) for val in col])
	final_width = core.final_width
	orig = Image.open(orig_name).resize((final_width,final_width))
	new_image = Image.new('RGB',(final_width,final_width))
	square_ratio = 50
	square_width = int(final_width/square_ratio)
	x_offset = 0
	all_images = {}
	for path in core.zone_map.values():
		all_images[path] = Image.open(path)
	for _ in range(square_ratio):
		y_offset = 0
		for _ in range(square_ratio):
			chunk = orig.crop((x_offset,y_offset,x_offset+square_width,y_offset+square_width))
			zone = rounded_col(chunk)
			path = core.zone_map[zone]
			pic = all_images[path]
			replacement = pic.resize((square_width,square_width))
			new_image.paste(replacement, (x_offset,y_offset))
			y_offset+=int(square_width)
		x_offset+=int(square_width)
	new_image.save(user_folder+"/new_"+str(core.pic_ind)+".jpg")
	core.pic_ind+=1

###
#Flask
###
UPLOAD_FOLDER = 'path/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
user_folder = ""

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def get_pics():
		return [user_folder+"/new_"+str(i)+".jpg" for i in range(core.pic_ind)]
@app.route('/folder', methods = ['GET','POST'])
def close_folder():
	global user_folder
	stringy = request.data.decode("utf-8")
	print(stringy)
	if stringy == "open":
		core.pic_ind = 0
		user_num = random.randint(1,100000000)
		user_folder = "static/user"+str(user_num)
		os.makedirs(user_folder)
		print(3)
	elif stringy == "close":
		print(2)
		shutil.rmtree(user_folder)
		user_folder=""
	return "hello"

@app.route('/links',methods=['GET','POST'])
def get_links():
	print(1)
	if request.method == 'GET':
		return jsonify(get_pics())

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			return "Hello1"
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			return "Hello2"
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(path)
			run_loop(path)
	pics = get_pics()
	return render_template('ind.html', pictures=pics)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)