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
	y_lerp = [interp.multilerp2d(points, x) for x in x]
	y_lagrange = [interp.lagrange(points, x) for x in x]

	actual_look = plotly.graph_objects.Scatter(x=mat.col(points, 0), y=mat.col(points, 1))
	lerp_look = plotly.graph_objects.Scatter(x=x, y=y_lerp, mode="markers")
	lagrange_look = plotly.graph_objects.Scatter(x=x, y=y_lagrange, mode="markers")
	
	fig = plotly.graph_objects.Figure(data=[actual_look, lerp_look, lagrange_look])
	fig.write_html("test.html")

