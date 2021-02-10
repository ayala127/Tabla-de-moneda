#Creador del codigo:ayala127#
mex = (int(input("ingresa la cantidad en pesos mexicanos: ")))
conv = [[mex, 'DA', str(round(mex / 21.51, 2))],
        [mex, 'DC', str(round(mex / 16.15, 2))],
        [mex, 'yenes', str(round(mex / .21, 2))],
        [mex, 'rupias', str(round(mex / .29, 2))],
        [mex, "eur", str(round(mex / 25.22, 2))],
        [mex, "PE", str(round(mex / 0.15, 2))],
        [mex, "MarcoAlem", str(round(mex / 12.77, 2))]]
Tabla = """\
+----------------------------------+
| PM    M                 Ca       |
|----------------------------------|
{}
+----------------------------------+\
"""
Tabla = (Tabla.format('\n'.join(
    "| {:<8} {:<10} {:>8} |".format(*fila) for fila in conv)))
print(Tabla)

