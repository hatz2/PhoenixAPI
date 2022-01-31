# Instant combat bot

This bot is able to complete an instant combat and take the rewards of every round if you set it up correctly.

## Requirements

* If you want to kill enemies set a high scan radius in the `Farming/Attack/Combat` tab and add the skills that you want to use in the `Farming/Attack/Player skills` tab.

* If you want to heal your character set the items in the `Farming/Items` tab.

* Additionally you can set up the `Farming/Loot` tab and the `Security` tab.

* The instant combat bot settings are in a file named `ic_settings.ini`, there you can change the bot options (move to players, move to a point, the point coordinates, etc).
  
  ```ini
  # ic_settings.ini example
  [Settings]
  afk_last_round=true
  move_to_players=false
  move_to_point=true
  x=35
  y=64
  ```

## How to use

1. Inject Phoenix Bot into the game.

2. Set up the bot taking into account the requirements listed above.

3. Open InstantCombat.exe

4. Select the index of the port that you want to use the bot on (You can find it in the bot title bar).
