from polygons import *

poly = Polygon(4, 5)
print(poly)
print(f"Edge           : {poly.edges}")
print(f"Vertices       : {poly.vertices}")
print(f"Interior angle : {poly.int_angle}")
print(f"Edge length    : {poly.edge_length:.3f}")
print(f"Apothem        : {poly.apothem:.3f}")
print(f"Area           : {poly.area:.3f}")
print(f"Perimeter      : {poly.perimeter:.3f}")

poly2 = Polygon(4, 5)
poly3 = Polygon(5, 6)
print(f"poly == poly2 ==> {poly == poly2}")
print(f"poly == poly3 ==> {poly == poly3}")
print(f"poly > poly3 ==> {poly > poly3}")
print(f"poly3 > poly ==> {poly3 > poly}")

print("")
seq_poly=Polygons(10,1)

print(seq_poly[2])

print(seq_poly[4:6])

print(seq_poly.get_max())

for poly in seq_poly:
     print(f"Edge           : {poly.edges:3}", f"ratio A/2P     : {poly.area/poly.perimeter:.5f}")


for poly in seq_poly:
    print(f"Edge           : {poly.edges:3}", f"Apothem      : {poly.apothem:.7f}")

