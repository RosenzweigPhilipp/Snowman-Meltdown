"""ASCII art stages for the Snowman Meltdown game.

This module contains the visual representations of the snowman at different
stages of melting, from a perfect snowman to complete meltdown.
"""

from typing import List

# Snowman ASCII Art stages - More detailed melting progression
STAGES: List[str] = [
    # Stage 0: Perfect snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
    [___]
     """,
    # Stage 1: Bottom base starts melting
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
    ~~___~~
     """,
    # Stage 2: Bottom section melting more
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ~~:~~
     """,
    # Stage 3: Middle section starts melting
    """
      ___  
     /___\\ 
     (o o) 
     ~~:~~
     """,
    # Stage 4: Only head with hat remains
    """
      ___  
     /___\\ 
     (o o) 
     """,
    # Stage 5: Head melting, hat falls
    """
      ___  
     ~~___~~ 
     (. .) 
     """,
    # Stage 6: Complete meltdown - only puddle remains
    """
      ___  
     /___\\ 
   ~~~~~~~~~~~
     """
]