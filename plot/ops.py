import interp.ops as interp
import approx.ops as approx
import mat.ops as mat
from math import cos
import plotly

def plot_interp():
	points = [
		[1, 2],
		[3, 4],
		[3.5, 3],
		[6, 7]
	]

	x = [x/10 for x in range(-10, 70)]

	linear_model = interp.linear(points)
	
	y_linear 	= [linear_model(x) for x in x]
	y_lagrange 	= [interp.lagrange(points, x) for x in x]

	reference 	= plotly.graph_objects.Scatter(x=mat.col(points, 0), y=mat.col(points, 1))
	linear 		= plotly.graph_objects.Scatter(x=x, y=y_linear, mode="markers")
	lagrange 	= plotly.graph_objects.Scatter(x=x, y=y_lagrange, mode="markers")
	
	fig = plotly.graph_objects.Figure(data=[reference, linear, lagrange])
	fig.write_html("interp.html")

def plot_approx():
	points = [
		[1, 2],
		[3, 4],
		[3.5, 3],
		[6, 7]
	]

	x = [x/10 for x in range(-10, 70)]

	linear_model = approx.model(points, approx.linear)
	polyn2_model = approx.model(points, approx.polynomial_2)
	polyn3_model = approx.model(points, approx.polynomial_3)
	cos3_model   = approx.model(points, approx.cos3)
	
	y_linear 	= [linear_model(x) for x in x]
	y_polyn2 	= [polyn2_model(x) for x in x]
	y_polyn3 	= [polyn3_model(x) for x in x]
	y_cos3 		= [cos3_model(x) for x in x]

	reference 	= plotly.graph_objects.Scatter(x=mat.col(points, 0), y=mat.col(points, 1), name="Линейная интерполяция")
	linear 		= plotly.graph_objects.Scatter(x=x, y=y_linear, mode="markers", name="Линейная аппроксимация")
	polyn2 		= plotly.graph_objects.Scatter(x=x, y=y_polyn2, mode="markers", name="Полином 2й степени")
	polyn3 		= plotly.graph_objects.Scatter(x=x, y=y_polyn3, mode="markers", name="Полином 3й степени")
	cos3 		= plotly.graph_objects.Scatter(x=x, y=y_cos3, mode="markers", name="a*cos(3x) + b*cos(2x) + c*cos(x) + d")
	
	fig = plotly.graph_objects.Figure(data=[reference, linear, polyn2, polyn3, cos3])
	fig.write_html("approx.html")

def plot_image_approx():
	data = []
	vsz = 32

	reference = mat.identity(vsz)

	for i in range(vsz):
		for j in range(vsz):
			data.append( [i/vsz, j/vsz, reference[i][j]] )


	jpeg_cos_xy_src = "lambda x, y: ["

	for mx in range(16):
		for my in range(16):
			if mx == 0 and my == 0:
				expr = "1"
			elif my == 0:
				expr = f"cos(x*{3.14*mx})"
			elif mx == 0:
				expr = f"cos(y*{3.14*my})"
			else:
				expr = f"cos(x*{3.14*mx})*cos(y*{3.14*my})"

			jpeg_cos_xy_src += expr + ", "

	jpeg_cos_xy_src += "]"
	jpeg_cos_xy = eval(jpeg_cos_xy_src)

	model = approx.model(data, jpeg_cos_xy)
	model_out = []

	for i in range(vsz):
		row = []

		for j in range(vsz):
			row.append( model(i/vsz, j/vsz) )

		model_out.append(row)

	heatmap_1 = plotly.graph_objects.Heatmap(z=reference)
	heatmap_2 = plotly.graph_objects.Heatmap(z=model_out)

	fig = plotly.graph_objects.Figure(data=[heatmap_1])
	fig.write_html("pix1.html")

	fig = plotly.graph_objects.Figure(data=[heatmap_2])
	fig.write_html("pix2.html")
