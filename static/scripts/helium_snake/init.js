
function init() {
    px = 5 // player x (head)
    py = 10; // player y (head)
    gridSize = 20; // grid size
    dx = dy = 10; // deuterium x | deuterium y
    tx = ty = 5; // tritium x | tritium y
    hx = hy = -2; // helium x | helium y
    xv = yv = 0; // velocity
    dxv = dyv = 0; // deuterium velocity
    dspeed = 0;
    doshoot = false;
    deuteriumActivated = true;
    tritiumActivated = true;
    gamestarted = false;

    trail = []; // trail x's and y's
    tailLength = 2; // trail length (head not included)

    deuteriumCollected = false;
}

init();

fps = 15;

window.onload = function() {
    canv = document.getElementById("snake");
    ctx = canv.getContext("2d");
    document.addEventListener("keydown", keyPush);
    setInterval(run, 1000/fps);
}

function draw() {
    ctx.fillStyle = "rgb(3, 167, 3)";
    ctx.fillRect(0, 0, canv.width, canv.height);

    ctx.fillStyle = "orange";
    ctx.fillRect(tx * gridSize, ty * gridSize, gridSize - 2, gridSize - 2);
    ctx.fillStyle = "white";
    ctx.fillRect(hx * gridSize, hy * gridSize, gridSize - 2, gridSize - 2);
    ctx.fillStyle = "aqua";
    ctx.fillRect(px * gridSize, py * gridSize, gridSize - 2, gridSize - 2);
    ctx.fillStyle = "red";
    ctx.fillRect(dx * gridSize, dy * gridSize, gridSize - 2, gridSize - 2);

    ctx.fillStyle = "aqua";
    for (let i = 0; i < trail.length; i++) {
        ctx.fillRect(trail[i].x * gridSize, trail[i].y * gridSize, gridSize - 2, gridSize - 2);
    }
}

function run() {
    if (xv != 0 && yv != 0) {
        gamestarted = true;
    }
    if (xv != 0 || yv != 0) {
        trail.push({x: px, y: py}); // add px and py to list as first part of the trail
    }
    while (trail.length > tailLength) {
        trail.shift(); // removes the last element in the list while the list is longer than the tailLength variable
    }

    px += xv;
    py += yv;
    if(px < 0) {
        px = gridSize - 1;
    }
    if(px > gridSize - 1) {
        px = 0;
    }
    if(py < 0) {
        py = gridSize - 1;
    }
    if(py > gridSize - 1) {
        py = 0;
    }
    if (px == dx && py == dy && !deuteriumCollected) {
        deuteriumCollected = true;
    }

    if (deuteriumCollected) {
        dx = px;
        dy = py;
    }

    if (doshoot && deuteriumActivated) {
        while (doshoot) {
            dx += dxv;
            dy += dyv;
            if(dx < 0) {
                dx = gridSize - 1;
            }
            if(dx > gridSize - 1) {
                dx = 0;
            }
            if(dy < 0) {
                dy = gridSize - 1;
            }
            if(dy > gridSize - 1) {
                dy = 0;
            }
            dspeed -= 1;
            if (dspeed == 0) {
                doshoot = false;
            }

            if (dx == tx && dy == ty && deuteriumActivated && tritiumActivated) {
            makeHelium();
            }
        }
    }

    if (px == hx && py == hy) {
        tailLength++;
        deuteriumActivated = tritiumActivated = true;
        hx = hy = -2;
        do {
            dx = Math.floor(Math.random() * gridSize);
            dy = Math.floor(Math.random() * gridSize);
            tx = Math.floor(Math.random() * gridSize);
            ty = Math.floor(Math.random() * gridSize);
        } while ((dx == px && dy == py) || (tx == px && ty == py) || (dx == tx && dy == ty) || {x: dx, y: dy} in trail || {x: tx, y: ty} in trail);
    }

    for (let i = 0; i < trail.length; i++) {
        if (px == trail[i].x && py == trail[i].y) {
            gamestarted = false;
        xv = 0;
        yv = 0;
        px = -1;
        video = document.getElementById('bomb');
        video.style.display = "block";
        video.play();
        setTimeout(() => {
            video.pause();
            video.currentTime = 0;
            video.style.display = "none";
            init();
        }, 6000);
        }
    }

    if ((px == tx && py == ty) || {x: px, y: py} in trail && gamestarted) {
        gamestarted = false;
        xv = 0;
        yv = 0;
        px = -1;
        video = document.getElementById('bomb');
        video.style.display = "block";
        video.play();
        setTimeout(() => {
            video.pause();
            video.currentTime = 0;
            video.style.display = "none";
            init();
        }, 6000);
    }

    draw();
}

function shoot() {
    deuteriumCollected = false;
    doshoot = true;
    dxv = xv;
    dyv = yv;
    dspeed = 4;
}

function makeHelium() {
    deuteriumActivated = tritiumActivated = doshoot = false;
    hx = tx;
    hy = ty;
    dx = dy = tx = ty = -2;
}

function keyPush(evt) {
    switch(evt.keyCode) {
        case 37:
            if (xv != 1) {xv=-1;yv=0;}
            break;
        case 38:
            if (yv != 1) {xv=0;yv=-1;}
            break;
        case 39:
            if (xv != -1) {xv=1;yv=0;}
            break;
        case 40:
            if (yv != -1) {xv=0;yv=1;}
            break;
        case 32:
            if (deuteriumCollected) {
                shoot();
            }
            break;
        default:
            xv=yv=0;
    }
}