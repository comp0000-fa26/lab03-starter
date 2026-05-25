from geom.shapes import area_of_circle

def print_circle_report(radius: float):
    area = area_of_circle(radius)
    print(f"Area: {area:.2f}")