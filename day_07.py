from aoc_helper import fetch, run

def custom_sort_1(e):
    return [['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'].index(c) for c in e]

def custom_sort_2(e):
    return [['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'].index(c) for c in e]

class Solution:
    def __init__(self):
        self.raw_data = fetch("07", "2023").splitlines()
        self.length = len(self.raw_data)
        self.data = self.parse_data()

    def parse_data(self):
        data = {}
        for line in self.raw_data:
            card, bid = line.split()
            data[card] = int(bid)
            
        return data

    def characterCount(self, word):
        charCount = {}
        for char in word:
            charCount[char] = 1 if char not in charCount else charCount[char] + 1
        return charCount
    
    def cardClassify(self, word, part=1):
        charCount = self.characterCount(word)
        keys, values = list(charCount.keys()), list(charCount.values())
        if part == 2:
            if "J" in charCount and charCount["J"] != 5:
                charCount[keys[values.index(max(values))]] += charCount["J"]
                del charCount["J"]

        if len(charCount) == 1:
            cardType = 7
        elif len(charCount) == 2 and 4 in values:
            cardType = 6
        elif len(charCount) == 2: 
            cardType = 5
        elif len(charCount) == 3 and 3 in values:
            cardType = 4
        elif len(charCount) == 3:
            cardType = 3
        elif len(charCount) == 4:
            cardType = 2
        elif len(charCount) == 5:
            cardType = 1

        return cardType
    
    def customSort(self, cards, part=1):
        keys, values = list(cards.keys()), list(cards.values())
        if part == 1:
            for i in range(7):
                cards[keys[i]] = sorted(values[i], key=custom_sort_1)
        else:
            for i in range(7):
                cards[keys[i]] = sorted(values[i], key=custom_sort_2)

        return cards

    def calculate_p1(self):
        p1 = 0

        cards = {7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1:[]}
        for card in self.data.keys():            
            cards[self.cardClassify(card)].append(card)

        cards = self.customSort(cards)

        rank = self.length
        for values in cards.values(): 
            for card in values:
                p1 += self.data[card] * rank
                rank -= 1
        return p1

    def calculate_p2(self):
        p2 = 0

        cards = {7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1:[]}
        for card in self.data.keys():            
            cards[self.cardClassify(card, 2)].append(card)

        cards = self.customSort(cards, 2)
        
        rank = self.length
        for values in cards.values(): 
            for card in values:
                p2 += self.data[card] * rank
                rank -= 1
        return p2

if __name__ == "__main__":
    run(Solution)