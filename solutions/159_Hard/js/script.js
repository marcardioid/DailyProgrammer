var g;
var ai;

$(document).ready(function() {
    g = new Game();
    ai = new IntermediateAI(g);
    var pieData = [
            {
                value: 1,
                color:"#dff0d8",
                highlight: "#dff0d8",
                label: "Your wins"
            },
            {
                value: 1,
                color: "#f2dede",
                highlight: "",
                label: "AI wins"
            },
            {
                value: 1,
                color: "#fcf8e3",
                highlight: "#fcf8e3",
                label: "Ties"
            }

    ];
    var ctx = document.getElementById("chart-area").getContext("2d");
    myPie = new Chart(ctx).Pie(pieData, {responsive: true, animationSteps: 20, animationEasing: "linear"});

    $('#player-buttons button').on("click touchstart", function(e) {
        e.stopPropagation();
        e.preventDefault();
        var playerMove = this.id;
        var aiMove = ai.move();
        var result = g.fight(playerMove, aiMove);

        ai.lastMatch(result); 
        displayResult(result);
        displayStats();
    });

    $('select#ai-difficulty').change(function() {
        // Create new AI
        var difficulty = $('select#ai-difficulty').val();
        switch (difficulty) {
            case 'easy':
                ai = new EasyAI(g);
                break;
            case 'intermediate':
                ai = new IntermediateAI(g);
                break;
            case 'hard':
                ai = new HardAI(g);
                break;
            default:
                ai = new AI(g);
        }
        
        // Restart
        g = new Game();
        $('#results tr').slice(1).remove();
        $('#results').css('visibility', 'hidden');
        $('#stats').css('visibility', 'hidden');
        $('#results-ai').text('AI ('+difficulty+')');
    });
});

function displayResult(result) {
    var html = '<tr>';
    if (result.winner == 1) {
        html += '<td class="success">'+result.player+'</td><td class="danger">'+result.ai+'</td>';
    } else if (result.winner == 2) {
        html += '<td class="danger">'+result.player+'</td><td class="success">'+result.ai+'</td>';			
    } else {
        html += '<td class="warning">'+result.player+'</td><td class="warning">'+result.ai+'</td>';
    }
    html += '</tr>';
    if ($('#results tr').length >= 14) {
        $('#results tr:nth-child(2)').remove();
    }
    $('#results').append(html);
    $('#results').css('visibility', 'visible');
    $('#stats').css('visibility', 'visible');
};

function displayStats() {
    $('#games').text(g.games);
    $('#player-wins').text(g.playerWins + ' (' + Math.round((g.playerWins / g.games) * 100) + '%)');
    $('#ai-wins').text(g.aiWins + ' (' + Math.round((g.aiWins / g.games) * 100) + '%)');
    $('#ties').text(g.ties + ' (' + Math.round((g.ties / g.games) * 100) + '%)');
    myPie.segments[0].value = g.playerWins;
    myPie.segments[1].value = g.aiWins;
    myPie.segments[2].value = g.ties;
    myPie.update();
};