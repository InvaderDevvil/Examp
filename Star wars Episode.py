import winsound
import threading
import time
star_wars_movies = [
    "Star Wars: Episode I The Phantom Menace",
    "Star Wars: Episode II Attack of the Clones",
    "Star Wars: Episode III Revenge of the Sith",
    "Star Wars: Episode IV A New Hope",
    "Star Wars: Episode V The Empire Strikes Back",
    "Star Wars: Episode VI Return of the Jedi",
    "Star Wars: Episode VII The Force Awakens",
    "Star Wars: Episode VIII The Last Jedi",
    "Star Wars: Episode IX The Rise of Skywalker",
    "Rogue One",
    "Solo"]

def play_sound():
    winsound.PlaySound("imperial_march.wav", winsound.SND_FILENAME)

import sys

def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

thread = threading.Thread(target=play_sound)
print('''
      
             Welcome Jedi, to the Star Wars Episode Selector!
You will find the introduction to each one of the Star Wars favorite movies below.
                    May the force be with you!
      
      
      ''')
print("The options are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Rogue One', 'Solo'")
star_wars_movie = input('Select the Star Wars episode (1-9, Rogue One, Solo): ')

thread.start()

if star_wars_movie == "1":
    print(''' 
          
    Episode I
THE PHANTOM MENACE
          
Turmoil has engulfed the
Galactic Republic. The taxation
of trade routes to outlying star
systems is in dispute.

Hoping to resolve the matter
with a blockade of deadly
battleships, the greedy Trade
Federation has stopped all
shipping to the small planet
of Naboo.

While the Congress of the
Republic endlessly debates
this alarming chain of events,
the Supreme Chancellor has
secretly dispatched two Jedi
Knights, the guardians of
peace and justice in the
galaxy, to settle the conflict....''')
elif star_wars_movie == "2":

    print('''

    Episode II
ATTACK OF THE CLONES

There is unrest in the Galactic
Senate. Several thousand solar
systems have declared their
intentions to leave the Republic.

This separatist movement,
under the leadership of the
mysterious Count Dooku, has
made it difficult for the limited
number of Jedi Knights to
maintain peace and order in
the galaxy.

Senator Amidala, the former
Queen of Naboo, is returning
to the Galactic Senate to vote
on the critical issue of creating
an ARMY OF THE REPUBLIC
to assist the overwhelmed
Jedi...."''')
elif star_wars_movie == "3":
    print(''' 
    Episode III
REVENGE OF THE SITH
          

War! The Republic is crumbling
under attacks by the ruthless
Sith Lord, Count Dooku.
There are heroes on both sides.
Evil is everywhere.

In a stunning move, the
fiendish droid leader, General
Grievous, has swept into the
Republic capital and kidnapped
Chancellor Palpatine, leader of
the Galactic Senate.

As the Separatist Droid Army
attempts to flee the besieged
capital with their valuable
hostage, two Jedi Knights lead a
desperate mission to rescue the
captive Chancellor.... ''')
elif star_wars_movie == "4":
    print('''
It is a period of civil war.
Rebel spaceships, striking
from a hidden base, have won
their first victory against
the evil Galactic Empire.

During the battle, Rebel
spies managed to steal secret
plans to the Empire's
ultimate weapon, the DEATH
STAR, an armored space
station with enough power to
destroy an entire planet.

Pursued by the Empire's
sinister agents, Princess
Leia races home aboard her
starship, custodian of the
stolen plans that can save
her people and restore
freedom to the galaxy....''')
elif star_wars_movie == "5":
    print(''' 
     Episode V
THE EMPIRE STRIKES BACK
          
It is a dark time for the
Rebellion. Although the Death
Star has been destroyed,
Imperial troops have driven the
Rebel forces from their hidden
base and pursued them across
the galaxy.

Evading the dreaded Imperial
Starfleet, a group of freedom
fighters led by Luke Skywalker
has established a new secret
base on the remote ice world
of Hoth.

The evil lord Darth Vader,
obsessed with finding young
Skywalker, has dispatched
thousands of remote probes into
the far reaches of space....''')
elif star_wars_movie == "6":
    print(''''
     Episode VI
RETURN OF THE JEDI
          
Luke Skywalker has returned to
his home planet of Tatooine in
an attempt to rescue his
friend Han Solo from the
clutches of the vile gangster
Jabba the Hutt.

Little does Luke know that the
GALACTIC EMPIRE has secretly
begun construction on a new
armored space station even
more powerful than the first
dreaded Death Star.

When completed, this ultimate
weapon will spell certain doom
for the small band of rebels
struggling to restore freedom
to the galaxy... ''')
elif star_wars_movie == "7":
    print('''
Episode VII
THE FORCE AWAKENS
Luke Skywalker has vanished.
In his absence, the sinister
FIRST ORDER has risen from
the ashes of the Empire
and will not rest until
Skywalker, the last Jedi,
has been destroyed.

With the support of the
REPUBLIC, General Leia Organa
leads a brave RESISTANCE.
She is desperate to find her
brother Luke and gain his
help in restoring peace
and justice to the galaxy.

Leia has sent her most daring
pilot on a secret mission
to Jakku, where an old ally
has discovered a clue to
Luke's whereabouts.... ''')
elif star_wars_movie == "8":
    print('''Episode VIII
THE LAST JEDI
The FIRST ORDER reigns.
Having decimated the peaceful
Republic, Supreme Leader Snoke
now deploys his merciless
legions to seize military
control of the galaxy.

Only General Leia Organa's
band of RESISTANCE fighters
stand against the rising
tyranny, certain that Jedi
Master Luke Skywalker will
return and restore a spark of
hope to the fight.

But the Resistance has been
exposed. As the First Order
speeds toward the rebel base,
the brave heroes mount a
desperate escape....''')
elif star_wars_movie == "9":
    print(''' Episode IX
THE RISE OF SKYWALKER
The dead speak! The galaxy has
heard a mysterious broadcast,
a threat of REVENGE in the
sinister voice of the late
EMPEROR PALPATINE.

GENERAL LEIA ORGANA
dispatches secret agents to
gather intelligence, while REY,
the last hope of the Jedi, trains
for battle against the diabolical
FIRST ORDER.

Meanwhile, Supreme Leader
KYLO REN rages in search
of the phantom Emperor,
determined to destroy any
threat to his power....''')
elif star_wars_movie.lower() == "rogue one":
    print('''
    Rogue One: A Star Wars Story
          
A long time ago in a galaxy far, far away....

It is a period of civil war. Rebel spaceships, striking from a hidden base
have won their first victory against the evil Galactic Empire.
During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon,
the DEATH STAR,
an armored space station with enough power to destroy an entire planet. 
Pursued by the Empire's sinister agents, Princess Leia races home aboard her starship
custodian of the stolen plans that can save her people and restore freedom to the galaxy....''')

    print("Invalid selection. Please choose a valid episode number (1-9) or title (Rogue One, Solo).")
    
elif star_wars_movie.lower() == "solo":
    print('''
    Solo: A Star Wars Story
          
A long time ago in a galaxy far, far away....

Board the Millennium Falcon and journey to a galaxy far, far away in Solo: A Star Wars Story, 
an all-new adventure with the most beloved scoundrel in the galaxy.
Through a series of daring escapades deep within a dark and dangerous criminal underworld
Han Solo meets his mighty future copilot Chewbacca and encounters the notorious gambler Lando Calrissian
in a journey that will set the course of one of the Star Wars saga’s most unlikely heroes.''')
else:
    print("Episode not found please use a valid episode number (1-9) or title (Rogue One, Solo).")
print("Returning to the menu...")
exec(open(__file__).read())
