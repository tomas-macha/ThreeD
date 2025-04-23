
def rgb(r: int, g: int, b: int) -> str:
	return f'#{r:02x}{g:02x}{b:02x}'


def is_point_in_triangle(point: (int, int), triangle: [(int, int), (int, int), (int, int)]) -> bool:
	d1 = barycentric(point, triangle[0], triangle[1])
	d2 = barycentric(point, triangle[1], triangle[2])
	d3 = barycentric(point, triangle[2], triangle[0])
	
	has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
	has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
	
	return not (has_neg and has_pos)

def barycentric(a: (int, int), b: (int, int), c: (int, int)) -> int:
	return (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])
