import datetime
import pytz
from django.conf import settings
from django.http import HttpResponse
import re


Dict_Char_Persian_English = {
    'ا':'a1',
    'آ':'a2',
    'ب':'b1',
    'پ':'p1',
    'ت':'t1',
    'ث':'c1',
    'ج':'j1',
    'چ':'ch',
    'ح':'h1',
    'خ':'kh',
    'د':'d1',
    'ذ':'z1',
    'ر':'r1',
    'ز':'z2',
    'ژ':'zh',
    'س':'c2',
    'ش':'sh',
    'ص':'c3',
    'ض':'z3',
    'ط':'t2',
    'ظ':'z4',
    'ع':'a3',
    'غ':'g_',
    'ف':'f1',
    'ق':'g5',
    'ک':'k1',
    'گ':'k2',
    'ل':'l1',
    'م':'m1',
    'ن':'n1',
    'و':'v1',
    'ه':'h2',
    'ی':'e2',
    ' ':'11',
    '':'22',
}

def ConvertPersianCharToEnglish(Text):
    Res = ''
    for i in Text:
        try:
            Res += Dict_Char_Persian_English[i]
        except:
            Res += i
    return Res


def Set_Cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE or None,
    )
    return response

def Set_Cookie_Functionality(Text,Type,Timer='5000',LevelOfNecessity='2',RedirectTo=None):
    if RedirectTo == None:
        Res = HttpResponse('<script>setTimeout(()=>{window.history.back();},50);</script>')
    else:
        Res =  HttpResponse(f"<script>location.href='{RedirectTo}';</script>")
    Set_Cookie(Res,'Functionality_N',f"{ConvertPersianCharToEnglish(Text)}~{Type}~{Timer}~{LevelOfNecessity}",1)
    return Res


def GetTimeIran():
    TimeIranZone = pytz.timezone('Asia/Tehran')
    TimeIranObject = datetime.datetime.now(TimeIranZone)
    TimeIran = TimeIranObject.now()
    return TimeIran


def GetDifferenceTime(Time):
    TimeIranZone = pytz.timezone('Asia/Tehran')
    TimeIranObject = datetime.datetime.now(TimeIranZone)
    TimeIran = TimeIranObject.now()
    DifferenceTime = datetime.datetime(TimeIran.year, TimeIran.month, TimeIran.day, TimeIran.hour,
                                       TimeIran.minute) - datetime.datetime(Time.year, Time.month, Time.day, Time.hour,
                                                                            Time.minute)
    DifferenceTimeSecond = DifferenceTime.seconds
    Second = DifferenceTimeSecond % 60
    Minute = DifferenceTimeSecond // 60 % 60
    Hour = DifferenceTimeSecond // 3600
    Day = DifferenceTime.days
    Str = ''
    if Minute > 0:
        Str = f'{Minute} دقیقه پیش'
    else:
        Str = f'لحظاتی پیش'

    if Hour > 0:
        Str = f'{Hour} ساعت پیش'

    if Day > 0:
        Str = f'{Day}  روز پیش'

    return Str

def GetDifferenceDate(Time):
    TimeIranZone = pytz.timezone('Asia/Tehran')
    TimeIranObject = datetime.datetime.now(TimeIranZone)
    TimeIran = TimeIranObject.now()
    DifferenceTime = datetime.datetime(TimeIran.year, TimeIran.month, TimeIran.day) - datetime.datetime(Time.year, Time.month, Time.day)
    Day = DifferenceTime.days
    Str = ''
    if Day > 0:
        Str = f'{Day} روز '
    else:
        Str = f'امروز'

    if Day > 6:
        Str = f'{Day} هفته '

    if Day > 30:
        Str = f'{Day}  ماه '

    return Str


def GetDifferenceTimeObj(Time):
    TimeIranZone = pytz.timezone('Asia/Tehran')
    TimeIranObject = datetime.datetime.now(TimeIranZone)
    TimeIran = TimeIranObject.now()
    DifferenceTime = datetime.datetime(TimeIran.year, TimeIran.month, TimeIran.day, TimeIran.hour,
                                       TimeIran.minute) - datetime.datetime(Time.year, Time.month, Time.day, Time.hour,
                                                                            Time.minute)
    DifferenceTimeSecond = DifferenceTime.seconds
    Second = DifferenceTimeSecond % 60
    Minute = DifferenceTimeSecond // 60 % 60
    Hour = DifferenceTimeSecond // 3600
    Day = DifferenceTime.days
    return {
        'Second':Second,
        'Minute':Minute,
        'Hour':Hour,
        'Day':Day
    }


def ValidationText(Text,Bigger=None,Less=None,NoSpace=False,En=False):
    State = False
    if Text is not None and Text is not '' and str(Text).strip() is not '':
        State = True
        Text = str(Text)
        if Bigger != None and Less != None:
            if Bigger < len(Text) and Less > len(Text):
                State = True
            else:
                State = False
    if NoSpace:
        if ' ' in Text:
           State = False
    if En:
        if bool(re.match('[a-zA-Z0-9]+$',Text)) == False:
            State = False

    return State

def ValidationNumber(Number,Bigger=None,Less=None):
    StateNumber = Number.isdigit()
    if Number is not None:
        if StateNumber:
            if Bigger is not None and Less is not None:
                if Number > Bigger and Number < Less:
                    return True
                else:
                    return False
            else:
                return True
        return False
    return False



def SerializerTool(Model,Objects,Attributes='__All__',Methods=[]):
    # Model = eval(Objects[0].__class__.__name__)
    ListJSON = []
    for Object in Objects:
        JSON = {}
        AllFields = Model._meta.fields if Attributes == '__All__' else [Field for Field in Model._meta.fields if Field.name in Attributes]
        for Field in AllFields:
            Value = getattr(Object,Field.name)
            if Field.get_internal_type() == 'DateTimeField' or Field.get_internal_type() == 'DateField':
                Value = str(Value)
            if Field.get_internal_type() == 'ForeignKey':
                Value = str(Value.id)
            JSON[Field.name] = Value
        for Method in Methods:
            try:
                JSON[Method] = getattr(Object, Method)()
            except TypeError:
                raise Exception('Value Passed is not Method')
        ListJSON.append(JSON)
    return ListJSON