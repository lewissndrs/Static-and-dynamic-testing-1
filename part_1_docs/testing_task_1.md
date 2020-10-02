### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  # needs double "=" to act as comparitor. Else needs colon after it.
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
  # Should be "def" not "dif". Card1 needs a comma. First return should be card1, not card. Block under first line needs to be indented.
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# total variable needs to be initialized equal to zero. return statement should be outside of for loop. Whole thing is indented outside of class. total needs to be converted to a string to concatenate it to the string.
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
