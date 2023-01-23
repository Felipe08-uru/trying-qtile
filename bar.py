from libqtile.bar import Bar
from libqtile.widget.check_updates import CheckUpdates
from libqtile.widget.clock import Clock
from libqtile.widget.cmus import Cmus
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.battery import Battery
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.net import Net
from libqtile.widget.quick_exit import QuickExit
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.textbox import TextBox
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
    right_arrow(catppuccin['mantle'], catppuccin['base']),
    WindowName(foreground=catppuccin['text']),
    left_arrow(catppuccin['mantle'], catppuccin['base']),
    Cmus(
        background=catppuccin['base'],
        foreground=catppuccin['green'],
        play_color=catppuccin['green'],
    ),
    CheckUpdates(
        background=catppuccin['base'],
        foreground=catppuccin['red'],
        colour_no_updates=catppuccin['red'],
        colour_have_updates=catppuccin['red'],
        distro='Arch',
    ),
    left_arrow(catppuccin['base'], catppuccin['surface0']),
    Net(
        background=catppuccin['surface0'],
        foreground=catppuccin['yellow']
    ),
    left_arrow(catppuccin['surface0'], catppuccin['surface1']),
    TextBox(
        background=catppuccin['surface1'],
        foreground=catppuccin['shappire'],
        text='󱨴',
        fontsize=20,
        padding=0
    ),
    Clock(
        background=catppuccin['surface1'],
        foreground=catppuccin['shappire'],
        format='%d/%m/%Y %I:%M %p',
    ),
    left_arrow(catppuccin['surface1'], catppuccin['surface2']),
    TextBox(
        text='󱊢',
        fontsize=20,
        padding=0,
        background=catppuccin['surface2'],
        foreground=catppuccin['lavender']
    ),
    Battery(
        background=catppuccin['surface2'],
        foreground=catppuccin['lavender'],
        format='{percent:2.0%}',
    ),
    left_arrow(catppuccin['surface2'], catppuccin['overlay0']),
    QuickExit(
        default_text=' ',
        fontsize=20,
        foreground=catppuccin['maroon'],
        countdown_format='[  ]',
        countdown_start=1,
        background=catppuccin['overlay0'],
    ),
    Systray(
        background=catppuccin['overlay0'],
    ),
], background=catppuccin['mantle'], size=32, margin=8)
