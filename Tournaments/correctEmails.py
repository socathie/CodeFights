def correctEmails(pattern):
    def isSymbol(c):
        return ord('a') <= ord(c) <= ord('e')

    def isCorrectEmail(emailList):
        email = ''.join(emailList)
        return (email.count('@') == 1 and
          email.count('.') >= 1 and
          email.rfind('.') > email.rfind('@') and
          email.find('..') == -1 and
          email.find('.@') == -1 and
          email.find('@.') == -1 and
          isSymbol(email[0]) and
          isSymbol(email[-1]))

    def countCorrectEmails(pattern, position):
        if position == len(pattern):
            return 1 if isCorrectEmail(pattern) else 0
        if pattern[position] != '?':
            return countCorrectEmails(pattern, position + 1)
        answer = 0
        pattern[position] = '@'
        answer += countCorrectEmails(pattern, position + 1)
        pattern[position] = '.'
        answer += countCorrectEmails(pattern, position + 1)
        pattern[position] = 'a'
        answer += countCorrectEmails(pattern, position + 1) * 5
        pattern[position] = '?'
        return answer

    return countCorrectEmails(list(pattern), 0)
