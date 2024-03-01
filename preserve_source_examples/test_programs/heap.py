from game_consts import * 

class Heap(object):
    
    def __init__(self, first_card: int, name: str) -> None:
        self._name = name 
        self._first_card = first_card
        self._hint = 0.0 
        if first_card == 100:
            self.direction = -1
            self.can_add_card = self.can_add_card_down
        elif first_card == 1: 
            self.direction = 1
            self.can_add_card = self.can_add_card_up
        else: 
            raise Exception("Invalid top card")
        
        self._top_card = first_card

    def set_hint(self, cost) -> None: 
        self._hint = cost 

    def reset_hint(self) -> None: 
        self._hint = 0.0 

    def get_hint(self) -> float: 
        return self._hint

    def best_card(self, cards: set[int]) -> tuple[int, bool]:
        """ 
        Returns a tuple of the best card (int) and whether it's a backward step. 
        """
        if self.direction == 1: 
            best_card = min(cards) 
            is_back = best_card < self._top_card
        else: 
            best_card = max(cards) 
            is_back = best_card > self._top_card
        return best_card, is_back

    def add_card(self, new_card: int) -> None: 
        # top_card = self.top_card
        # if new_card == top_card - DESIRED_DIFF * self.direction:
        #     logger.info("jump by 10") 
        # else: 
        #     assert new_card * self.direction > top_card * self.direction 
        self._top_card = new_card

    def get_top_card(self) -> int:
        return self._top_card 

    def add_cards(self, cards) -> None: 
        for card in cards: 
            self.add_card(card)

    def can_add_card_up(self, new_card: int) -> bool: 
        top_card = self._top_card
        return new_card  > top_card or new_card == top_card - DESIRED_DIFF

    def can_add_card_down(self, new_card: int) -> bool: 
        top_card = self._top_card
        return  new_card  < top_card or new_card == top_card + DESIRED_DIFF

    def __repr__(self) -> str:
        return f"{self._name}: {self.get_top_card()}"

    def copy(self) -> 'Heap':
        new_heap = Heap(self._first_card, self._name + "*")
        new_heap._top_card = self._top_card 
        return new_heap
