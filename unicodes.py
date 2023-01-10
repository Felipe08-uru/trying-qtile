from typing import Optional
from libqtile.widget.textbox import TextBox


def left_half_circle(fg_color):
    return TextBox(
        text='\uE0B6',
        fontsize=28,
        foreground=fg_color,
        padding=0)


def right_half_circle(fg_color, bg_color: Optional['str'] = None):
    return TextBox(
        text='\uE0B4',
        fontsize=28,
        background=bg_color,
        foreground=fg_color,
        padding=0)


def lower_left_triangle(bg_color, fg_color):
    return TextBox(
        text='\u25e2',
        padding=0,
        fontsize=50,
        background=bg_color,
        foreground=fg_color)


def left_arrow(bg_color, fg_color):
    return TextBox(
        text='',
        padding=0,
        fontsize=30,
        background=bg_color,
        foreground=fg_color)


def right_arrow(bg_color, fg_color):
    return TextBox(
        text='',
        padding=0,
        fontsize=30,
        background=bg_color,
        foreground=fg_color)
