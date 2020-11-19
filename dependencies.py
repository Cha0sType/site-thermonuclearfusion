def openDependencies():
    header_html = open('templates/header.html', encoding="utf-8") #Opening the header html file
    header = header_html.read() #Reading the file
    header_html.close() #Closing the file

    footer_html = open('templates/footer.html', encoding="utf-8")
    footer = footer_html.read()
    footer_html.close()

    icon_svg = open('static/Icon.svg', encoding="utf-8") #Opening the icon
    icon = icon_svg.read() #Reading the file
    icon_svg.close() #Closing the file

    opened = [header, footer, icon] #Putting the both opend items into an array for better handling
    return opened #Returning the array to make it accessible outside of the function