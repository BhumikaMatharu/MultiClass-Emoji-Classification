#!/usr/local/bin/python3
from PIL import Image, ImageFont, ImageDraw
import emoji
import random
from collections import OrderedDict
from operator import itemgetter
import cv2
from csv import writer
emotions = {1:':grinning_face:',
            2:':loudly_crying_face:',3:':astonished_face:',
            4:':winking_face:',5:':face_with_medical_mask:'}
happy = [':grinning_face:',':grinning_face_with_big_eyes:',':grinning_face_with_smiling_eyes:',
         ':beaming_face_with_smiling_eyes:',':grinning_squinting_face:',':slightly_smiling_face:',
         ':smiling_face_with_smiling_eyes:']
sad = [':worried_face:',':slightly_frowning_face:',':frowning_face:',':disappointed_face:',
       ':weary_face:',':downcast_face_with_sweat:',':loudly_crying_face:']
surprised = [':face_with_open_mouth:',':hushed_face:',':astonished_face:',
             ':frowning_face_with_open_mouth:',':anguished_face:',':fearful_face:']
unamused = [':face_with_steam_from_nose:',':neutral_face:',':expressionless_face:',':unamused_face:',
            ':angry_face:',':grimacing_face:']
f = [25,20,28,30,32]
n = 0
for i in range(1000):
    elem = [0,0,0,0,0]
    lab_loc = {}
    num = random.randint(1,3)
    img = Image.new('RGB', (64, 64), color='white')
    d = ImageDraw.Draw(img)
    loc = [[(0,0),(30,0),(30,30)],[(0,10),(20,30),(40,20)]]
    e = [1, 2, 3, 4, 5]
    binary_emo = []
    for j in range(num):
        val = random.choice(f)
        l = random.randint(0,1)
        #print(val)
        font = ImageFont.truetype("C:/Users/U S Matharu/Downloads/Symbola/Symbola_hint.ttf", val)
        emo_num = random.choice(e)
        e.remove(emo_num)
        elem[emo_num-1] = 1
        emo = str(emoji.emojize(emotions[emo_num]))
        d.text(loc[l][j],emo,(0,0,0), font=font)
        lab_loc[emotions[emo_num][1:-1]] = [loc[l][j],val,emo_num]
        binary_emo.append(emotions[emo_num])
        #print(elem,e)
    name = ''
    for k,v in lab_loc.items():
        name += k+'-'
        name += str(v[0])+'-'
    #print(name[:-1],i)
    img.save('test'+str(i)+'.png','PNG')

    # list_elem = ['test' + str(i) + '.png', labels, elem[0], elem[1], elem[2], elem[3], elem[4]]
    # print(binary_emo)
    coordinates_data = [0,0,0,0,0]
    l = 1
    location_data = [0,0,0,0,0]
    binary = ['01','10','11']
    for k,v in lab_loc.items():
        location_data[v[2]-1] = l
        l += 1
        coordinates_data[v[2]-1] = v[0][0],v[0][1],v[0][0]+v[1],v[0][1]+v[1]
    # print(location_data,coordinates_data)
    labels = []
    for b in binary_emo:
        labels.append(b[1:-1])
    # print(labels)
    with open('locations.csv', 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            list_elem = ['test'+str(i)+'.png',labels,location_data[0],location_data[1],location_data[2],
                         location_data[3],location_data[4]]
            csv_writer.writerow(list_elem)
    with open('coordinates.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        list_elem = ['test' + str(i) + '.png', labels, coordinates_data[0], coordinates_data[1], coordinates_data[2],
                     coordinates_data[3], coordinates_data[4]]
        csv_writer.writerow(list_elem)
    with open('emo_count.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        list_elem = ['test' + str(i) + '.png', len(labels)]
        csv_writer.writerow(list_elem)
    n += 1
    # img.save('test'+str(i)+'-'+name[:-1] + '.png', 'PNG')
