from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Joffrey Baratheon, the weird King.
    Inherits from both Baratheon and Lannister using C3 Linearization.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the King class.
        Starts as a Baratheon with default Baratheon features.
        """
        # Follows C3: Baratheon.__init__()
        super().__init__(first_name, is_alive)
        # In case Lannister defines its own attributes, super() handles MRO

    def get_eyes(self) -> str:
        """
        Getter for eye color.

        Returns:
            str: eye color of the king
        """
        return self.eyes

    def set_eyes(self, color: str) -> None:
        """
        Setter for eye color.

        Args:
            color (str): new eye color
        """
        self.eyes = color

    def get_hairs(self) -> str:
        """
        Getter for hair color.

        Returns:
            str: hair color of the king
        """
        return self.hairs

    def set_hairs(self, color: str) -> None:
        """
        Setter for hair color.

        Args:
            color (str): new hair color
        """
        self.hairs = color
