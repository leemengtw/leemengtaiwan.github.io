import os
from shutil import copyfile

def main():

    templates = [
        'googleb61e79b00fce6520.html'
    ]

    for template in templates:
        copyfile('./{}'.format(template), './output/{}'.format(template))

    print('Done: Processed {} templates.'.format(len(templates)))

if __name__ == "__main__":
    main()
