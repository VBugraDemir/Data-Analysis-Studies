#  The best use case for lambda functions, however,
#  are for when you want these simple functionalities to be anonymously embedded within larger expressions

spells = ["protego", "accio", "expecto patronum", "legilimens"]

shout_spells = map(lambda item: item + "!!!", spells)
shout_spells_list = list(shout_spells)
print(shout_spells_list)
