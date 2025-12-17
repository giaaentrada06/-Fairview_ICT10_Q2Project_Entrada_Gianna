def compute():
    a = float(Element("g1").value)
    b = float(Element("g2").value)
    c = float(Element("g3").value)
    d = float(Element("g4").value)
    e = float(Element("g5").value)

    Element("output").write((a + b + c + d + e) / 5)
