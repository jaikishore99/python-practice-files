from PIL import Image

# (r " location or navigate to photo which is selected ")

open_image = Image.open(r"     #        ")
convert_to_bw = open_image.convert("L")
convert_to_bw.show()