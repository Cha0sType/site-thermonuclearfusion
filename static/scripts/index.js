
pagebuttons = document.getElementsByTagName('pagebutton');
    for (let i = 0; i < pagebuttons.length; i++) {
        actualinnerHTML = pagebuttons[i].innerHTML;
        pagebuttons[i].innerHTML = '<span class="material-icons" style="color: black; position: absolute; margin-left: -2vw; margin-top: 1.79vw; font-size: 1.7vw;">keyboard_arrow_right</span>' + actualinnerHTML
    }

footer = document.getElementById('footer');
