TWE Mode Configuration (config-twe/qtile/config.py)
This file is designed for MonadTall Layout and a High-Data Density Bar.

Python

# LAYOUTS: MonadTall Layout Focus
layouts = [
    layout.MonadTall(
        border_focus='#81A1C1', # nord9 - Faded Royal Blue
        border_normal='#4C566A', # nord3
        margin=5,
        ratio=0.55 # Slightly wider main window for productivity
    ),
    # Max layout included as an alternate
    layout.Max(
        border_focus='#81A1C1',
        border_normal='#4C566A',
        margin=5,
    ),
]

# BAR: High-Data Density Bar (Segmented, Productivity Info)
screens = [
    Screen(
        top=bar.Bar([
            widget.GroupBox(
                background="#2E3440", # nord0
                active="#81A1C1", # nord9
                inactive="#4C566A", # nord3
                highlight_method="block",
            ),
            widget.Prompt(),
            # High-Density Widgets
            widget.Net(
                interface="wlan0", # Adjust to your actual network interface
                format='{down}↓↑{up}',
                foreground="#A3BE8C", # nord14 (Green/Success)
            ),
            widget.Sep(),
            widget.CPU(
                format='CPU: {load_percent}%',
                foreground="#D08770" # nord12 (Orange/Warning)
            ),
            widget.Memory(
                format='Mem: {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
                foreground="#EBCB8B" # nord13 (Yellow/Data)
            ),
            widget.Spacer(),
            widget.WindowName(foreground="#D8DEE9"), # nord4
            widget.Clock(format="%I:%M:%S %p", foreground="#D8DEE9"),
            widget.Systray(),
        ],
        size=28,
        background="#2E3440", # nord0
        opacity=1.0 # Slightly less transparent to hold all the data
        ),
    ),
]

# KEYBINDING for Toggle
keys = [
    # TWE Toggle: Super + T
    Key([mod], "t", lazy.spawn("~/dotfiles/toggle_tweak.sh"), desc="Toggle TWE/Sleek Mode"),
    # ... other standard keybindings for window manipulation/resizing
]
