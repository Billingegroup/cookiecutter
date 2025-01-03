import subprocess


def run_cookiecutter():
    try:
        # Run cookiecutter with the Billingegroup template
        subprocess.run(["cookiecutter", "https://github.com/Billingegroup/cookiecutter"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run cookiecutter: {e}")
