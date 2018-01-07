from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

milk = Thing('Get milk')
obstacles = Thing('Remove the obstacles')
work = Thing('Stand up')
eat = Thing('Eat lunch')

work.complete()
eat.complete()

fleet.add(milk)
fleet.add(obstacles)
fleet.add(work)
fleet.add(eat)


print(fleet)
