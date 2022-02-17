import sys
sys.path.append(r"C:\doit")

# 1
import game.sound.echo
game.sound.echo.echo_test()

# 2
from game.sound import echo
echo.echo_test()

# 3
from game.sound.echo import echo_test
echo_test()

## 종료 후 
import sys
sys.path.append(r"C:\doit")

# 1
import game 
game.sound.echo.echo_test()

# 2
import game.sound.echo.echo_test

# 3
from game.sound import *
echo.echo_test()

from game.graphic.render import render_test
render_test()
