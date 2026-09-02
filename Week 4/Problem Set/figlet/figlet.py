import pyfiglet
import sys
import random

fonts = pyfiglet.Figlet().getFonts()
if len(sys.argv) == 1:
    input_text = input("Input: ").strip()
    f = pyfiglet.Figlet(font=random.choice(fonts))
    print(f.renderText(input_text))
elif len(sys.argv) == 3:
    if (sys.argv[1] != '-f' and sys.argv[1] != '-font') or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    else:
        input_text = input("Input: ").strip()
        f = pyfiglet.Figlet(font=sys.argv[2])
        print(f.renderText(input_text))
else:
    sys.exit("Invalid usage")