import argparse

parser = argparse.ArgumentParser()

# Flag to start program on bot mode
parser.add_argument("-b", "--bot", action='store_true',
                    help="play using a bot")
# Flag to start program on video capture mode
parser.add_argument("-v", "--video", action='store_true',
                    help="play using video capture")

args = parser.parse_args()

