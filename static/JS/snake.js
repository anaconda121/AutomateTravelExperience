const cvs = document.getElementById("snake");
const context = cvs.getContext("2d");
//const text = "";
//const TEXT_SIZE = 40;
// create the unit
const box = 32;
//const gameOver = false;

var canv = document.getElementById("snake");
// load images

const ground = new Image();
ground.src = "static/imgSnake/ground.png";

const foodImg = new Image();
foodImg.src = "static/imgSnake/food.png";

// load audio files
let dead = new Audio();
let eat = new Audio();
let up = new Audio();
let right = new Audio();
let left = new Audio();
let down = new Audio();

dead.src = "static/audioSnake/dead.mp3";
eat.src = "static/audioSnake/eat.mp3";
up.src = "static/audioSnake/up.mp3";
right.src = "static/audioSnake/right.mp3";
left.src = "static/audioSnake/left.mp3";
down.src = "static/audioSnake/down.mp3";

// create the snake

var snake = new Array();
snake[0] = new Image();
snake[0].src = "static/imgSnake/snake.png";




snake[0] = {
    x : 9 * box,
    y : 10 * box
};

// create the food

let food = {
    x : Math.floor(Math.random()*17+1) * box,
    y : Math.floor(Math.random()*15+3) * box
}

// create the score var

let scoreSnake = 0;

//control the snake

let d;

document.addEventListener("keydown",direction);

function direction(event){

    let key = event.keyCode;
    if( key == 37 && d != "RIGHT"){
        left.play();
        d = "LEFT";
    }else if(key == 38 && d != "DOWN"){
        d = "UP";
        up.play();
    }else if(key == 39 && d != "LEFT"){
        d = "RIGHT";
        right.play();
    }else if(key == 40 && d != "UP"){
        d = "DOWN";
        down.play();
    }
}

// cheack collision function
function collision(head,array){
    for(let i = 0; i < array.length; i++){
        if(head.x == array[i].x && head.y == array[i].y){
            return true;
        }
    }
    return false;
}



// draw everything to the canvas

function draw(){
    
    context.drawImage(ground,0,0);
    
    for( let i = 0; i < snake.length ; i++){
        var imgSrc = document.getElementById("icon");
        var imgRender = context.createPattern(imgSrc, 'repeat');
        context.fillStyle = imgRender;
        context.fillRect(snake[i].x,snake[i].y,box,box);
        context.fill();        
        context.strokeStyle = "#00008B";
        context.strokeRect(snake[i].x,snake[i].y,box,box);
        context.fill();
    }
    
    context.drawImage(foodImg, food.x, food.y);
    
    // old head position
    let snakeX = snake[0].x;
    let snakeY = snake[0].y;
    
    // which direction
    if( d == "LEFT") snakeX -= box;
    if( d == "UP") snakeY -= box;
    if( d == "RIGHT") snakeX += box;
    if( d == "DOWN") snakeY += box;
    
    // if the snake eats the food
    if(snakeX == food.x && snakeY == food.y){
        score++;
        eat.play();
        food = {
            x : Math.floor(Math.random()*17+1) * box,
            y : Math.floor(Math.random()*15+3) * box
        }
        // we don't remove the tail
    }else{
        // remove the tail
        snake.pop();
    }
    
    // add new Head
    
    let newHead = {
        x : snakeX,
        y : snakeY
    }
    
    // game over
    if(snakeX < box || snakeX > 17 * box || snakeY < 3*box || snakeY > 17*box || collision(newHead,snake)){
      /*
        context.textAlign = "center";
        context.textBaseline = "middle";
        context.fillStyle = "rgb(255, 255, 255)";
        context.font = "small-caps " + TEXT_SIZE + "px dejavu sans mono";
        context.fillText("Game Over", canv.width / 2, canv.height * 0.75); 
        dead.play();*/
        const gameResult = false;
    } /*else if (gameResult = false ){
      newGame();
    }*/
    
    snake.unshift(newHead);
    
    context.fillStyle = "white";
    context.font = "45px Changa one";
    context.fillText(score,2*box,1.6*box);
}

// call draw function every 100 ms

let game = setInterval(draw,130);