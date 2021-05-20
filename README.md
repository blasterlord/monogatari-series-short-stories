# Monogatari Series Short Stories

## Build Instructions
1. Clone the repo `git clone https://github.com/blasterlord/monogatari-series-short-stories.git`
2. [Install Pandoc](https://pandoc.org)
3. [Install Python](https://www.python.org)
4. Run `python build.py`
5. The generated EPUB will be located in the newly created `book` folder

## How to Add a New Short Story
1. Put the Markdown file in the `src` folder.
2. The filename should be of the form `(serial_number)_(name).md`. The name should be all lowercase with words separated with underscores. For example, `01_hitagi_buffet.md`.
3. Any images or other assets like fonts go in the `assets` folder. The naming convention for these files is similar to the Markdown files. For example, `01_hitagi_buffet.jpg`.
4. Run `python build.py` to regenerate the EPUB with the new content.

-----------------------------

![](assets/00_01_cover.jpg)
