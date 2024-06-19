from pathlib import Path
import shutil

# All cookie-cutter hooks run on project root, but good to enforce
ROOT = Path.cwd()

# Remove src/diffpy directory for non-diffpy projects
def remove_diffpy(ROOT):
    src_dir = ROOT / "src"
    diffpy_dir = src_dir / "diffpy"

    for child in diffpy_dir.iterdir():
        # Remove all files within the diffpy directory (__init__.py)
        if child.is_file():
            child.unlink()

        # Move all directories ({{ cookiecutter.package_dir_name }})
        elif child.is_dir():
            shutil.move(child, src_dir)

    # Remove diffpy directory
    diffpy_dir.rmdir()


if "{{ cookiecutter.diffpy_project }}" != "y":
    remove_diffpy(ROOT)
