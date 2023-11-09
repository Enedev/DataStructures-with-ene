// Tic Tac Toe AI with Minimax Algorithm
// The Coding Train / Daniel Shiffman
// https://thecodingtrain.com/CodingChallenges/154-tic-tac-toe-minimax.html
// https://youtu.be/I64-UTORVfU
// https://editor.p5js.org/codingtrain/sketches/0zyUhZdJD

function bestMove() {
    // AI to make its turn
    let bestScore = -Infinity;
    let move;
    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 4; j++) {
        // Is the spot available?
        if (board[i][j] == '') {
          board[i][j] = ai;
          
          let score = minimax(board, 8, false, -Infinity, Infinity);
          board[i][j] = '';
          if (score > bestScore) {
            bestScore = score;
            move = { i, j };
          }
        }
      }
    }
    board[move.i][move.j] = ai;
    currentPlayer = human

  }
  
  let scores = {
    'X': 1,
    'O': -1,
    'tie': 0
  };

  function minimax(board, depth,  isMaximizing, alpha, beta) {
    
    let result = checkWinner(board);
    if (result !== null) {
      return result === ai ? 1 : result === human ? -1 : 0;
    }

    if(depth === 0) {
      return result === ai ? 1 : result === human ? -1 : 0;
    }
    
    if (isMaximizing) {
      
        let bestScore = -Infinity;
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                // Is the spot available?
                if (board[i][j] == '') {
                    board[i][j] = ai;
                    let score = minimax(board, depth -1, false, alpha, beta);
                    board[i][j] = '';
                    bestScore = Math.max(bestScore, score);
                    alpha = Math.max(alpha, bestScore);
                    if (beta <= alpha) {
                        break; // Beta cutoff
                    }
                }
            }
        }
        return bestScore;
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                // Is the spot available?
                if (board[i][j] == '') {
                    board[i][j] = human;
                    let score = minimax(board, depth -1, true, alpha, beta);
                    board[i][j] = '';
                    bestScore = Math.min(bestScore, score);

                    beta = Math.min(beta, bestScore);
                    if (beta <= alpha) {
                        break; // Alpha cutoff
                    }
                }
            }
        }
        return bestScore;
    }
}

