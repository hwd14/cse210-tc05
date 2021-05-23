class Console:
    """This class is in charge of the console. Basically sending and recieving information
    to and from the console. More specifically it gets and sends text and numbers.
    
    Stereotype: 
        Interfacer
        
    Attributes:
        letter: The place where the input for the letter is stored.
        current_guess: Where the user's current guesses is displayed.
        parachute: Where the parachute is printed out line by line.
    """

    def __init__(self):
        """This is the class constructor.
        Args:
            self (console): An instance of Console. 
        """
        self.letter = ''
        
    def get_letter(self):
        """Gets letter from the player.
        Args:
            self (console): An instance of Console. 
        Returns:
            Char: The letter from the user.
        """
        self.letter = input("Guess a letter [a-z]: ")
        return self.letter

    def display_guess(self, current_guess):
        """Displays the current correct guesses from the user
        Args:
            self (console): An instance of Console. 
            current_guess (string): The current guess's made by user.
        """
        for i in range(0, len(current_guess), 1):
            print(f'{current_guess[i]} ', end = '')


    def display_parachute(self, parachute):
        """Displays the current correct guesses from the user
        Args:
            self (console): An instance of Console. 
            parachute (array): The current parachute as it now stands.
        """
        print()
        print()
        for i in range (0, len(parachute), 1):
            print(parachute[i])
        print()
        print('^^^^^^^')
