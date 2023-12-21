# Gibme - Unleashing the CLI Superpowers!

Gibme is your CLI sidekick, ready to generate shells, hunt down binaries, and so much more. With the power of GTFOBins and LOLBAS at its fingertips, it's like having your own personal information superhero right in your terminal.

## Features

- Binaries from GTFOBins? Gibme got 'em! And it'll print them directly to your CLI, no fuss.
- Executables from LOLBAS? Gibme is on it! It'll print them out for you, neat and tidy.
- Need a variety of reverse shells? Gibme is your shell sommelier, ready to serve.
- Quick search and print out a note or cheatsheet? Gibme is faster than a caffeinated librarian.
- Got your own custom notes? Gibme can load them up for you, making it your personalized CLI companion.
- RapidFuzz integration for swift and effortless searching? Gibme is all over it.
- Easy updates? Gibme is your maintenance-free buddy.

## Getting Started

The easiest way to get started is to download the precompiled binary for Linux. You can find it in the [release section](https://github.com/foreztgump/gibme/releases) of the Gibme repository.

After downloading the binary, you'll need to make it executable and move it to a directory in your PATH. Here's how you can do that:

```sh
# Navigate to the directory where you downloaded the binary
cd /path/to/download/directory

# Make the binary executable
chmod +x gibme

# Move the binary to a directory in your PATH, e.g., /usr/local/bin
sudo mv gibme /usr/local/bin/

Now, you should be able to run Gibme from anywhere in your terminal by simply typing gibme.
```

For those who prefer a hands-on approach, you can clone the repository and set up the required Python packages:

```sh
git clone https://github.com/foreztgump/gibme.git
cd gibme
pip install -r requirements.txt
```

## Configuration

When you first run Gibme, it will create a `.gibme` directory in your home folder. This directory contains a `settings.json` file, which is used to store your personal configurations.

One of the configurations you can set is the path to your custom note folder. This allows Gibme to load your personal notes, making it a truly personalized CLI tool.

To set the path to your custom note folder, open the `settings.json` file in a text editor and set the value of the `custom_notes_dir` key to the path of your note folder. Here's an example:

```json
{
  "custom_notes_dir": "/path/to/your/notes_folder"
}

Replace /path/to/your/notes with the actual path to your note folder. After saving the settings.json file, Gibme will load your custom notes the next time you run it. 
```

## How to Use
    gibme -u        Update Gibme.
    gibme -b less   Search for the binary 'less' on GTFOBins.
    gibme -e cmd    Search for the executable 'cmd' on LOLBAS.
    gibme -rs bash  Generate a reverse shell for bash.
    gibme -bs bash  Generate a bind shell for bash.

    gibme -rs bash -i 10.10.11.12 -p 9000 -os linux -s /bin/bash -en base64 -l nc   Generate a reverse shell for bash with the specified options.

    gibme -n default "Active Directory"     Print the default note for "Active Directory".
    gibme -ls bins  List all the available binaries.
    gibme -ls notes List all the available notes.
place-holder-picture

place-holder-picture

place-holder-picture


## Join the Effort

- Got a fix for something? Awesome! Open a pull request and we'll review it together.
- Spotted a bug? Let me know! Report it and I'll get to squashing.
- Any thoughts or ideas? Open an issue, I'm all ears!

## Upcoming Tasks
- Code refactoring is on the horizon!

## License

This project is licensed under the terms of the MIT License. 

MIT License

Copyright (c) [2023] [foreztgump]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Resources - Credits - Thank you!

- [reverse-shell-generator](https://github.com/0dayCTF/reverse-shell-generator)
- [gtfo](https://github.com/mzfr/gtfo)
- [LOLBAS](https://github.com/LOLBAS-Project/LOLBAS)
- [GTFO](https://github.com/GTFOBins/GTFOBins.github.io)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/)
- [RapidFuzz](https://github.com/maxbachmann/RapidFuzz/)
- [rich](https://github.com/Textualize/rich)
- [httpx](https://github.com/encode/httpx)

