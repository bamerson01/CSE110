intro = "Backpacking deep in the mountains you realize your surroundings do not reflect the location you should be at on the map. You're lost and it’s getting late. If you can get higher you can get a better view of the surrounding mountains and better determine your location on the map. It will take you another 3 hours to get to the peak of the closest mountain so it may be dangerous. You have a GPS beacon but hesitate to activate it. Activating it will seem like you failed on your outdoor adventure. Do you attempt to SUMMIT the mountain? Set CAMP up and try in the morning? Or activate your GPS beacon to be rescued?"

gps = "You activate your GPS. Everyone hears your story and wonders why you didn't try a little harder."

summit = "After a very strenuous climb, you summit just before dark. You can make out silhouettes of the mountains well enough to determine your location and realize you went up the wrong valley. No problem, you just need to backtrack a few miles to get to the right spot. You see just below the peak a good area that should block the wind gusts to set-up a camp for the night. You’re not sure though as the wind might pick up in the middle of the night but hiking back down in the dark might be a risk too. Do you set up your TENT on top of the mountain or HIKE back down?"

tent = "Hiking back down seemed like more of a risk so you decide to set up your camp. However, the wind is gusting at gail force speed. Your tent collapses and you have no choice but to activate your GPS signal. You tell everyone at home about your adventure and they are glad you made the choice to be rescued."

hike = "You hike back down the mountain. It is dark and you are having trouble with your footing. You slip on loose rocks and fall to your death."

camp = "You recall in your wilderness training that when lost, it’s best not to wander off, especially when it gets dark. You finish setting up camp and finally fall asleep. While sleeping you are awoken by the sound of heavy footsteps outside your tent. Nervous by how heavy the steps sound, you debate in your head, should you get out and LOOK to see what it is and scare it off or IGNORE it in hopes that it goes away?"

look = "You get out and look and find yourself confronted with an extremely large grizzly bear that is startled. It immediately begins to maul you and you die."

ignore = "You remain in your tent, you can hear the animal breathing heavily and sniffing your tent. You remain silent and eventually the beast leaves. Worried that the beast comes back and possibly attacks you, you activate the GPS beacon and are rescued. You tell everyone about the beast and they are glad you did not stay through the night."

first_decision = input(f'{intro}\nType your decsion SUMMIT, CAMP, GPS: ')


if first_decision.lower() == 'summit':
    second_decision = input(f'\n{summit}\nType your decsion TENT, HIKE: ')
    if second_decision.lower() == 'tent':
        print(tent)
    elif second_decision.lower() == 'hike':
        print(hike)
    else:
        print(f'\nIncorrect Input')
elif first_decision.lower() == 'camp':
    second_decision = input(f'\n{camp}\nType your decsion LOOK, IGNORE: ')
    if second_decision.lower() == 'look':
        print(look)
    elif second_decision.lower() == 'ignore':
        print(ignore)
    else:
        print(f'\nIncorrect Input')
elif first_decision.lower() == 'gps':
    print(f'\n{gps}\nGAME OVER')
else:
    print(f'\nIncorrect Input')
