
#!/bin/bash

ssh  'python3 /Schreibtisch/Bricks/Brick1/main.py' &
ssh enx121653818af0 'python3 /Schreibtisch/Bricks/Brick2/main.py' &
ssh enx12165381750d 'python3 /Schreibtisch/Bricks/Brick3/main.py' &
ssh enx121653651766 'python3 /Schreibtisch/Bricks/Brick4/main.py' &
wait