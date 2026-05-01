def compute_polkadot_score(ascii_art):
    lines = ascii_art.split('\n')
    # I am here trying to find the position of the lips, which are represented by '()' in the ASCII art.
    lips_start_x = -1
    lips_end_x = -1

    for line in lines:
        if '(' in line and ')' in line:
            start = line.find('()')
            if start != -1 and start > 20:
                lips_start_x = start
                lips_end_x = start + 1
                break

    # Here I am counting the number of '0' characters that are inside the lips and outside the lips, 
    # and also counting the number of '.' characters which represent the pupils.            
    pupil_chars_count = 0
    for line in lines:
        if '.' in line or ' ; ' in line:
            pupil_chars_count += line.count('.')

    dots_inside = 0
    dots_outside = 0

    for line in lines:
        for x, char in enumerate(line):
            if char == '0':
                if lips_start_x <= x <= lips_end_x:
                    dots_inside += 1
                else:
                    dots_outside += 1
    
    score = dots_outside + (dots_inside * pupil_chars_count)
    return score


# Number of polkadots in the ASCII art is 51 
# akaankshpemmaraju - akaankshp10@gmail.com