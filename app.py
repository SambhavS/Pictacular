import os
from flask import Flask, request, redirect, url_for, render_template, flash, jsonify
from werkzeug.utils import secure_filename
from math import sqrt
from PIL import Image
from mapdic import get_mapdict
import base64
import io

###
#Pictacular
###
#Note: Numbers may need to be modified depending on the number of images and dimensions of images used.
####

class PicCore:
	def __init__(self):
		self.final_width = 2500
		self.pic_ind = 0
		self.zone_map = get_mapdict()
core = PicCore()

def run_loop(img):
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
			return tuple([16*(int(val)//16) for val in col])
	final_width = core.final_width
	orig = img.resize((final_width,final_width))
	new_image = Image.new('RGB',(final_width,final_width))
	square_ratio = 60
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
	core.pic_ind+=1
	return new_image

###
#Flask
###
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
user_folder = ""

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload',methods=['GET','POST'])
def upload():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			return "What is this supposed to check for?"
		file = request.files['file']
		img = Image.open(io.BytesIO(file.read())).convert()

		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			return "Hi! You didn't enter a file! Go back and enter one."
		if file and allowed_file(file.filename):
			output =  run_loop(img)
			in_mem_file = io.BytesIO()
			output.save(in_mem_file, format = "PNG")
			# reset file pointer to start
			in_mem_file.seek(0)
			img_bytes = in_mem_file.read()
			base64_encoded_result_bytes = base64.b64encode(img_bytes)
			result = base64_encoded_result_bytes.decode('ascii')
			return result

@app.route('/', methods=['GET', 'POST'])
def normal():
	return render_template('ind.html')

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)