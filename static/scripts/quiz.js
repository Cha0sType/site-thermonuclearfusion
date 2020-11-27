
questions = ["2", "3", "4", "5", "6", "7", "8", "9", "10"];
a1 = ["2", "3", "4", "5", "6", "7", "8", "9", "10"];
a2 = ["2", "3", "4", "5", "6", "7", "8", "9", "10"];
a3 = ["2", "3", "4", "5", "6", "7", "8", "9", "10"];
correctAnswers = [1, 2, 3, 1, 2, 3, 1, 2, 3, 2];

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
        document.getElementById('percentage').innerHTML = (questionNum) * 10 + "%";
        document.getElementById('barfront').style.width = (questionNum) * 4 + "vw";
        document.getElementById('barlight').style.width = (questionNum) * 4 - 1 + "vw";
        document.getElementById('question').innerHTML = questions[questionNum - 1];
        document.getElementById('a1').innerHTML = a1[questionNum - 1];
        document.getElementById('a2').innerHTML = a2[questionNum - 1];
        document.getElementById('a3').innerHTML = a3[questionNum - 1];
    }, 1500);
}