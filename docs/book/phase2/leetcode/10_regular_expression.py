class Solution:
    """

        # if has more than two consecutive chars in p, means a must in s
        # *ab*, .ab*, a. all indicate a must be in s two consecutive chars in p, "." also consider as char
        # otherwise, p should be like z*b*c*d*.*e*,

    """
    def isMatch(self, s: str, p: str) -> bool:
        return self.is_match(s, p)

    def solve_edge_case(self, s,p):
        if len(p)==0:
            return len(s)==0
        if len(p)==1:
            return len(s)==1 and (s==p or p==".")
        if len(p)==2: #
            if p[0]==".":
                if p == ".*":
                    return True
                elif p=="..":
                    return len(s)==2
                else:
                    return len(s)==len(p) and s[1]==p[1]
            elif p[0]=="*":
                raise Exception("There should be a previous valid char")
            else: # p[0]=a
                if p[1]==".": # p = a.
                    return len(s)>=1 and s[0]==p[0] and len(s)==2
                elif p[1]=="*":  #p= a*, s must be aaaaa
                    # empty string or s[0]==p[0], s[i]==s[0] for all i
                    return s=="" or set(s).issubset(set(p[:1]))
                else: # p=aa
                    return s==p
        if len(s)==0:
            # p must be empty or a*b*...c*
            print('s=0',s,p)
            return len(p)==0 or (len(p)%2==0 and set(p[1::2])==set(["*"]))
        elif len(s)==1:
            # s=a, p = a,  a*,a*b*,a*c*,a*d*,...,an*, .*
            if p==s:
                return True
            elif p[-1] not in  "*.":
                if p[-1]!=s:
                    return False
                else:
                    return self.is_match("", p[:-1])
            elif p[-1]=="*" and p[-2]!=s: # p=a*b*
                return self.is_match(s, p[:-2])
            elif p[-1]=="*" and p[-2]==s:
                x1 = self.is_match(s, p[:-2])
                x2 = self.is_match("", p)
                print("len(s)==1", x1, s, p[:-2], x2, "",p)
                return x1 or x2
            elif p[-1]==".":
                return self.is_match("", p[:-1])
        return s, p

    def is_match(self, s, p):
        if "*" not in p and "." not in p:
            return self.is_match_no_star_and_dot(s,p)
        if "*" not in p:
            return self.is_match_only_dot(s,p)
        out = self.solve_edge_case(s,p)
        if isinstance(out, bool):
            return out
        else:
            s, p = out
        n_old = len(p)
        n = n_old+1
        while n_old < n:
            n = n_old
            out= self.reduce_normal_char_prefix_surfix(s, p)
            print('out',out,'s,p', s,p)
            if isinstance(out, bool):
                return out
            else:
                s, p = out


            n_old = len(p)

        # p = self.reduce_p(p)
        if len(s)<=1 or len(p)<=2:
            return self.is_match(s,p)
        else:
            return self.is_match_by_prefix_surfix(s, p)

    def is_match_by_prefix_surfix(self,s, p):
        # p: begin [a*, .*], end with [a*, .*]
        assert p[1]=="*" and p[-1]=="*", "p should be begin [a*, .*], end with [a*, .*]"
        # devide into two cases: a* = "" or a*=aa*
        print('prefix', 's',s,'p',p)
        if p[0]!=s[0] and p[0]!=".": # s = a? p= b*
            return self.is_match(s, p[2:])

        if p[-2]!="." and p[-2]!=s[-1]: # s= "ab", p ="?c*"
            return self.is_match(s, p[:-2])

        x1 = self.is_match(s, p[2:]) # a*=""
        print('x1', s, p[2:])
        x2 = self.is_match(s[1:], p) # a*=aa*
        print("x2", s[1:], p)
        return x1 or x2

    def is_match_only_dot(self, s,p):
        # p only contains .
        if len(p)==len(s):
            for si,pi in zip(s,p):
                if pi != "." and pi != si:
                    return False
            return True
        return False

    def is_match_no_star_and_dot(self,s,p):
        # no * and . in p
        return s==p

    def reduce_normal_char_prefix_surfix(self, s, p):
        # assume len(p)>=3
        # all possible for begin [aa, a*, a., .a, .*,.., *a, **, *.]

        if p[0]=="*": # removed *a, **, *.
            raise ValueError("p[0] cannot be *")
        if len(p)<=2 or len(s)<=1:
            return self.solve_edge_case(s,p)
        if p[0] == "." and p[1] !="*":
            s = s[1:]
            p = p[1:] # removed .a, ..
        # left [aa, a*, a., .*,]
        if p[0] not in '.*' and p[1]!="*":
            print('p[0]', 's',s, 'p',p)
            if p[0]!=s[0]:
                return False
            else:
                s = s[1:]
                p = p[1:]
            # remove aa, a.
        # left [a*, .*]

        # consider last two # all possible [aa, a*, a., .a, .*,.., *a, **, *.]
        if "**" in p:
            raise ValueError("Cannot have ** in p")
        if p[-1] not in '.*':
            if p[-1]!=s[-1]:
                return False
            else:
                s = s[:-1]
                p = p[:-1]
            # remove .a, *a, aa
        if p[-1] == ".":
            s = s[:-1]
            p = p[:-1]
            # remove a., *., ..
        # left [a*, ,.*]
        return s, p

