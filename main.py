import sys
import argparse

from svg import SvgGenerate

args = argparse.ArgumentParser()
args.add_argument('--figure', type=str, help='Figure type')
args.add_argument('--color', type=str, help='Figure color in hex')
args.add_argument('--width', type=int, help='Figure width')
args.add_argument('--height', type=int, help='Figure height')
args.add_argument('--filename', type=str, help='File name to save')


def main():
    parse_args = args.parse_args()
    SvgGenerate(
        parse_args.color,
        parse_args.width,
        parse_args.height,
        parse_args.figure,
        parse_args.filename
    ).save()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
    except Exception as e:
        print('Error: {}'.format(e))
        sys.exit(1)
