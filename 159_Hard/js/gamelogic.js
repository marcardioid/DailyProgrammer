// GAME OBJECT
function Game() {
	this.games = 0;
	this.playerWins = 0;
	this.aiWins = 0;
	this.ties = 0;
    this.moves = ["rock", "paper", "scissors", "lizard", "spock"];
	this.rules = {
        rock: {scissors, lizard},
        paper: {rock, spock},
        scissors: {paper, lizard},
        lizard: {paper, spock},
        spock: {rock, scissors}
	};
}
Game.prototype.fight = function(playerMove, aiMove) {
    if (playerMove === "random") {
        playerMove = this.moves[Math.floor(Math.random() * this.moves.length)];
    }
    // 0 = draw, 1 = player, 2 = ai
	var result = { 
		winner: 0,
		player: playerMove,
		ai: aiMove
	};
	if (playerMove === aiMove) {
		this.ties++;
	} else if (this.rules[playerMove][aiMove] !== undefined) {
		result.winner = 1;
		this.playerWins++;
	} else {
		result.winner = 2;
		this.aiWins++;
	}
	this.games++;
	return result;
}

// AI OBJECT
function AI(game) {
    this.game = game;
}
AI.prototype.move = function() {}
AI.prototype.lastMatch = function(result) {}

// AI -> EASY
function EasyAI(game){
	AI.call(this, game);
};
EasyAI.prototype = new AI();
EasyAI.prototype.constructor = EasyAI;
EasyAI.prototype.move = function() {
    return this.game.moves[Math.floor(Math.random() * this.game.moves.length)];
};

// AI -> INTERMEDIATE
function IntermediateAI(game){
	AI.call(this, game);
	this.history = {
		'rock': 0,
		'paper': 0,
		'scissors': 0,
		'lizard': 0,
		'spock': 0
	}
};
IntermediateAI.prototype = new AI();
IntermediateAI.prototype.constructor = IntermediateAI;
IntermediateAI.prototype.move = function() {
	// Find the most popular player moves
	var max = 0;
	for (var move in this.history) {
		if (this.history[move] > max) { max = this.history[move]; }
	}
	var popular = [];
	for (var move in this.history) {
		if (this.history[move] === max) { popular.push(move); }
	}
	
	// Find potential winning moves
	var potential = [];
    var _this = this;
    popular.forEach(function(popularMove, k) {
		jQuery.each(_this.game.rules, function(winningMove, v) {
			jQuery.each(v, function(losingMove, v) {
				if (popularMove == losingMove) { potential.push(winningMove); }
			});
		});
	});
	jQuery.unique(potential);
	// Remove popular player moves
	jQuery.each(popular, function(k, v) {
		if (potential.indexOf(v) > -1) { potential.splice(potential.indexOf(v), 1) }
	});
	
	if (potential.length === 0) {
		return this.game.moves[Math.floor(Math.random() * this.game.moves.length)];
	} else {
		return potential[Math.floor(Math.random() * potential.length)];
	}
};
IntermediateAI.prototype.lastMatch = function(result) {
	this.history[result.player]++;
};

// AI -> HARD
function HardAI(game){
	AI.call(this, game);
};
HardAI.prototype = new AI();
HardAI.prototype.constructor = HardAI;
HardAI.prototype.move = function() {
    var aiMove = $(document).find("button:focus")[0].id;
    if (aiMove === undefined) {
        return "rock";
    }
    if (aiMove === "random") {
        return this.game.moves[Math.floor(Math.random() * this.game.moves.length)];
    }
    else {
        var potentialMoves = [];
        for (var potentialMove in this.game.rules) {
            for (var losingMove in this.game.rules[potentialMove]) {
                if (aiMove === losingMove) {
                    potentialMoves.push(potentialMove);
                }
            }
        }
        return potentialMoves[Math.floor(Math.random() * potentialMoves.length)];
    }
};