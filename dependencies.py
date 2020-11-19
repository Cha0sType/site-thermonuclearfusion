def openDependencies():
    header_html = open('templates/header.html') #Opening the header html file
    header = header_html.read() #Reading the file
    header_html.close() #Closing the file

    footer_html = open('templates/footer.html')
    footer = footer_html.read()
    footer_html.close()

    icon_svg = open('static/Icon.svg') #Opening the icon
    icon = icon_svg.read() #Reading the file
    icon_svg.close() #Closing the file

    opened = [header, footer, icon] #Putting the both opend items into an array for better handling
    return opened #Returning the array to make it accessible outside of the function