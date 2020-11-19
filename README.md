# vtt2txt: a simply utility for converting vtt captionss into MaxQDA compatible txt files with timestamps

installing it: `pip install vtt2txt`

```
# parsed contains a dictionary of spoken 'turns' and speakers is a list of speakers
parsed, speakers = vtt2txt.parse_vtt(path_object)

# this gets the text representation with correct timestamps (a list of strings)
# any speaker name that doesn't equal "Interviewer Name" will be replaced with "Anonymous Participant Name"
# (this anonymizes the transcripts)
txt = vtt2txt.get_text_representation(parsed, "Interviewer Name", "Anonymous Participant Name")

# write to a txt file
with open("output.txt", 'w', encoding='utf-8') as outfile:
    outfile.writelines(txt)


```

`wesanderson.color_palettes` has the color palettes as a dictionary by film title. Some of the films have more than one title.

## Color palettes

![wesanderson color palettes](wes_anderson_color_palettes.png)