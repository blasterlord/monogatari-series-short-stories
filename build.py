from pathlib import Path
import subprocess
import shutil
import json

if __name__ == "__main__":

    # Check if Pandoc exists
    if shutil.which("pandoc") is None:
        raise FileNotFoundError("Can't find Pandoc. Please install it from https://pandoc.org/")
        
    # Get all the Markdown files in alphabetical order
    markdown_files = sorted(map(str, Path("src").glob("*.md")))
    
    # Get the version of the book
    with open("metadata.json") as f:
        metadata = json.load(f)
    VERSION = metadata["version"]
    
    # Create output directory if it doesn't already exist
    Path("book").mkdir(exist_ok=True)
    
    # Generate Pandoc's args
    args = [
        "pandoc",
        "--file-scope", # Makes all short stories into independent HTML files.
        "--resource-path=assets", # Resource folder to locate images
        "--epub-cover-image=assets/00_01_cover.jpg",
        "--metadata-file=metadata.json",
        "-o", f"book/Monogatari_Series_Short_Stories_V_{VERSION.replace('.', '_')}.epub",
    ] + markdown_files
    
    subprocess.run(args)