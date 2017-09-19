import os
from shutil import copyfile

def main():

    templates = ['search.html']

    for template in templates:
        copyfile('./{}'.format(template), './output/{}'.format(template))

    print('{} templates added.'.format(len(templates)))


if __name__ == "__main__":
    main()
