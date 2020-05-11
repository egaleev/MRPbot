import pymorphy2

morph = pymorphy2.MorphAnalyzer()


class WordParsing():
    def __init__(self, word):
        self.word = word.lower()
        self.temp = ''
        if len(morph.parse(word)) > 1:
            self.temp += (
                f'Слово {self.word} может быть разобрано {len(morph.parse(self.word))} способами.'
                f'Вариант разбора зависит от того,в составе какогo'
                f'словосочетания или предложения слово находится.'
                f'Выберите подходящий вариант для вашего случая:\n\n')
            for i in range(len(morph.parse(self.word))):
                self.temp += (f'{i + 1} разбор: \n')
                self.nd = ['смотреть', 'видеть', 'ненавидеть', 'терпеть', 'обидеть', 'зависеть', 'вертеть',
                           'гнать', 'дышать', 'держать', 'слышать']
                self.st = ['брить', 'стелить']
                self.mrp = morph.parse(self.word)[i]
                if self.part_of_speech() == 'существительное':
                    self.s_parsing()
                elif self.part_of_speech() == 'глагол':
                    self.gl_parsing()
                elif self.part_of_speech() == 'деепричастие':
                    self.dpr_parsing()
                elif self.part_of_speech() == 'прилагательное':
                    self.prl_parsing()
                elif self.part_of_speech() == 'причастие':
                    self.prch_parsing()
                elif self.part_of_speech() == 'числительное':
                    self.n_parsing()
                elif self.part_of_speech() == 'наречие':
                    self.nar_parsing()
                elif self.part_of_speech() == 'местоимение':
                    self.pl_parsing()
                self.temp += "\n\n"

        else:
            self.nd = ['смотреть', 'видеть', 'ненавидеть', 'терпеть', 'обидеть', 'зависеть', 'вертеть',
                       'гнать', 'дышать', 'держать', 'слышать']
            self.st = ['брить', 'стелить']
            self.mrp = morph.parse(self.word)[0]
            if self.part_of_speech() == 'существительное':
                self.s_parsing()
            elif self.part_of_speech() == 'глагол':
                self.gl_parsing()
            elif self.part_of_speech() == 'деепричастие':
                self.dpr_parsing()
            elif self.part_of_speech() == 'прилагательное':
                self.prl_parsing()
            elif self.part_of_speech() == 'причастие':
                self.prch_parsing()
            elif self.part_of_speech() == 'числительное':
                self.n_parsing()
            elif self.part_of_speech() == 'наречие':
                self.nar_parsing()
            elif self.part_of_speech() == 'местоимение':
                self.pl_parsing()
            else:
                self.temp = "error"
            self.temp += "\n"

    def pl_parsing(self):
        self.temp += (f'I.{self.word} - местоимение\n')
        self.temp += (f'II.Начальная форма - {self.normalform()}\n')
        self.temp += (f'Постоянные признаки: {self.face()}\n')
        self.temp += (f'Непостоянные признаки: {self.case()} {self.num()}\n')
        self.temp += (
            f'III.Может быть различным членом предложения, смотрите по контексту.')

    def nar_parsing(self):
        self.temp = ''
        self.temp += f'I.{self.word} - {self.part_of_speech()}\n'
        self.temp += f'II.Начальная форма - {self.normalform()}\n'
        self.temp += f'Морфологические признаки: {self.compr()}\n'
        self.temp += f'III.Может быть различным членом предложения, смотрите по контексту.'

    def composite(self):
        if len(self.word.split()) > 1:
            return 'составное,'
        else:
            return 'простое,'

    def n_parsing(self):
        self.temp = ''
        self.temp += f'I.{self.word} - {self.part_of_speech()}\n'
        self.temp += f'II.Начальная форма - {self.normalform()}\n'
        self.temp += f'Постоянные признаки:{self.composite()}{self.freq()}\n'
        self.temp += f'Непостоянные признаки: {self.case()} {self.num()}'f'{self.gender()}\n'
        self.temp += f'III.Может быть различным членом предложения, смотрите по контексту.'

    def gl_parsing(self):
        self.temp = ''
        self.temp += f'I.{self.word} - {self.part_of_speech()}\n'
        self.temp += f'II.Начальная форма - {self.normalform()}\n'
        self.temp += f'Постоянные признаки: {self.viev()} {self.pere()} {self.spry()}\n'
        self.temp += f'Непостоянные признаки: {self.mood()} {self.num()}'f' {self.time()} {self.face()} {self.gender()}\n'
        self.temp += f'III.Может быть различным членом предложения, смотрите по контексту.'

    def prl_parsing(self):
        self.temp = ''
        self.temp += f'I.{self.word} - {self.part_of_speech()}\n'
        self.temp += f'II.Начальная форма - {self.normalform()}\n'
        self.temp += f'Постоянные признаки: {self.quality()} \n'
        self.temp += f'Непостоянные признаки:'
        if self.quality() == 'качественное,':
            self.temp += f'{self.compr()}\n {self.short()}'
        self.temp += f'{self.case()} {self.num()} {self.gender()}\n'

        self.temp += f'III.Может быть различным членом предложения, смотрите по контексту.'

    def active(self):
        if 'actv' in self.mrp.tag:
            return 'действительный залог,'
        elif 'pssv' in self.mrp.tag:
            return 'страдательный залог,'

    def prch_parsing(self):
        self.temp = ''
        self.temp += f'I. {self.word} - {self.part_of_speech()}\n'
        self.temp += f'II.Начальная форма - {self.normalform()}\n'
        self.temp += f'Постоянные признаки: {self.active()} {self.time()} {self.viev()}\n'
        self.temp += f'Непостоянные признаки: '
        if self.active() == 'страдательное,':
            self.temp += f'{self.short()}'
        if self.short() == 'полная форма,':
            self.temp += f'{self.case()}'
        self.temp += f'{self.num()} {self.gender()}\n'

        self.temp += f'III.Может быть различным членом предложения, смотрите по контексту.'

    def dpr_parsing(self):
        self.temp = ''
        self.temp += f'I.{self.word} - {self.part_of_speech()}\n'
        self.temp += f'II.Начальная форма - {self.normalform()}\n'
        self.temp += f'Морфологические признаки: {self.viev()} неизменяемая форма, {self.time()}\n'
        self.temp += f'III.Может быть различным членом предложения, смотрите по контексту.'

    def part_of_speech(self):
        if 'NOUN' in self.mrp.tag:
            return 'существительное'
        if 'NUMR' in self.mrp.tag or "Anum" in self.mrp.tag:
            return 'числительное'
        if 'ADJF' in self.mrp.tag or 'ADJS' in self.mrp.tag or 'COMP' in self.mrp.tag:
            return 'прилагательное'
        if 'VERB' in self.mrp.tag or 'INFN' in self.mrp.tag:
            return 'глагол'
        if 'PRTF' in self.mrp.tag or 'PRTS' in self.mrp.tag:
            return 'причастие'
        if 'GRND' in self.mrp.tag:
            return 'деепричастие'
        if 'NPRO' in self.mrp.tag:
            return 'местоимение'
        if 'ADVB' in self.mrp.tag:
            return 'наречие'

    def freq(self):
        if 'Anum' in self.mrp.tag:
            return 'порядковое,'
        else:
            return 'количественное,'

    def face(self):
        if '1per' in self.mrp.tag:
            return '1 лицо,'
        elif '2per' in self.mrp.tag:
            return '2 лицо,'
        elif '3per' in self.mrp.tag:
            return '3 лицо,'
        else:
            return ''

    def compr(self):
        if 'Cmp2' in self.mrp.tag or 'V-ej' in self.mrp.tag or 'COMP' in self.mrp.tag:
            return 'сравнительная степень, '
        elif 'Supr' in self.mrp.tag:
            return 'превосходная степень, '
        else:
            return 'положительная степень, '

    def time(self):
        if 'pres' in self.mrp.tag:
            return 'настоящее время,'
        elif 'past' in self.mrp.tag:
            return 'прошедшее время,'
        elif 'futr' in self.mrp.tag:
            return 'будущее время,'
        else:
            return ''

    def mood(self):
        if 'indc' in self.mrp.tag:
            return 'изъявительное наклонение,'
        else:
            return 'повелительное наклонение,'

    def pere(self):
        if 'tran' in self.mrp.tag:
            return 'переходный,'
        else:
            return 'непероходный,'

    def viev(self):
        if 'perf' in self.mrp.tag:
            return 'совершенный вид,'
        else:
            return "несовершенный вид,"

    def spry(self):
        if self.mrp.inflect({'pres', '2per'}) != None:
            if self.mrp.inflect({'pres', '2per'})[-3] == 'и' or self.word in self.nd and self.word not in self.st:
                return 'II спряжение'
            else:
                return 'I спряжение'
        else:
            return 'к сожалению я не могу определить спряжение,'

    def short(self):
        if 'ADJS' in self.mrp.tag or 'PRTS' in self.mrp.tag:
            return "краткая форма,"
        else:
            return 'полная форма,'

    def gender(self):
        if 'masc' in self.mrp.tag:
            return 'мужской род,'
        elif 'femn' in self.mrp.tag:
            return 'женский род,'
        elif 'neut' in self.mrp.tag:
            return 'средний род,'
        else:
            return ''

    def declination(self):
        if (self.gender() == 'мужской род,' or self.gender() == 'женский род,') and (
                self.normalform()[-1] == 'а' or self.normalform()[-1] == 'я'):
            return '1 склонение,'
        elif (self.gender() == 'мужской род,') or (
                self.gender() == 'средний род,' and self.normalform()[
            -1] == 'о') or (
                self.gender() == 'средний род,' and self.normalform()[-1] == 'е'):
            return '2 склонение,'
        elif (self.gender() == 'женский род,'):
            return '3 склонение,'

    def proper_or_common(self):
        if 'Name' in self.mrp.tag:
            return 'имя собственное,'
        elif 'Surn' in self.mrp.tag:
            return 'имя собственное,'
        elif 'Patr' in self.mrp.tag:
            return 'имя собственное,'
        elif 'Geox' in self.mrp.tag:
            return 'имя собственное,'
        elif 'Orgn' in self.mrp.tag:
            return 'имя собственное,'
        elif 'Trad' in self.mrp.tag:
            return 'имя собственное,'
        else:
            return 'имя нарицательное,'

    def s_parsing(self):
        self.temp += (f'I.{self.word} - сущ\n')
        self.temp += (f'II.Начальная форма - {self.normalform()}\n')
        self.temp += (
            f'Постоянные признаки: {self.proper_or_common()} {self.anim()} {self.gender()}'
            f' {self.declination()}\n')
        self.temp += (f'Непостоянные признаки: {self.case()} {self.num()}\n')
        self.temp += (
            f'III.Может быть различным членом предложения, смотрите по контексту.')

    def anim(self):
        if 'anim' in self.mrp.tag:
            return 'одушевлённое,'
        else:
            return 'неодушевлённое,'

    def case(self):
        if 'nomn' in self.mrp.tag:
            return 'Именительный падеж,'
        elif 'gent' in self.mrp.tag:
            return 'Родительный падеж,'
        elif 'datv' in self.mrp.tag:
            return 'Дательный падеж,'
        elif 'accs' in self.mrp.tag:
            return 'Винительный падеж,'
        elif 'ablt' in self.mrp.tag:
            return 'Творительный падеж,'
        elif 'loct' in self.mrp.tag:
            return 'Предложный падеж,'
        else:
            return ''

    def num(self):
        if 'sing' in self.mrp.tag:
            return 'единственное число,'
        else:
            return 'множественное число,'

    def quality(self):
        if 'Qual' in self.mrp.tag:
            return 'качественное,'
        elif 'Poss' in self.mrp.tag:
            return 'притяжательное,'
        else:
            return 'относительное,'

    def normalform(self):
        if "Anum" in self.mrp.tag:
            return self.mrp.inflect({'masc'}).inflect({'nomn'}).word
        elif self.part_of_speech() == 'причастие':
            return self.mrp.inflect({'masc'}).inflect({'nomn'}).inflect({'sing'}).word
        else:
            return self.mrp.normal_form
