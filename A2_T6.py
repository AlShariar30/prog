print("Program starting.", end='\n')

hex_color = input("Insert a hex color: ").strip()


if len(hex_color) == 7 and hex_color.startswith('#') and all(c in '0123456789ABCDEF' for c in hex_color[1:].upper()):
 
    red = hex_color[1:3]
    green = hex_color[3:5]
    blue = hex_color[5:7]

    print("\nColors")
    print(f"- Red {red}")
    print(f"- Green {green}")
    print(f"- Blue {blue}")
else:
    print("Invalid hex color format. Please enter a valid hex color.")

print("Program ending.", end='')