from libqtile.bar import Bar
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName

from unicodes import right_arrow, left_arrow
from colors import catppuccin

bar = Bar([
    GroupBox(
        disable_drag=True,
        active=catppuccin['text'],
        inactive=catppuccin['subtext1'],
        highlight_method='line',
        block_highlight_text_color=catppuccin['blue'],
        borderwidth=0,
        highlight_color=catppuccin['surface1'],
        background=catppuccin['surface1']
    ),
    right_arrow(catppuccin['surface0'], catppuccin['surface1']),
    CurrentLayout(
        background=catppuccin['surface0'],
        foreground=catppuccin['text']
    ),
    right_arrow(catppuccin['base'], catppuccin['surface0']),

    WindowCount(
        text_format='缾 {num}',
        background=catppuccin['base'],
        foreground=catppuccin['text'],
        show_zero=True,
    ),

    right_arrow(catppuccin['surface1'], catppuccin['base']),
    WindowName(foreground=catppuccin['text']),

    left_arrow(catppuccin['surface1'], catppuccin['base']),
    CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=catppuccin['base'],
        foreground=catppuccin['green']
    ),

    left_arrow(catppuccin['base'], catppuccin['surface0']),
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
    Systray(
        background=catppuccin['surface2']
    ),

    Spacer(length=20, background=catppuccin['surface2'])
], background=catppuccin['surface1'], size=32, margin=5)
