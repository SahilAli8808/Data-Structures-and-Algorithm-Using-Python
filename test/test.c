#include <stdio.h>
#include<string.h>

// Define a structure to represent a player
struct Player {
    char name[50];
    int runs;
};

// Define a structure to represent a team
struct Team {
    char name[50];
    int totalScore;
    struct Player players[11]; // Assuming 11 players per team
};

int main() {
    struct Team team1, team2;

    // Initialize team names
    strcpy(team1.name, "Team A");
    strcpy(team2.name, "Team B");

    // Initialize player names
    strcpy(team1.players[0].name, "Player 1");
    strcpy(team1.players[1].name, "Player 2");
    // ...

    // Initialize total scores
    team1.totalScore = 0;
    team2.totalScore = 0;

    // Input scores for each ball
    // ...

    // Calculate and update scores
    // ...

    // Display the scoreboard
    printf("Cricket Scoreboard\n");
    printf("------------------\n");
    printf("%s: %d\n", team1.name, team1.totalScore);
    printf("%s: %d\n", team2.name, team2.totalScore);

    return 0;
}
