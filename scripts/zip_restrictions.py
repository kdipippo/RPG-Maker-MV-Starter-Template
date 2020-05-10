import os

rootdir = 'src'

checks_text = [
    "The ZIP file should not contain more than 500 individual files after extraction.",
    "The maximum length of a file name including path should not be greater than 240 characters long.",
    "The size of all the extracted content should not be greater than 1GB.",
    "The size any single extracted file should not be greater than 100MB."
]
checks = [True, True, True, True]

total_file_size = 0
total_count = 0
ONE_HUNDRED_MEGABYTES = 104857600
ONE_GIGABYTE = 1073741824

for subdir, dirs, files in os.walk(rootdir):
    if subdir == 'src/save':
        continue
    for file in files:
        if file == 'Game.rpgproject':
            continue
        if len(file) > 240:
            print(f"[!] Filename for {file} is {len(file-240)} characters too long!")
            checks[1] = False
        total_count = total_count + 1
        file_size = os.path.getsize(os.path.join(subdir, file))
        total_file_size += file_size
        if file_size >= ONE_HUNDRED_MEGABYTES:
            print(f"[!] {file} is {file_size} bytes!")
            checks[3] = False

if total_count > 500:
    checks[0] = False
    print(f"[!] {total_count} files total!")
if total_file_size > ONE_GIGABYTE:
    checks[2] = False
    print(f"[!] Total file size is {total_file_size} bytes!")

print("-"*20)
for i in range(len(checks)):
    if checks[i]:
        print(f"✅ {checks_text[i]}")
    else:
        print(f"❌ {checks_text[i]}")
