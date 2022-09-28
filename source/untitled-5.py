from PIL import Image

wr = Image.open("images/flow2.jpeg")
print(wr.height,wr.width)

wt = wr.resize((130*4,130*3),Image.LANCZOS)
wt.save("images/flow.jpeg")