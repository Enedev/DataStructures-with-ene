// Tic Tac Toe AI with Minimax Algorithm
// The Coding Train / Daniel Shiffman
// https://thecodingtrain.com/challenges/154-tic-tac-toe-minmax
// https://youtu.be/I64-UTORVfU
// https://editor.p5js.org/codingtrain/sketches/0zyUhZdJD


let board = [
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', '']
  ];
  
  let w; // = width / 3;
  let h; // = height / 3;
  
  let ai = 'X';
  let human = 'O';
  let currentPlayer = human;
  
  function setup() {
    createCanvas(600, 600);
    w = width / 4;
    h = height / 4;
  }
  
  function equals3(a, b, c) {
    return a == b && b == c && a != '';
  }
  
  const checkWinner = (board) => {
    let p1 = 0
    let p12 = 0

    let p2 = 0
    let p22 = 1
    
    let p3 = 1
    let p32 = 1

    while(true) {
        if(p32 > 3){
            break
        }

        for(let i = 0; i<3; i++){
            if(board[p1][p12] === board[p2][p22] && board[p2][p22] === board[p3][p32] && board[p1][p12] !== "") {
                //We found a winner
                return board[p1][p12]
            }

            p1++
            p2++
            p3++
        }
        p1 = 0

        p2 = 0
        
        p3 = 1

        p12++
        p22++
        p32++
    }

    let openSpots = 0;
    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 4; j++) {
        if (board[i][j] == '') {
          openSpots++;
        }
      }
    }
  
    if (openSpots == 0) {
      return 'tie';
    }

    //No winner was found
    return null
};

  
  function mousePressed() {
    if (currentPlayer == human) {
      // Human make turn
      let i = floor(mouseX / w);
      let j = floor(mouseY / h);
      console.log(i, j)

      // If valid turn
      if (board[i][j] == '') {
        board[i][j] = human;
        currentPlayer = ai;
        bestMove();
      }
    }
  }
  
  function draw() {
    background(255);
    strokeWeight(4);
  
    line(w, 0, w, height);
    line(w * 2, 0, w * 2, height);
    line(w * 3, 0, w * 3, height);
    line(0, h, width, h);
    line(0, h * 2, width, h * 2);
    line(0, h * 3, width, h * 3);


  
    for (let j = 0; j < 4; j++) {
      for (let i = 0; i < 4; i++) {
        let x = w * i + w / 2;
        let y = h * j + h / 2;
        let spot = board[i][j];
        textSize(32);
        let r = w / 4;
        if (spot == human) {
          noFill();
          ellipse(x, y, r * 2);
        } else if (spot == ai) {
          line(x - r, y - r, x + r, y + r);
          line(x + r, y - r, x - r, y + r);
        }
      }
    }
  
    let result = checkWinner(board);
    if (result != null) {
      noLoop();
      let resultP = createP('');
      resultP.addClass('message-box');
      if (result == 'tie') {
        resultP.html('Tie! Press any key to restart.');
      } else {
        resultP.html(`${result} wins! Press any key to restart.`);
      }
    }
  }

  function resetBoard() {
    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 4; j++) {
        board[i][j] = '';
      }
    }
    currentPlayer = human;
    loop(); // Reactivar el loop de dibujo
  }

  function keyPressed() {
    resetBoard(); // Reiniciar el tablero al presionar cualquier tecla
    select('.message-box').remove(); 
  }
  