class Solution2(object): # time limit exceed
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], "."}

        if len(pattern) >= 2 and pattern[1] == "*":
            # p start with a* or .*
            # two cases * =0 or *>1
            x1 = self.isMatch(text, pattern[2:]) # *=0
            x2 = self.isMatch(text[1:], pattern) # *>1
            return x1 or (first_match and x2)
        else:
            # p start with aa, a.,.a or ..
            return first_match and self.isMatch(text[1:], pattern[1:])

class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a DP table with dimensions (len(s) + 1) x (len(p) + 1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # dp[i][j], i is the index of s, j is the index of p
        # dp[i][j] means the match of substring s[:i], p[:j]
        # i, j = 0, 0, means empty string, empty pattern

        # Empty pattern matches empty string
        dp[0][0] = True # 0,0 if s[:n], p[:n]

        # Handle patterns like a*, a*b*, a*b*c* for empty string
        for j in range(2, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        # solve start condition dp[0][j], all old is False

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # we need to find the d[i][j] transition formula
                # dp[i][j] -> s[...,j-2,i-1], p[..,j-2,j-1]
                # if p[j-1] == *
                ## then it could be devide into two cases a* = "", (a* = aa* and s[i] begin with a)
                ## dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-2] in {s[i-1], .})
                # if  p[j-1] != *
                ## last one must match
                ## dp[i,j] = dp[i-1][j-1]  and p[j-1] in {s[i-1], '.'}
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-2] in {s[i-1], '.'})
                else:
                    dp[i][j] = dp[i-1][j-1] and p[j-1] in {s[i-1], '.'}
        return dp[len(s)][len(p)]

