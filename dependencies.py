def openDependencies():
    header_html = open('templates/header.html')
    header = header_html.read()
    header_html.close()

    icon_svg = open('static/Icon.svg')
    icon = icon_svg.read()
    icon_svg.close()
    opend = [header, icon]
    return opend