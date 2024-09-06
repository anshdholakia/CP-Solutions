class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        cur_words = []
        cur_length = 0
        for word in words:
            if cur_length+len(word)<maxWidth:
                cur_length+=(len(word) if not cur_length else len(word)+1)
                cur_words.append(word)
            else:
                # format the line
                length = sum([len(x) for x in cur_words])
                spaces_needed = maxWidth-length
                if len(cur_words)-1:
                    remainder = spaces_needed%(len(cur_words)-1)
                    floored_spaces = spaces_needed//(len(cur_words)-1)
                else:
                    floored_spaces = spaces_needed
                    remainder = 0
                cur_line = ""
                for w in range(len(cur_words)):
                    cur_line+=cur_words[w]
                    if w!=len(cur_words)-1:
                        cur_line+=" "*(floored_spaces+bool(remainder))
                    remainder=max(0, remainder-1)
                cur_line+=" "*(maxWidth-len(cur_line))
                if cur_line!=" "*maxWidth:
                    output.append(cur_line)
                cur_length=len(word)
                cur_words=[word]
        cur_line = ""
        for w in range(len(cur_words)):
            cur_line+=cur_words[w]
            if w!=len(cur_words)-1:
                cur_line+=" "
        cur_line+=" "*(maxWidth-len(cur_line))
        output.append(cur_line)
        return output
