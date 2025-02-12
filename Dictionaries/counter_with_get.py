names = ['Drax', 'Black Panther', 'Captain Marvel', 'Magneto', 'Venom', 'Thanos', 'Star-Lord', 'Scarlet Witch', 'Venom', 'Hawkeye', 'Mystique', 'Shang-Chi', 'Vision', 'Thor', 'Professor X', 'Shang-Chi', 'Captain America', 'Jean Grey', 'Ultron', 'Vision', 'Storm', 'Deadpool', 'Gamora', 'Drax', 'Drax', 'Loki', 'Hulk', 'Red Skull', 'Shang-Chi', 'Professor X', 'Magneto', 'Deadpool', 'Ghost Rider', 'Moon Knight', 'Ultron', 'Winter Soldier', 'Black Panther', 'Vision', 'Professor X', 'Captain Marvel', 'Deadpool', 'Winter Soldier', 'Wasp', 'Doctor Strange', 'Deadpool', 'Ant-Man', 'Shang-Chi', 'Cyclops', 'Doctor Doom', 'Ultron', 'Hawkeye', 'Groot', 'Jean Grey', 'Nick Fury', 'Hulk', 'Silver Surfer', 'Thor', 'Doctor Doom', 'Groot', 'Iron Man', 'Groot', 'Gamora', 'Moon Knight', 'Moon Knight', 'Professor X', 'Doctor Doom', 'Captain Marvel', 'Venom', 'Hawkeye', 'Groot', 'Doctor Doom', 'Doctor Doom', 'Shang-Chi', 'Loki', 'Moon Knight', 'Silver Surfer', 'Winter Soldier', 'Storm', 'Black Panther', 'Hawkeye', 'Winter Soldier', 'Professor X', 'Black Panther', 'Red Skull', 'Thor', 'Wolverine', 'Jean Grey', 'Hawkeye', 'Nick Fury', 'Star-Lord', 'Vision', 'Doctor Strange', 'Vision', 'Wasp', 'Storm', 'Iron Man', 'Doctor Strange', 'Captain America', 'Black Panther', 'Hulk']
count = dict()
for name in names:
    # if name not in count:
    #     count[name]=0
    # else:
    #     count[name]+=1
    count[name] = count.get(name,0)+1                 # get()basically makes a key if there's none and stores initial value 0.Basically does all the work of the above if.
print(count)

print(count['Wolverine'])
