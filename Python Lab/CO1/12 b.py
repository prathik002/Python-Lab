colors = input("Enter color names separated by commas: ")
color_list = [c.strip() for c in colors.split(",")]
print("List of colors:", color_list)
if color_list:  
    print("First color:", color_list[0])
    print("Last color:", color_list[-1])
else:
    print("No colors entered.")
