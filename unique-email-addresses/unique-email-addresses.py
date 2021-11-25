class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for index, value in enumerate(emails):
            local, domain = value.split('@') # split local and domain at @
            local = local.split('+')[0] # remove everything after the first '+' on local
            local = local.replace('.', '') #remove all '.' from local
            result.add(local+'@'+domain)
        return len(result)