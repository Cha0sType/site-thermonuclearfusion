def openDependencies():
    header_html = open('templates/header.html') #Opening the header html file
    header = header_html.read() #Reading the file
    header_html.close() #Closing the file

    icon_svg = open('static/Icon.svg') #Opening the icon
    icon = icon_svg.read() #Reading the file
    icon_svg.close() #Closing the file

    opend = [header, icon] #Putting the both opend items into an array for better handling
    return opend #Returning the array to make it accessible outside of the function