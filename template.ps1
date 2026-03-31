mkdir src
mkdir research

New-Item src/__init__.py -ItemType File
New-Item src/helper.py -ItemType File
New-Item src/prompt.py -ItemType File
New-Item .env -ItemType File
New-Item setup.py -ItemType File
New-Item app.py -ItemType File
New-Item research/trials.ipynb -ItemType File
New-Item requirements.txt -ItemType File

echo "directory and files created successfully"


