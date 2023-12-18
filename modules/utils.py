#!/usr/bin/env python3
import shutil
import json
import tempfile

from .colors import colors
from pathlib import Path
from git import Repo, Blob
from .gtfobins import get_bins
from .lolbas import get_exe
from rapidfuzz import process, fuzz

def check_init():
    home_dir = Path.home()
    gibnme_dir = home_dir / '.gibme'
    if not gibnme_dir.exists():
        initialize_settings()
    
    return gibnme_dir

def initialize_settings():
    print('Initializing settings...')
    home_dir = Path.home()
    gibnme_dir = home_dir / '.gibme'
    if not gibnme_dir.exists():
        gibnme_dir.mkdir()
    
    gtfobins_file = gibnme_dir / 'gtfobins.json'
    if not gtfobins_file.exists():
        gtfobins_file.touch()
        update_gtfo(gtfobins_file)

    lolbas_file = gibnme_dir / 'lolbas.json'
    if not lolbas_file.exists():
        lolbas_file.touch()
        update_lolbas(lolbas_file)
    
    shell_file = gibnme_dir / 'shell.json'
    if not shell_file.exists():
        shell_file.touch()
        update_shell(shell_file)

    settings_file = gibnme_dir / 'settings.json'
    if not settings_file.exists():
        settings_file.touch()
        with open(settings_file, 'w') as f:
            data = {'gtfobins_file': str(gtfobins_file), 'lolbas_file': str(lolbas_file), 'shell_file': str(shell_file)}
            json.dump(data, f)

    print('Settings initialized successfully')

def update_gtfo_local(gibnme_dir: Path):
    print('Updating GTFOBins...')

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_url = "https://github.com/GTFOBins/GTFOBins.github.io.git"
        
        repo = Repo.clone_from(repo_url, temp_dir, branch='master', depth=1)
        
        tree = repo.head.commit.tree

        for item in tree:
            if item.path == '_gtfobins':
                for sub_item in item:
                    if isinstance(sub_item, Blob):
                        shutil.copy(sub_item.abspath, gibnme_dir / 'gtfobins' / sub_item.name)

        repo.close()

def update_shell(shell_json_file: Path):
    pass

def update_lolbas(lolbas_json_file: Path):
    if not lolbas_json_file.exists():
        initialize_settings()

    lolbas_choice = get_exe()
    data = {'exe': lolbas_choice}

    with lolbas_json_file.open('w') as f:
        json.dump(data, f)

def update_gtfo(gtfo_json_file: Path):
    if not gtfo_json_file.exists():
        initialize_settings()

    gtfo_choice = get_bins()
    data = {'bins': gtfo_choice}

    with gtfo_json_file.open('w') as f:
        json.dump(data, f)

def update_gibme():
    # print('Updating Gibme...')
    # home_dir = Path.home()
    # gibnme_dir = home_dir / '.gibme'
    # update_gtfo(gibnme_dir)
    # print('Gibme updated successfully')
    pass

def fuzz_name(name: str, type_str: str, choice_path: Path):
    choice_path = choice_path / f'{type_str}.json'
    with open(choice_path, 'r') as f:
        if type_str == 'gtfobins':
            data = json.load(f)
            choice = data['bins']
            fuzz_similarity = process.extract(name, choice, scorer=fuzz.ratio, limit=10)
            highest_similarity = max(fuzz_similarity, key=lambda x: x[1])
            if highest_similarity[1] > 90:
                return highest_similarity[0]
            print(colors("Did you mean one of these?", 'yellow'))  # Print the question in yellow
            for name, similarity, index in fuzz_similarity:
                # Print the name in green and the similarity in cyan
                print(colors(f"{name}:", 'green'), colors(f"{format(similarity, '.1f')}% similarity", 'cyan'))
            exit(0)
        
        elif type_str == 'lolbas':
            pass