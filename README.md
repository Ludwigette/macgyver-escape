<!-- README.md --- 
;; 
;; Filename: README.md
;; Author: Louise <louise>
;; Created: Fri Nov 15 18:27:51 2019 (+0100)
;; Last-Updated: Fri Nov 15 18:37:50 2019 (+0100)
;;           By: Louise <louise>
 -->

# McGyver's Escape
## Synopsis

This game is a labyrinth game. You control McGyver,
and you have to collect all three items to put the
guard to sleep. If you go to the guard before you
have collected the three items, you lose. If you
do it with the three items in your pocket, you win.

Simple as that.

## Building

Building the game is fairly straightforward : Install
the dependencies in a virtual environment, then run
`main.py`. In other words :

	virtualenv -p python3 env
	pip3 install -r requirements.txt
	python3 -m main # Or ./main.py
