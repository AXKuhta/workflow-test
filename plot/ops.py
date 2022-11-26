import interp.ops as interp
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
	fig.write_html("test.html")

