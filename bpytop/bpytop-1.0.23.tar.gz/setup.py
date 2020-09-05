# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['bpytop']
install_requires = \
['psutil>=5.7.0,<6.0.0']

entry_points = \
{'console_scripts': ['bpytop = bpytop:main']}

setup_kwargs = {
    'name': 'bpytop',
    'version': '1.0.23',
    'description': 'Resource monitor that shows usage and stats for processor, memory, disks, network and processes.',
    'long_description': '# ![bpytop](https://github.com/aristocratos/bpytop/raw/master/Imgs/logo.png)\n\n![Linux](https://img.shields.io/badge/-Linux-grey?logo=linux)\n![OSX](https://img.shields.io/badge/-OSX-black?logo=apple)\n![FreeBSD](https://img.shields.io/badge/-FreeBSD-red?logo=freebsd)\n![Usage](https://img.shields.io/badge/Usage-System%20resource%20monitor-yellow)\n![Python](https://img.shields.io/badge/Python-v3.6%5E-green?logo=python)\n![bpytop_version](https://img.shields.io/github/v/tag/aristocratos/bpytop?label=version)\n[![pypi_version](https://img.shields.io/pypi/v/bpytop?label=pypi)](https://pypi.org/project/bpytop)\n[![Donate](https://img.shields.io/badge/-Donate-yellow?logo=paypal)](https://paypal.me/aristocratos)\n[![Sponsor](https://img.shields.io/badge/-Sponsor-red?logo=github)](https://github.com/sponsors/aristocratos)\n[![Coffee](https://img.shields.io/badge/-Buy%20me%20a%20Coffee-grey?logo=Ko-fi)](https://ko-fi.com/aristocratos)\n\n## Index\n\n* [Documents](#documents)\n* [Description](#description)\n* [Features](#features)\n* [Themes](#themes)\n* [Support and funding](#support-and-funding)\n* [Prerequisites](#prerequisites)\n* [Dependencies](#dependencies)\n* [Screenshots](#screenshots)\n* [Installation](#installation)\n* [Configurability](#configurability)\n* [TODO](#todo)\n* [License](#license)\n\n## Documents\n\n#### [CHANGELOG.md](https://github.com/aristocratos/bpytop/blob/master/CHANGELOG.md)\n\n#### [CONTRIBUTING.md](https://github.com/aristocratos/bpytop/blob/master/CONTRIBUTING.md)\n\n#### [CODE_OF_CONDUCT.md](https://github.com/aristocratos/bpytop/blob/master/CODE_OF_CONDUCT.md)\n\n## Description\n\nResource monitor that shows usage and stats for processor, memory, disks, network and processes.\n\nPython port of [bashtop](https://github.com/aristocratos/bashtop).\n\n## Features\n\n* Easy to use, with a game inspired menu system.\n* Full mouse support, all buttons with a highlighted key is clickable and mouse scroll works in process list and menu boxes.\n* Fast and responsive UI with UP, DOWN keys process selection.\n* Function for showing detailed stats for selected process.\n* Ability to filter processes, multiple filters can be entered.\n* Easy switching between sorting options.\n* Send SIGTERM, SIGKILL, SIGINT to selected process.\n* UI menu for changing all config file options.\n* Auto scaling graph for network usage.\n* Shows message in menu if new version is available\n* Shows current read and write speeds for disks\n\n## Themes\n\nBpytop uses the same theme files as bashtop so any theme made for bashtop will work.\n\nSee [themes](https://github.com/aristocratos/bpytop/tree/master/themes) folder for available themes.\n\nThe `make install` command places the default themes in `/usr/local/share/bpytop/themes`.\nUser created themes should be placed in `$HOME/.config/bpytop/themes`.\n\nLet me know if you want to contribute with new themes.\n\n## Support and funding\n\nYou can sponsor this project through github, see [my sponsors page](https://github.com/sponsors/aristocratos) for options.\n\nOr donate through [paypal](https://paypal.me/aristocratos) or [ko-fi](https://ko-fi.com/aristocratos).\n\nAny support is greatly appreciated!\n\n## Prerequisites\n\n#### Mac Os X\n\nWill not display correctly in the standard terminal!\nRecommended alternative [iTerm2](https://www.iterm2.com/)\n\nWill also need to be run as superuser to display stats for processes not owned by user.\n\n#### Linux, Mac Os X and FreeBSD\n\nFor correct display, a terminal with support for:\n\n* 24-bit truecolor ([See list of terminals with truecolor support](https://gist.github.com/XVilka/8346728))\n* Wide characters (Are sometimes problematic in web-based terminals)\n\nAlso needs a UTF8 locale and a font that covers:\n\n* Unicode Block “Braille Patterns” U+2800 - U+28FF\n* Unicode Block “Geometric Shapes” U+25A0 - U+25FF\n* Unicode Block "Box Drawing" and "Block Elements" U+2500 - U+259F\n\n#### Notice\n\nDropbear seems to not be able to set correct locale. So if accessing bpytop over ssh, OpenSSH is recommended.\n\n## Dependencies\n\n**[Python3](https://www.python.org/downloads/)** (v3.6 or later)\n\n**[psutil module](https://github.com/giampaolo/psutil)** (v5.7.0 or later)\n\n## Optionals for additional stats\n\n(Optional OSX) **[osx-cpu-temp](https://github.com/lavoiesl/osx-cpu-temp)** Needed to show CPU temperatures.\n\n## Screenshots\n\nMain UI showing details for a selected process.\n![Screenshot 1](https://github.com/aristocratos/bpytop/raw/master/Imgs/main.png)\n\nMain UI in mini mode.\n![Screenshot 2](https://github.com/aristocratos/bpytop/raw/master/Imgs/mini.png)\n\nMain menu.\n![Screenshot 3](https://github.com/aristocratos/bpytop/raw/master/Imgs/menu.png)\n\nOptions menu.\n![Screenshot 4](https://github.com/aristocratos/bpytop/raw/master/Imgs/options.png)\n\n## Installation\n\n### PyPi (will always have latest version)\n\n> Install or update to latest version\n``` bash\npip3 install bpytop --upgrade\n```\n\n### Arch Linux\n\nAvailable in the AUR as `bpytop.git`\n\nhttps://aur.archlinux.org/packages/bpytop/\n\n### Debian based\n\nAvailable for debian/ubuntu from [Azlux\'s repository](http://packages.azlux.fr/)\n\n### FreeBSD package\n\nAvailable in [FreeBSD ports](https://www.freshports.org/sysutils/bpytop/)\n\n>Install pre-built package\n\n``` bash\nsudo pkg install bpytop\n```\n\n### Fedora/CentOS 8 package\n\n[Available](https://src.fedoraproject.org/rpms/bpytop) in the Fedora and [EPEL-8 repository](https://fedoraproject.org/wiki/EPEL).\n\n>Installation\n\n``` bash\nsudo dnf install bpytop\n```\n\n### Snap package\n\nby @kz6fittycent\n\nhttps://github.com/kz6fittycent/bpytop-snap\n\n>Install the package\n``` bash\nsudo snap install bpytop\n```\n\n>Give permissions\n``` bash\nsudo snap connect bpytop:mount-observe\nsudo snap connect bpytop:network-control\nsudo snap connect bpytop:hardware-observe\nsudo snap connect bpytop:system-observe\nsudo snap connect bpytop:process-control\nsudo snap connect bpytop:physical-memory-observe\n```\n\nThe config folder will be located in `~/snap/bpytop/current/.config/bpytop`\n\n## Manual installation\n\n#### Dependencies installation Linux\n\n>Install python3 and git with a package manager of you choice\n\n>Install psutil python module (sudo might be required)\n\n``` bash\npython3 -m pip install psutil\n```\n\n#### Dependencies installation OSX\n\n>Install homebrew if not already installed\n\n``` bash\n/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"\n```\n\n>Install python3 if not already installed\n\n``` bash\nbrew install python3 git\n```\n\n>Install psutil python module\n\n``` bash\npython3 -m pip install psutil\n```\n\n>Install optional dependency osx-cpu-temp\n\n``` bash\nbrew install osx-cpu-temp\n```\n\n#### Dependencies installation FreeBSD\n\n>Install with pkg and pip\n\n``` bash\nsudo pkg install git python3 py37-psutil\n```\n\n#### Manual installation Linux, OSX and FreeBSD\n\n>Clone and install\n\n``` bash\ngit clone https://github.com/aristocratos/bpytop.git\ncd bpytop\nsudo make install\n```\n\n>to uninstall it\n\n``` bash\nsudo make uninstall\n```\n\n## Configurability\n\nAll options changeable from within UI.\nConfig files stored in "$HOME/.config/bpytop" folder\n\n#### bpytop.cfg: (auto generated if not found)\n\n"/etc/bpytop.conf" will be used as default seed for config file creation if it exists.\n\n```bash\n#? Config file for bpytop v. 1.0.22\n\n#* Color theme, looks for a .theme file in "/usr/[local/]share/bpytop/themes" and "~/.config/bpytop/themes", "Default" for builtin default theme.\n#* Prefix name by a plus sign (+) for a theme located in user themes folder, i.e. color_theme="+monokai"\ncolor_theme="Default"\n\n#* If the theme set background should be shown, set to False if you want terminal background transparency\ntheme_background=False\n\n#* Set bpytop view mode, "full" for everything shown, "proc" for cpu stats and processes, "stat" for cpu, mem, disks and net stats shown.\nview_mode=full\n\n#* Update time in milliseconds, increases automatically if set below internal loops processing time, recommended 2000 ms or above for better sample times for graphs.\nupdate_ms=2000\n\n#* Processes sorting, "pid" "program" "arguments" "threads" "user" "memory" "cpu lazy" "cpu responsive",\n#* "cpu lazy" updates top process over time, "cpu responsive" updates top process directly.\nproc_sorting="cpu lazy"\n\n#* Reverse sorting order, True or False.\nproc_reversed=False\n\n#* Show processes as a tree\nproc_tree=False\n\n#* Use the cpu graph colors in the process list.\nproc_colors=True\n\n#* Use a darkening gradient in the process list.\nproc_gradient=True\n\n#* If process cpu usage should be of the core it\'s running on or usage of the total available cpu power.\nproc_per_core=True\n\n#* Show process memory as bytes instead of percent\nproc_mem_bytes=True\n\n#* Check cpu temperature, needs "osx-cpu-temp" on MacOS X.\ncheck_temp=True\n\n#* Draw a clock at top of screen, formatting according to strftime, empty string to disable.\ndraw_clock="%X"\n\n#* Update main ui in background when menus are showing, set this to false if the menus is flickering too much for comfort.\nbackground_update=True\n\n#* Custom cpu model name, empty string to disable.\ncustom_cpu_name=""\n\n#* Optional filter for shown disks, should be last folder in path of a mountpoint, "root" replaces "/", separate multiple values with comma.\n#* Begin line with "exclude=" to change to exclude filter, oterwise defaults to "most include" filter. Example: disks_filter="exclude=boot, home"\ndisks_filter=""\n\n#* Show graphs instead of meters for memory values.\nmem_graphs=True\n\n#* If swap memory should be shown in memory box.\nshow_swap=True\n\n#* Show swap as a disk, ignores show_swap value above, inserts itself after first disk.\nswap_disk=True\n\n#* If mem box should be split to also show disks info.\nshow_disks=True\n\n#* Set fixed values for network graphs, default "10M" = 10 Mibibytes, possible units "K", "M", "G", append with "bit" for bits instead of bytes, i.e "100mbit"\nnet_download="100Mbit"\nnet_upload="100Mbit"\n\n#* Start in network graphs auto rescaling mode, ignores any values set above and rescales down to 10 Kibibytes at the lowest.\nnet_auto=True\n\n#* Sync the scaling for download and upload to whichever currently has the highest scale\nnet_sync=False\n\n#* If the network graphs color gradient should scale to bandwith usage or auto scale, bandwith usage is based on "net_download" and "net_upload" values\nnet_color_fixed=False\n\n#* Show init screen at startup, the init screen is purely cosmetical\nshow_init=False\n\n#* Enable check for new version from github.com/aristocratos/bpytop at start.\nupdate_check=True\n\n#* Set loglevel for "~/.config/bpytop/error.log" levels are: "ERROR" "WARNING" "INFO" "DEBUG".\n#* The level set includes all lower levels, i.e. "DEBUG" will show all logging info.\nlog_level=WARNING\n\n```\n\n#### Command line options:\n\n``` text\nUSAGE: bpytop [argument]\n\nArguments:\n    -f, --full            Start in full mode showing all boxes [default]\n    -p, --proc            Start in minimal mode without memory and net boxes\n    -s, --stat            Start in minimal mode without process box\n    -v, --version         Show version info and exit\n    -h, --help            Show this help message and exit\n    --debug               Start with loglevel set to DEBUG overriding value set in config\n```\n\n## TODO\n\n- [ ] Add gpu temp and usage.\n- [ ] Add cpu and mem stats for docker containers. (If feasible)\n- [x] Change process list to line scroll instead of page change.\n- [ ] Add options for resizing all boxes.\n- [x] Add command line argument parsing.\n\n- [ ] Miscellaneous optimizations and code cleanup.\n\n\n## LICENSE\n\n[Apache License 2.0](https://github.com/aristocratos/bpytop/blob/master/LICENSE)\n',
    'author': 'Aristocratos',
    'author_email': 'jakob@qvantnet.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aristocratos/bpytop',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
