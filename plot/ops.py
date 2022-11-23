import interp.ops as interp
import mat.ops as mat
import plotly

def plot_multilerp():
	points = [
		[1, 2],
		[3, 4],
		[3.5, 3],
		[6, 7]
	]

	x = [x/10 for x in range(-10, 70)]
	y = [interp.multilerp2d(points, x) for x in x]

	actual_look = plotly.graph_objects.Scatter(x=mat.col(points, 0), y=mat.col(points, 1))
	lerp_look = plotly.graph_objects.Scatter(x=x, y=y, mode="markers")
	
	fig = plotly.graph_objects.Figure(data=[actual_look, lerp_look])
	fig.write_html("test.html")

