import os
from shutil import copyfile
import glob


def main():

    templates = [
        'googleb61e79b00fce6520.html'
    ]

    for template in templates:
        copyfile('./{}'.format(template), './output/{}'.format(template))

    print('Done: Processed {} additional templates.'.format(len(templates)))

    # add ipynb from other projects
    extension = 'ipynb'
    source_dir = './projects'
    destination_dir = './content/projects'
    num_files_copied = 0

    ipynb_paths = glob.iglob(os.path.join(source_dir, '**', '*.%s' % extension), recursive=True)
    for ipynb_p in ipynb_paths:
        destination_p = ipynb_p.replace(source_dir, destination_dir)
        # create new project folder for the ipynb file in content folder if not exist
        sub_destination_dir = '/'.join(destination_p.split('/')[:-1])
        if not os.path.exists(sub_destination_dir):
            os.makedirs(sub_destination_dir)

        copyfile(ipynb_p, destination_p)
        num_files_copied += 1

    print('Done: Processed {} additional ipynb files from other projects.'.format(num_files_copied))


if __name__ == "__main__":
    main()
