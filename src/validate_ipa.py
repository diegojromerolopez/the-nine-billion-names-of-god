import panphon
import regex as re
import sys


# Shameless copied from panphon project
# adapted to be an IPA string validator
class Validator(object):
    def __init__(self):
        """
        Validate Unicode IPA from file relative to panphon database.
        """
        self.ws_punc_regex = re.compile(r'[," \t\n]', re.V1 | re.U)
        self.ft = panphon.FeatureTable()

    def validate(self, ipa_string) -> bool:
        """
        Validate Unicode IPA string relative to panphon.

        line -- String of IPA characters. Can contain whitespace and limited
        punctuation.
        """
        line0 = ipa_string
        pos = 0
        while ipa_string:
            seg_m = self.ft.seg_regex.match(ipa_string)
            wsp_m = self.ws_punc_regex.match(ipa_string)
            if seg_m:
                length = len(seg_m.group(0))
                ipa_string = ipa_string[length:]
                pos += length
            elif wsp_m:
                length = len(wsp_m.group(0))
                ipa_string = ipa_string[length:]
                pos += length
            else:
                msg = 'IPA not valid at position {} in "{}".'.format(pos, line0.strip())
                print(msg, file=sys.stderr)
                ipa_string = ipa_string[1:]
                pos += 1
                return False
        return True
