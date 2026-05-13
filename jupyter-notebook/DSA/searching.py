class CardSearch:
    def __init__(self, cards):
        self.cards = cards

    def linear_search(self, element):
        for i in range(len(self.cards)):
            if self.cards[i] == element:
                return i
        return -1

    def binary_search(self, element):
        sorted_cards = sorted(self.cards)
        print("Sorted List:", sorted_cards)
        
        low = 0
        high = len(sorted_cards) - 1

        while low <= high:
            mid = (low + high) // 2
            if sorted_cards[mid] == element:
                return mid
            elif sorted_cards[mid] < element:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def search(self):
        print("Shuffled List:", self.cards)
        try:
            element = int(input("Enter a number from card to find position: "))
            method = input("Which search do you want to perform? (linear/binary): ").strip().lower()

            if method == "linear":
                pos = self.linear_search(element)
                if pos != -1:
                    print(f"Number {element} found at position {pos} (original list).")
                else:
                    print(f"Oops! {element} not found in the list.")
            elif method == "binary":
                pos = self.binary_search(element)
                if pos != -1:
                    print(f"Number {element} found at position {pos} (in sorted list).")
                else:
                    print(f"Oops! {element} not found in the list.")
            else:
                print("Invalid search method. Please choose 'linear' or 'binary'.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Example usage
cards = [7, 13, 1, 4, 10, 0, 11, 3]  # shuffled list
cs = CardSearch(cards)
cs.search()
