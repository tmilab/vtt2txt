# takes in a string of a timestamp and returns a string of a formatted timestamp
# right now, this is just for ensuring the floating point on the second is correct
def time_parser(time, s_precision=1):
    time_split = time.split(':')
    seconds = round(float(time_split[-1]), s_precision)
    if seconds < 10:
        seconds = '0' + str(seconds)
    else:
        seconds = str(seconds)
    return time_split[0] + ':' + time_split[1] + ':' + seconds


# returns a list of dicts with parsed data
# give it the pathlib file object (or any string path)
# s_precision is the number of decimals after the point on the timestamp (MaxQDA only allows 1)
def parse_vtt(p, s_precision=1):
    with open(p, 'r', encoding='utf-8') as infile:
        contents = infile.read()

    with open(p, 'r', encoding='utf8') as infile:
        lines = infile.readlines()

    # data will be a list of "turns" taken
    # each entry will be a dict with "count" "start_time" "end_time" "speaker" and "content"
    data = []

    # include a list of unique speakers, this can be used to anonymize the transcripts
    speakers = []

    curr_line = {}
    curr_stage = 'empty'
    last_speaker = 'Unknown'
    for line in lines:
        # parse to see where we're at
        if line == 'WEBVTT' or line.strip() == '':
            next
        if line.strip().isdigit() and curr_stage == 'empty':
            # start of a new line, so clear out the old
            curr_line = {}
            curr_line['index'] = int(line)

            # set the next stage to timestamps
            curr_stage = 'time'
        elif curr_stage == 'time':
            # parse the time stamps
            times = line.split(' ')
            curr_line['start_time'] = time_parser(times[0][:-2], s_precision)
            curr_line['end_time'] = time_parser(times[2].strip()[:-2], s_precision)

            # set the next stage to speaker
            curr_stage = 'speaker'

        elif curr_stage == 'speaker':
            # parse the speaker and what they said
            if (':' in line):
                # there is a new speaker. Capture it
                splits = line.split(':')
                curr_line['speaker'] = splits[0]
                if (curr_line['speaker'] not in speakers):
                    speakers.append(curr_line['speaker'])
                last_speaker = curr_line['speaker']
                curr_line['content'] = splits[1].strip()
            else:
                # no speaker, just grab the last speaker
                curr_line['speaker'] = last_speaker
                curr_line['content'] = line.strip()

            # set stage back to empty and save the result into the list
            curr_stage = 'empty'
            data.append(curr_line)
    return data, speakers


def get_txt_representation(lines, interviewer_name=None, participant_code=None):
    # loop through and print out content into a text file.
    # will be like:
    # Name: #start_time# What this person said #end_time#
    output = []
    for line in lines:
        if interviewer_name and participant_code and line['speaker'] != interviewer_name:
            curr_speaker = participant_code
        else:
            curr_speaker = line['speaker']
        output.append(curr_speaker + ': ' + line['start_time'] + ' ' + line['content'] + ' ' \
                      + line['start_time'] + '\n')

    return output


def convert_to_txt(p, interviewer_name=None, participant_code=None, s_precision=1):
    lines, speakers = parse_vtt(p, s_precision=s_precision)
    contents = get_txt_representation(lines, interviewer_name, participant_code)
    return contents


# outputs a text file with timestamps for importing into MaxQDA
# replaces anyone who isn't the interviewer_name with participant_code
def write_text_file(lines, output_file, interviewer_name, participant_code):
    contents = get_txt_representation(lines, interviewer_name, participant_code)
    # write to file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(contents)






