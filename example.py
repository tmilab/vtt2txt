from pathlib import Path

import vtt2txt

# simple test
file = Path('.') / '..' / 'testV2t' / 'zoom_transcript_7.vtt'

converted = vtt2txt.convert_to_txt(file)

with open('participant_7.txt', 'w', encoding='utf-8') as outfile:
    outfile.writelines(converted)


# replace participant name with a code
# anyone who is not "Interviewer Name" will be replaced with "Participant Code"
file = Path('.') / '..' / 'testV2t' / 'zoom_transcript_7.vtt'

converted = vtt2txt.convert_to_txt(file, 'Interviewer Name', 'Participant Code')

with open('participant_7-Anonymized.txt', 'w', encoding='utf-8') as outfile:
    outfile.writelines(converted)


# Convert an entire directory of .vtt files with the following naming convention
# zoom_transcript_1.vtt
# zoom_transcript_2.vtt
# ...
# ...

root_directory = Path(".")
for path_object in root_directory.glob('**/*'):
    if path_object.is_file() and path_object.suffix == '.vtt':
        contents = path_object.stem.split('_')
        number = contents[-1]
        converted = vtt2txt.convert_to_txt(path_object, 'Interviewer Name', 'Participant Code')
        outfile_path = path_object.stem + '_parsed.txt'
        with open(outfile_path, 'w', encoding='utf-8') as outfile:
            outfile.writelines(converted)