class Solution3:
    """combine dp method and some edge condition"""

    def isMatch(self, s: str, p: str) -> bool:
        # reduce normal char prefix and surfix
        n = len(p)
        while True:
            if len(p)<=2:
                return self.solve_edge_case(s,p)
            out= self.reduce_normal_char_prefix_surfix(s, p)
            if isinstance(out, bool):
                return out
            else:
                s, p = out
                if len(p) == n: # cannot reduce anymore
                    break
                else:
                    n = len(p)
        if "*" not in p and "." not in p:
            return self.is_match_no_star_and_dot(s,p)
        if "*" not in p:
            return self.is_match_only_dot(s,p)

        return self.dp_solution(s, p)

    def reduce_normal_char_prefix_surfix(self, s, p):
        if p[0]=="*": # removed *a, **, *.
            raise ValueError("p[0] cannot be *")
        if p[0] == "." and p[1] !="*":
            if s=="":
                return False
            s = s[1:]
            p = p[1:] # removed .a, ..
        # left [aa, a*, a., .*,]
        if p[0] not in '.*' and p[1]!="*":
            if s=="":
                return False
            if p[0]!=s[0]:
                return False
            else:
                s = s[1:]
                p = p[1:]
            # remove aa, a.
        # left [a*, .*]

        # consider last two # all possible [aa, a*, a., .a, .*,.., *a, **, *.]
        if "**" in p:
            raise ValueError("Cannot have ** in p")
        if p[-1] not in '.*':

            if len(s)<1 or p[-1]!=s[-1]:
                return False
            else:
                s = s[:-1]
                p = p[:-1]
            # remove .a, *a, aa
        if p[-1] == ".":
            if s=="":
                return False
            s = s[:-1]
            p = p[:-1]
            # remove a., *., ..
        # left [a*, ,.*]
        return s, p

    def is_match_only_dot(self, s,p):
        # p only contains .
        if len(p)==len(s):
            for si,pi in zip(s,p):
                if pi != "." and pi != si:
                    return False
            return True
        return False

    def is_match_no_star_and_dot(self,s,p):
        return s==p

    def solve_edge_case(self, s,p):
        assert len(p)<=2, "only for case len(p)<=2, len(p)={} , s={}, p={}".format(len(p),s,p)
        if len(p)==0:
            return len(s)==0

        if len(p)==1:
            return len(s)==1 and (s==p or p==".")

        if len(p)==2: #
            if p[0]==".":
                if p == ".*":
                    return True
                elif p=="..":
                    return len(s)==2
                else:
                    return len(s)==len(p) and s[1]==p[1]
            elif p[0]=="*":
                raise Exception("There should be a previous valid char")
            else: # p[0]=a
                if p[1]==".": # p = a.
                    return len(s)>=1 and s[0]==p[0] and len(s)==2
                elif p[1]=="*":  #p= a*, s must be aaaaa
                    # empty string or s[0]==p[0], s[i]==s[0] for all i
                    return s=="" or set(s).issubset(set(p[:1]))
                else: # p=aa
                    return s==p
        return False

    def dp_solution(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True # 0,0 if s[:n], p[:n]
        for j in range(2, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-2] in {s[i-1], '.'})
                else:
                    dp[i][j] = dp[i-1][j-1] and p[j-1] in {s[i-1], '.'}
        return dp[len(s)][len(p)]


if __name__ == "__main__":
    s = ['aa','ab', "aaab", "aaaabccd","aa"]
    p = ["a*","b*", "aab*", "a*b*c*d","a"]
    s = ['mississippi']
    s = ["mississippi"]
    p = ["mis*is*ip*."]
    # p = ["mis*is*p*."]
    # s = ["aa"]
    # p = ["aa"]
    # s = ['aaca']
    # p = ["ab*a*c*a"]
    # s = ["bbbba"]
    # p = [".*a*a"]
    # s = ["a"]
    # p = [".*..a*"]
    # s = ["ab"]
    # p = [".*.."]
    # s = ["a"]
    # p = ["b.."]
    # s = ["aaacacbbaaaabbcaa"]
    # p = ["ab*ac*a*abb*a.baa*"]
    # s =["cbacbbabbcaabbb"]
    # p = ["b*c*.*a*..a.*c*.*"]
    for si,pi in zip(s,p):
        y = Solution().isMatch(si,pi)
        print('y',y)

    test_cases = [
        ("aa", "a*"),
        ("ab", ".*"),
        ("mississippi", "mis*is*ip*."),
        ("aab", "c*a*b"),
        ("", "a*b*"),
        ("a", "ab*"),
        ("aaa", "a*a")
    ]

    solution = Solution4()
    for s, p in test_cases:
        result = solution.isMatch(s, p)
        print(f"s: {s}, p: {p}, matches: {result}")
