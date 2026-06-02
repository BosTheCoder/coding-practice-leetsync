class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target_word = "balloon"
        target_counter = Counter(target_word)

        curr_word = text
        curr_counter = Counter(curr_word)

        num_instances = 0
        while True:
            for target_char, target_char_appearances in target_counter.items():
                if target_char not in curr_counter:
                    return num_instances
                
                curr_char_appearances = curr_counter.get(target_char)
                curr_char_appearances -= target_char_appearances

                if curr_char_appearances <0:
                    return num_instances
                
                curr_counter[target_char] = curr_char_appearances
            num_instances += 1
        
        return num_instances