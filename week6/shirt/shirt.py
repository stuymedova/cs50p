import sys
import os.path
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    input, output = sys.argv[1], sys.argv[2]
    input_ext, output_ext = get_extension(input), get_extension(output)
    accepted_formats = ['.jpeg', '.jpg', '.png']
    if input_ext not in accepted_formats:
        sys.exit('Invalid input')
    if output_ext not in accepted_formats:
        sys.exit('Invalid output')
    if input_ext != output_ext:
        sys.exit('Input and output have different extensions')
    if not os.path.isfile(input):
        sys.exit('Input does not exist')
    if os.path.isfile(output):
        sys.exit(f'Cannot overwrite contents of a file. File {
            output} already exists'
        )
    dir = os.path.dirname(__file__)
    mask = os.path.join(dir, 'shirt.png')
    apply_mask(input, output, mask)


def get_extension(file):
    return os.path.splitext(file)[1].lower()


def apply_mask(input, output, mask):
    with Image.open(input) as input, Image.open(mask) as mask:
        input = ImageOps.fit(input, size=mask.size)
        input.paste(mask, mask=mask)
        input.save(output)


if __name__ == '__main__':
    main()
