from libqtile.bar import Bar
from libqtile.widget.check_updates import CheckUpdates
from libqtile.widget.clock import Clock
from libqtile.widget.cmus import Cmus
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.battery import Battery
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.quick_exit import QuickExit
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.volume import Volume
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName

from unicodes import right_arrow, left_arrow
from colors import catppuccin

bar = Bar([
    GroupBox(
        disable_drag=True,
        fontsize = 20,
        active=catppuccin['text'],
        inactive=catppuccin['subtext1'],
        highlight_method='line',
        block_highlight_text_color=catppuccin['yellow'],
        borderwidth=0,
        highlight_color=catppuccin['surface2'],
        background=catppuccin['surface2']
    ),
    right_arrow(catppuccin['surface1'], catppuccin['surface2']),
    CurrentLayout(
        background=catppuccin['surface1'],
        foreground=catppuccin['text']
    ),
    right_arrow(catppuccin['surface0'], catppuccin['surface1']),
    WindowCount(
        text_format='缾 {num}',
        background=catppuccin['surface0'],
        foreground=catppuccin['text'],
        show_zero=True,
    ),
    right_arrow(catppuccin['base'], catppuccin['surface0']),
    Volume(
        background=catppuccin['base'],
        foreground=catppuccin['text'],
        scroll=True,
        emoji=True,
    ),
    right_arrow(catppuccin['mantle'], catppuccin['base']),
    WindowName(foreground=catppuccin['text']),
    left_arrow(catppuccin['mantle'], catppuccin['base']),
    Cmus(
        background=catppuccin['base'],
        foreground=catppuccin['green'],
        play_color=catppuccin['green'],
    ),
    left_arrow(catppuccin['base'], catppuccin['surface0']),
    CheckUpdates(
        background=catppuccin['surface0'],
        foreground=catppuccin['yellow'],
        colour_no_updates=catppuccin['yellow'],
        colour_have_updates=catppuccin['red']
    ),
    Net(
        background=catppuccin['surface0'],
        foreground=catppuccin['yellow']
    ),
    left_arrow(catppuccin['surface0'], catppuccin['surface1']),
    Clock(
        background=catppuccin['surface1'],
        foreground=catppuccin['shappire'],
        format=' %Y-%m-%d %a %I:%M %p'
    ),
    left_arrow(catppuccin['surface1'], catppuccin['surface2']),
    Battery(
        background=catppuccin['surface2'],
        foreground=catppuccin['lavender'],
        format='{percent:2.0%} {hour:d}:{min:02d}',
    ),
    left_arrow(catppuccin['surface2'], catppuccin['overlay0']),
    QuickExit(
        default_text=' ',
        fontsize=20,
        foreground=catppuccin['maroon'],
        countdown_format='[{}]',
        background=catppuccin['overlay0'],
    ),
    Systray(
        background=catppuccin['overlay0'],
    ),
], background=catppuccin['mantle'], size=32, margin=5)
