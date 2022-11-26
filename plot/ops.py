import interp.ops as interp
import approx.ops as approx
import mat.ops as mat
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
