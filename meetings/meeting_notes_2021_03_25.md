What things go over the command station serial port?
- Call / response, one at a time, over the serial port from the brain
- Block occupancy detection - one command gives a bunch of states back as a bitfield (6 AIUs with 14 bits per)
- Switch position (read) - One giant chunk of memory, one bit per switch, and a poll gives several back
- Switch position (write) - can/would update switches by sending a packet with the switch address (or something)
- Control signal lights by sending DCC control commands over the computer interface, which the command station will proxy and relay over DCC

Signal lights can be run off of (existing) decoder boards attached directly to the DCC bus, or can be wired straight to the new boards (which will need LED output anyway, because theyre backing the new physical panels)


Before, the serial port was being checked once per sweep of cab addresses, but that rate might be faster now.


The physical panels:
Have buttons and lights, wired though the new GPIO type pins, all digital.


Breakaoutable tasks:

Phase 1
- Interfacing over the computer interface to the command station
  - Read block status
  - Read switch status (the switches, for testing, would be set by hand with a throttle on CAB)
  - Portable hardware kit is located at Boardman / there is also the one at the club, but please use the devkit.

Phase 2
- Leaf setup / communication
  - Setting LED state / reading button state / general "gettin the pi 0 up and running"
  - Commication protocol between leaves and brain
    - Needs some fleshing out / definition
    - Will be RS485 presumably, at least baseline
    - How much smarts do we want to put on the leaves and why is the answer to that very little... **Big Dumb IO**
    - Consider more complex light states than on/off (blink, multi-lead-LEDs)
    - The state the leaves represent is: Display state of each LED
    - Buttons fire events? back to the brain - this is much lower priority / stretch goal

Phase 3
- Initial implementation of logic system.
  - Nothing too crazy
  - some form of reactive control that can set output based on ... conditions.
  - Use block presence detection perhaps as the input?
    - Blocks aren't 1:1 with occupancy detection sections


Future:
Some form of API for the PC and whatnot


Takeaway tasks:
- Charles to locate docs on command station interface ("NCE Serial Interface manual")
- Initial protocol layout on new bus between leaves and brain
  - Keep it simple, etc
  - Expect it to be disposable MVP
- Approach to implementation of logic system
- Write some use cases, especially around the logic
- Set up a Trello
- Upload these notes to github

Next time:
- Go through use cases
- Architect how the brain represents state
- Scope phase 1, give a definition of done











Misc requirements / thoughts / misc:

The same state can be represented multiple places, so do we keep track of this by setting multiple outputs independently or do 

Do we set individual bits or full status at a time?  We could prob get away with just big sweeping set everything updates, but this is dependent on data rates.

Timers - some form of intervaled / scheduled events need to be able to occur in the brain part, like crossing gates being on for a period of time (if the block leading up to crossing block is active, turn on crossing (lights / gates, etc), but if the crossing itself has no train after a bit, release the crossing and raise gates).  I'm calling this a later version feature.


Some sort of rule engine, DSL, etc - if we use an off the shelf language, be very clear about the API that the client code interacts with






