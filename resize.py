from PIL import Image
from os import listdir

mypath = "static/img/merch/test"

onlyfiles = [f for f in listdir(mypath)]

for i in onlyfiles:
    foo = Image.open(f'{mypath}/{i}')
    print(foo.size)
    foo = foo.resize((350, 350))
    foo.save(f'static/img/merch/ready/{i}', optimize=True, quality=95)
