# vtt2txt: convert Zoom transcripts for MaxQDA

A simply utility for converting vtt captions into MaxQDA compatible text files with timestamps.

Install via:  `pip install vtt2txt`


#### Usage:

Convert a .vtt file to a .txt file with timestamps:
```
import vtt2txt

lines = vtt2txt.convert_to_txt('zoom_transcript.vtt')

# write to a txt file
with open("output.txt", 'w', encoding='utf-8') as outfile:
    outfile.writelines(lines)

```

Anonymize the transcript with the following optional parameters
Any speaker name not equal to 'Interviewer Name' will be replaced with 'Participant Code' 
```
import vtt2txt

lines = vtt2txt.convert_to_txt('zoom_transcript.vtt', 'Interviewer Name', 'Participant Code')

# write to a txt file
with open("output.txt", 'w', encoding='utf-8') as outfile:
    outfile.writelines(lines)

```

Convert an entire directory of transcripts
The file naming convention in this example is:

zoom_transcript_1.vtt  
zoom_transcript_2.vtt  
...  
...

```
import vtt2txt
from pathlib import Path

root_directory = Path(".")
for path_object in root_directory.glob('**/*'):
    if path_object.is_file() and path_object.suffix == '.vtt':
        contents = path_object.stem.split('_')
        number = contents[-1]
        converted = vtt2txt.convert_to_txt(path_object, 'Interviewer Name', 'Participant Code')
        outfile_path = path_object.stem + '_parsed.txt'
        with open(outfile_path, 'w', encoding='utf-8') as outfile:
            outfile.writelines(converted)
```