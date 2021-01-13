import unittest
import traceback
from perm_lex import *


class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex_00_empty_string(self):
        self.assertEqual(perm_gen_lex(''), [])


    def test_perm_gen_lex_01_a(self):
        self.assertEqual(perm_gen_lex('a'), ['a'])


    def test_perm_gen_lex_02_ab(self):
        self.assertEqual(perm_gen_lex('ab'), ['ab', 'ba'])


    def test_perm_gen_lex_03_abc(self):
        self.assertEqual(perm_gen_lex('amz'), ['amz', 'azm', 'maz', 'mza', 'zam', 'zma'])


    def test_perm_gen_lex_04_abyz(self):
        self.assertEqual(perm_gen_lex('abyz'), ['abyz', 'abzy', 'aybz', 'ayzb', 'azby', 'azyb', 'bayz', 'bazy', 'byaz', 'byza', 'bzay', 'bzya', 'yabz', 'yazb', 'ybaz',
                                                'ybza', 'yzab', 'yzba', 'zaby', 'zayb', 'zbay', 'zbya', 'zyab', 'zyba'])


    def test_perm_gen_lex_05_abmyz(self):
        self.assertEqual(perm_gen_lex('abmyz'), ['abmyz', 'abmzy', 'abymz', 'abyzm', 'abzmy', 'abzym', 'ambyz', 'ambzy', 'amybz', 'amyzb', 'amzby', 'amzyb', 'aybmz', 
                                                 'aybzm', 'aymbz', 'aymzb', 'ayzbm', 'ayzmb', 'azbmy', 'azbym', 'azmby', 'azmyb', 'azybm', 'azymb', 'bamyz', 'bamzy', 
                                                 'baymz', 'bayzm', 'bazmy', 'bazym', 'bmayz', 'bmazy', 'bmyaz', 'bmyza', 'bmzay', 'bmzya', 'byamz', 'byazm', 'bymaz', 
                                                 'bymza', 'byzam', 'byzma', 'bzamy', 'bzaym', 'bzmay', 'bzmya', 'bzyam', 'bzyma', 'mabyz', 'mabzy', 'maybz', 'mayzb', 
                                                 'mazby', 'mazyb', 'mbayz', 'mbazy', 'mbyaz', 'mbyza', 'mbzay', 'mbzya', 'myabz', 'myazb', 'mybaz', 'mybza', 'myzab', 
                                                 'myzba', 'mzaby', 'mzayb', 'mzbay', 'mzbya', 'mzyab', 'mzyba', 'yabmz', 'yabzm', 'yambz', 'yamzb', 'yazbm', 'yazmb', 
                                                 'ybamz', 'ybazm', 'ybmaz', 'ybmza', 'ybzam', 'ybzma', 'ymabz', 'ymazb', 'ymbaz', 'ymbza', 'ymzab', 'ymzba', 'yzabm', 
                                                 'yzamb', 'yzbam', 'yzbma', 'yzmab', 'yzmba', 'zabmy', 'zabym', 'zamby', 'zamyb', 'zaybm', 'zaymb', 'zbamy', 'zbaym', 
                                                 'zbmay', 'zbmya', 'zbyam', 'zbyma', 'zmaby', 'zmayb', 'zmbay', 'zmbya', 'zmyab', 'zmyba', 'zyabm', 'zyamb', 'zybam', 
                                                 'zybma', 'zymab', 'zymba'])


    def test_perm_gen_lex_06_abmnyz(self):
        self.assertEqual(perm_gen_lex('abmnyz'),['abmnyz', 'abmnzy', 'abmynz', 'abmyzn', 'abmzny', 'abmzyn', 'abnmyz', 'abnmzy', 'abnymz', 'abnyzm', 'abnzmy', 'abnzym',
                                                 'abymnz', 'abymzn', 'abynmz', 'abynzm', 'abyzmn', 'abyznm', 'abzmny', 'abzmyn', 'abznmy', 'abznym', 'abzymn', 'abzynm',
                                                 'ambnyz', 'ambnzy', 'ambynz', 'ambyzn', 'ambzny', 'ambzyn', 'amnbyz', 'amnbzy', 'amnybz', 'amnyzb', 'amnzby', 'amnzyb',
                                                 'amybnz', 'amybzn', 'amynbz', 'amynzb', 'amyzbn', 'amyznb', 'amzbny', 'amzbyn', 'amznby', 'amznyb', 'amzybn', 'amzynb',
                                                 'anbmyz', 'anbmzy', 'anbymz', 'anbyzm', 'anbzmy', 'anbzym', 'anmbyz', 'anmbzy', 'anmybz', 'anmyzb', 'anmzby', 'anmzyb',
                                                 'anybmz', 'anybzm', 'anymbz', 'anymzb', 'anyzbm', 'anyzmb', 'anzbmy', 'anzbym', 'anzmby', 'anzmyb', 'anzybm', 'anzymb',
                                                 'aybmnz', 'aybmzn', 'aybnmz', 'aybnzm', 'aybzmn', 'aybznm', 'aymbnz', 'aymbzn', 'aymnbz', 'aymnzb', 'aymzbn', 'aymznb',
                                                 'aynbmz', 'aynbzm', 'aynmbz', 'aynmzb', 'aynzbm', 'aynzmb', 'ayzbmn', 'ayzbnm', 'ayzmbn', 'ayzmnb', 'ayznbm', 'ayznmb',
                                                 'azbmny', 'azbmyn', 'azbnmy', 'azbnym', 'azbymn', 'azbynm', 'azmbny', 'azmbyn', 'azmnby', 'azmnyb', 'azmybn', 'azmynb',
                                                 'aznbmy', 'aznbym', 'aznmby', 'aznmyb', 'aznybm', 'aznymb', 'azybmn', 'azybnm', 'azymbn', 'azymnb', 'azynbm', 'azynmb',
                                                 'bamnyz', 'bamnzy', 'bamynz', 'bamyzn', 'bamzny', 'bamzyn', 'banmyz', 'banmzy', 'banymz', 'banyzm', 'banzmy', 'banzym',
                                                 'baymnz', 'baymzn', 'baynmz', 'baynzm', 'bayzmn', 'bayznm', 'bazmny', 'bazmyn', 'baznmy', 'baznym', 'bazymn', 'bazynm',
                                                 'bmanyz', 'bmanzy', 'bmaynz', 'bmayzn', 'bmazny', 'bmazyn', 'bmnayz', 'bmnazy', 'bmnyaz', 'bmnyza', 'bmnzay', 'bmnzya',
                                                 'bmyanz', 'bmyazn', 'bmynaz', 'bmynza', 'bmyzan', 'bmyzna', 'bmzany', 'bmzayn', 'bmznay', 'bmznya', 'bmzyan', 'bmzyna',
                                                 'bnamyz', 'bnamzy', 'bnaymz', 'bnayzm', 'bnazmy', 'bnazym', 'bnmayz', 'bnmazy', 'bnmyaz', 'bnmyza', 'bnmzay', 'bnmzya',
                                                 'bnyamz', 'bnyazm', 'bnymaz', 'bnymza', 'bnyzam', 'bnyzma', 'bnzamy', 'bnzaym', 'bnzmay', 'bnzmya', 'bnzyam', 'bnzyma',
                                                 'byamnz', 'byamzn', 'byanmz', 'byanzm', 'byazmn', 'byaznm', 'bymanz', 'bymazn', 'bymnaz', 'bymnza', 'bymzan', 'bymzna',
                                                 'bynamz', 'bynazm', 'bynmaz', 'bynmza', 'bynzam', 'bynzma', 'byzamn', 'byzanm', 'byzman', 'byzmna', 'byznam', 'byznma',
                                                 'bzamny', 'bzamyn', 'bzanmy', 'bzanym', 'bzaymn', 'bzaynm', 'bzmany', 'bzmayn', 'bzmnay', 'bzmnya', 'bzmyan', 'bzmyna',
                                                 'bznamy', 'bznaym', 'bznmay', 'bznmya', 'bznyam', 'bznyma', 'bzyamn', 'bzyanm', 'bzyman', 'bzymna', 'bzynam', 'bzynma',
                                                 'mabnyz', 'mabnzy', 'mabynz', 'mabyzn', 'mabzny', 'mabzyn', 'manbyz', 'manbzy', 'manybz', 'manyzb', 'manzby', 'manzyb',
                                                 'maybnz', 'maybzn', 'maynbz', 'maynzb', 'mayzbn', 'mayznb', 'mazbny', 'mazbyn', 'maznby', 'maznyb', 'mazybn', 'mazynb',
                                                 'mbanyz', 'mbanzy', 'mbaynz', 'mbayzn', 'mbazny', 'mbazyn', 'mbnayz', 'mbnazy', 'mbnyaz', 'mbnyza', 'mbnzay', 'mbnzya',
                                                 'mbyanz', 'mbyazn', 'mbynaz', 'mbynza', 'mbyzan', 'mbyzna', 'mbzany', 'mbzayn', 'mbznay', 'mbznya', 'mbzyan', 'mbzyna',
                                                 'mnabyz', 'mnabzy', 'mnaybz', 'mnayzb', 'mnazby', 'mnazyb', 'mnbayz', 'mnbazy', 'mnbyaz', 'mnbyza', 'mnbzay', 'mnbzya',
                                                 'mnyabz', 'mnyazb', 'mnybaz', 'mnybza', 'mnyzab', 'mnyzba', 'mnzaby', 'mnzayb', 'mnzbay', 'mnzbya', 'mnzyab', 'mnzyba',
                                                 'myabnz', 'myabzn', 'myanbz', 'myanzb', 'myazbn', 'myaznb', 'mybanz', 'mybazn', 'mybnaz', 'mybnza', 'mybzan', 'mybzna',
                                                 'mynabz', 'mynazb', 'mynbaz', 'mynbza', 'mynzab', 'mynzba', 'myzabn', 'myzanb', 'myzban', 'myzbna', 'myznab', 'myznba',
                                                 'mzabny', 'mzabyn', 'mzanby', 'mzanyb', 'mzaybn', 'mzaynb', 'mzbany', 'mzbayn', 'mzbnay', 'mzbnya', 'mzbyan', 'mzbyna',
                                                 'mznaby', 'mznayb', 'mznbay', 'mznbya', 'mznyab', 'mznyba', 'mzyabn', 'mzyanb', 'mzyban', 'mzybna', 'mzynab', 'mzynba',
                                                 'nabmyz', 'nabmzy', 'nabymz', 'nabyzm', 'nabzmy', 'nabzym', 'nambyz', 'nambzy', 'namybz', 'namyzb', 'namzby', 'namzyb',
                                                 'naybmz', 'naybzm', 'naymbz', 'naymzb', 'nayzbm', 'nayzmb', 'nazbmy', 'nazbym', 'nazmby', 'nazmyb', 'nazybm', 'nazymb',
                                                 'nbamyz', 'nbamzy', 'nbaymz', 'nbayzm', 'nbazmy', 'nbazym', 'nbmayz', 'nbmazy', 'nbmyaz', 'nbmyza', 'nbmzay', 'nbmzya',
                                                 'nbyamz', 'nbyazm', 'nbymaz', 'nbymza', 'nbyzam', 'nbyzma', 'nbzamy', 'nbzaym', 'nbzmay', 'nbzmya', 'nbzyam', 'nbzyma',
                                                 'nmabyz', 'nmabzy', 'nmaybz', 'nmayzb', 'nmazby', 'nmazyb', 'nmbayz', 'nmbazy', 'nmbyaz', 'nmbyza', 'nmbzay', 'nmbzya',
                                                 'nmyabz', 'nmyazb', 'nmybaz', 'nmybza', 'nmyzab', 'nmyzba', 'nmzaby', 'nmzayb', 'nmzbay', 'nmzbya', 'nmzyab', 'nmzyba',
                                                 'nyabmz', 'nyabzm', 'nyambz', 'nyamzb', 'nyazbm', 'nyazmb', 'nybamz', 'nybazm', 'nybmaz', 'nybmza', 'nybzam', 'nybzma',
                                                 'nymabz', 'nymazb', 'nymbaz', 'nymbza', 'nymzab', 'nymzba', 'nyzabm', 'nyzamb', 'nyzbam', 'nyzbma', 'nyzmab', 'nyzmba',
                                                 'nzabmy', 'nzabym', 'nzamby', 'nzamyb', 'nzaybm', 'nzaymb', 'nzbamy', 'nzbaym', 'nzbmay', 'nzbmya', 'nzbyam', 'nzbyma',
                                                 'nzmaby', 'nzmayb', 'nzmbay', 'nzmbya', 'nzmyab', 'nzmyba', 'nzyabm', 'nzyamb', 'nzybam', 'nzybma', 'nzymab', 'nzymba',
                                                 'yabmnz', 'yabmzn', 'yabnmz', 'yabnzm', 'yabzmn', 'yabznm', 'yambnz', 'yambzn', 'yamnbz', 'yamnzb', 'yamzbn', 'yamznb',
                                                 'yanbmz', 'yanbzm', 'yanmbz', 'yanmzb', 'yanzbm', 'yanzmb', 'yazbmn', 'yazbnm', 'yazmbn', 'yazmnb', 'yaznbm', 'yaznmb',
                                                 'ybamnz', 'ybamzn', 'ybanmz', 'ybanzm', 'ybazmn', 'ybaznm', 'ybmanz', 'ybmazn', 'ybmnaz', 'ybmnza', 'ybmzan', 'ybmzna',
                                                 'ybnamz', 'ybnazm', 'ybnmaz', 'ybnmza', 'ybnzam', 'ybnzma', 'ybzamn', 'ybzanm', 'ybzman', 'ybzmna', 'ybznam', 'ybznma',
                                                 'ymabnz', 'ymabzn', 'ymanbz', 'ymanzb', 'ymazbn', 'ymaznb', 'ymbanz', 'ymbazn', 'ymbnaz', 'ymbnza', 'ymbzan', 'ymbzna',
                                                 'ymnabz', 'ymnazb', 'ymnbaz', 'ymnbza', 'ymnzab', 'ymnzba', 'ymzabn', 'ymzanb', 'ymzban', 'ymzbna', 'ymznab', 'ymznba',
                                                 'ynabmz', 'ynabzm', 'ynambz', 'ynamzb', 'ynazbm', 'ynazmb', 'ynbamz', 'ynbazm', 'ynbmaz', 'ynbmza', 'ynbzam', 'ynbzma',
                                                 'ynmabz', 'ynmazb', 'ynmbaz', 'ynmbza', 'ynmzab', 'ynmzba', 'ynzabm', 'ynzamb', 'ynzbam', 'ynzbma', 'ynzmab', 'ynzmba',
                                                 'yzabmn', 'yzabnm', 'yzambn', 'yzamnb', 'yzanbm', 'yzanmb', 'yzbamn', 'yzbanm', 'yzbman', 'yzbmna', 'yzbnam', 'yzbnma',
                                                 'yzmabn', 'yzmanb', 'yzmban', 'yzmbna', 'yzmnab', 'yzmnba', 'yznabm', 'yznamb', 'yznbam', 'yznbma', 'yznmab', 'yznmba',
                                                 'zabmny', 'zabmyn', 'zabnmy', 'zabnym', 'zabymn', 'zabynm', 'zambny', 'zambyn', 'zamnby', 'zamnyb', 'zamybn', 'zamynb',
                                                 'zanbmy', 'zanbym', 'zanmby', 'zanmyb', 'zanybm', 'zanymb', 'zaybmn', 'zaybnm', 'zaymbn', 'zaymnb', 'zaynbm', 'zaynmb',
                                                 'zbamny', 'zbamyn', 'zbanmy', 'zbanym', 'zbaymn', 'zbaynm', 'zbmany', 'zbmayn', 'zbmnay', 'zbmnya', 'zbmyan', 'zbmyna',
                                                 'zbnamy', 'zbnaym', 'zbnmay', 'zbnmya', 'zbnyam', 'zbnyma', 'zbyamn', 'zbyanm', 'zbyman', 'zbymna', 'zbynam', 'zbynma',
                                                 'zmabny', 'zmabyn', 'zmanby', 'zmanyb', 'zmaybn', 'zmaynb', 'zmbany', 'zmbayn', 'zmbnay', 'zmbnya', 'zmbyan', 'zmbyna',
                                                 'zmnaby', 'zmnayb', 'zmnbay', 'zmnbya', 'zmnyab', 'zmnyba', 'zmyabn', 'zmyanb', 'zmyban', 'zmybna', 'zmynab', 'zmynba',
                                                 'znabmy', 'znabym', 'znamby', 'znamyb', 'znaybm', 'znaymb', 'znbamy', 'znbaym', 'znbmay', 'znbmya', 'znbyam', 'znbyma',
                                                 'znmaby', 'znmayb', 'znmbay', 'znmbya', 'znmyab', 'znmyba', 'znyabm', 'znyamb', 'znybam', 'znybma', 'znymab', 'znymba',
                                                 'zyabmn', 'zyabnm', 'zyambn', 'zyamnb', 'zyanbm', 'zyanmb', 'zybamn', 'zybanm', 'zybman', 'zybmna', 'zybnam', 'zybnma',
                                                 'zymabn', 'zymanb', 'zymban', 'zymbna', 'zymnab', 'zymnba', 'zynabm', 'zynamb', 'zynbam', 'zynbma', 'zynmab', 'zynmba'])


    def test_perm_gen_lex_07_acemvxz(self):
        x = perm_gen_lex('acemvxz')
        self.assertEqual(len(x), 5040)


    def test_perm_gen_lex_08_acemnvxz(self):
        x = perm_gen_lex('acemnvxz')
        self.assertEqual(len(x), 40320)


    def test_perm_gen_lex_09_acemnovxz(self):
        x = perm_gen_lex('acemnovxz')
        self.assertEqual(len(x), 362880)


    def test_perm_gen_lex_10_aaaaaaaaa(self):
        x = perm_gen_lex('aaaaaaaaa')
        self.assertEqual(len(x), 362880)

if __name__ == "__main__":
    unittest.main()
