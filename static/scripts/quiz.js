
questions = ["Wie heiß muss es mindestens in einem Fusionsreaktor sein,<br>damit er auf der Erde funktioniert?", "3", "Wofür steht die Abkürzung ITER?", "5", "Welche Halbwertszeit hat Tritium?", "7", "Wo wird ITER gebaut?", "Wie viele Neutronen hat Deuterium<br>und wie viele Tritium?", "10"];
a1 = ["100 Tsd. °C", "3", "Internationaler Toller Erfindungsreaktor", "5", "12,1 Jahre", "7", "Im Süden Frankreichs", "Deuterium hat eins, Tritium zwei", "10"];
a2 = ["100 Mio. °C", "3", "<span style='font-size: 1.8vw;'>International Thermonuclear Experimental Reactor</span>", "5", "12,2 Jahre", "7", "Im Süden Spanienes", "Deuterium hat drei, Tritium zwei", "10"];
a3 = ["100 Mrd. °C", "3", "International Testing Experiment Reactor", "5", "12,3 Jahre", "7", "Im Südosten Frankreichs", "Deuterium hat keine, Tritium drei", "10"];
correctAnswers = [1, 2, 3, 2, 3, 3, 1, 1, 1, 2];
//   Question No. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

questionNum = 0;
score = 0;
result = undefined;
answering = false;

function answer(index) {
    if (!answering) {
        answering = true;
        if (index == correctAnswers[questionNum]) {
            score++;
            result = true;
        } else {
            result = false;
        }

        questionNum++;
        ask(index);
        setTimeout(() => {
            if (questionNum == 3) {
                document.getElementById('secret').style.display = "block";
            } else {
                document.getElementById('secret').style.display = "none";
            }
        }, 1500);
    }
}

function ask(i) {
    if (result) {
        if (i == 1) {
            style = document.getElementById('a1').style;
            document.getElementById('a1').style.backgroundColor = "#0EDF00";
            document.getElementById('a1').style.borderColor = "#0ba700";
            document.getElementById('a1').style.color = "white";
            setTimeout(() => {
                document.getElementById('a1').style = style;
                answering = false;
            }, 1500);
        } else if (i == 2) {
            style = document.getElementById('a2').style;
            document.getElementById('a2').style.backgroundColor = "#0EDF00";
            document.getElementById('a2').style.borderColor = "#0ba700";
            document.getElementById('a2').style.color = "white";
            setTimeout(() => {
                document.getElementById('a2').style = style;
                answering = false;
            }, 1500);
        } else {
            style = document.getElementById('a3').style;
            document.getElementById('a3').style.backgroundColor = "#0EDF00";
            document.getElementById('a3').style.borderColor = "#0ba700";
            document.getElementById('a3').style.color = "white";
            setTimeout(() => {
                document.getElementById('a3').style = style;
                answering = false;
            }, 1500);
        }
    } else {
        if (i == 1) {
            style = document.getElementById('a1').style;
            document.getElementById('a1').style.backgroundColor = "red";
            document.getElementById('a1').style.borderColor = "darkred";
            document.getElementById('a1').style.color = "white";
            setTimeout(() => {
                document.getElementById('a1').style = style;
                answering = false;
            }, 1500);
        } else if (i == 2) {
            style = document.getElementById('a2').style;
            document.getElementById('a2').style.backgroundColor = "red";
            document.getElementById('a2').style.borderColor = "darkred";
            document.getElementById('a2').style.color = "white";
            setTimeout(() => {
                document.getElementById('a2').style = style;
                answering = false;
            }, 1500);
        } else {
            style = document.getElementById('a3').style;
            document.getElementById('a3').style.backgroundColor = "red";
            document.getElementById('a3').style.borderColor = "darkred";
            document.getElementById('a3').style.color = "white";
            setTimeout(() => {
                document.getElementById('a3').style = style;
                answering = false;
            }, 1500);
        }
    }

    setTimeout(() => {
        if (questionNum < 10) {
            document.getElementById('percentage').innerHTML = (questionNum) * 10 + "%";
            document.getElementById('barfront').style.width = (questionNum) * 4 + "vw";
            document.getElementById('barlight').style.width = (questionNum) * 4 - 1 + "vw";
            document.getElementById('question').innerHTML = questions[questionNum - 1];
            document.getElementById('a1').innerHTML = a1[questionNum - 1];
            document.getElementById('a2').innerHTML = a2[questionNum - 1];
            document.getElementById('a3').innerHTML = a3[questionNum - 1];
        } else {
            endtext = "";

            if (score == 0) {
                endtext = "Das ist jetzt schon ganz gut,<br>aber sieh dir besser erst mal die anderen Seiten an,<br>bevor du das Quiz machst...";
            } else if (score < 4 && score > 0) {
                endtext = "War jetzt ehrlich nicht so dufte, aber immerhin.";
            } else if (score < 7 && score > 0) {
                endtext = "Das ist schon ganz gut, aber sieh dir ein paar Seiten besser nochmal an.";
            } else if (score < 10 && score > 0) {
                endtext = "Boah, das war schon echt gut! ABER NICHT GUT GENUG!!!";
            } else if (score == 10) {
                endtext = "Mein lieber Herr Gesangsverein,<br>du bist halt schon wirklich gut drin im Thema!";
            } else if (score > 10) {
                endtext = "Hacker. Hör auf damit.";
            } else if (score < 0) {
                endtext = "Äääh, jetzt mal ganz ehrlich,<br>SO SCHLECHT kann man doch echt nicht sein!!!";
            }

            document.getElementsByTagName('quiz')[0].innerHTML = '<span id="percentage">100%</span><div id="barback"><div id="barfront" style="width: 40vw; box-shadow: none;"><div id="barlight" style="width: 39vw;"></div></div></div><h1 style=\'text-align: center; margin-left: 0vw; margin-top: 11vw; font-size: 3vw;\'>Herzlichen Glückwunsch,<br>du hast ' + score + ' von 10 Fragen richtig beantwortet!<br>' + endtext + '</h1><button onclick="location.href=\'/\'" style=\'margin-left: 50%; margin-top: 5vw; transform: translateX(-50%); border-bottom: none; background-color: #0ed100; color: white; padding-left: 0vw; text-align: center; width: 25vw;\'>Zurück zum Hauptmenü</button>';
        }
    }, 1500);
}