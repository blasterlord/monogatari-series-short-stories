from pathlib import Path
import subprocess
import shutil
import json

VERSION = "0.1"

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
    
    # Generate Pandoc's args
    args = [
        "pandoc",
        "--file-scope", # Makes all short stories into independent HTML files.
        "--resource-path=assets", # Resource folder to locate images
        "--metadata-file=metadata.json",
        "-o", f"book/Monogatari_Series_Short_Stories_V_{VERSION.replace('.', '_')}.epub",
    ] + markdown_files
    subprocess.run(args)