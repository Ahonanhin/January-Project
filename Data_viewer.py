from platform import libc_ver
import pandas as pd
countries = pd.read_csv("countries.csv")

list_of_countries = countries.country.to_list()
list_of_capitals = countries.capital.to_list()

abbreviations = [country for country in countries.abbreviation.to_list()]
for abb in abbreviations:
    if type(abb) == str:
        if abb not in list_of_countries:
            list_of_countries.append(abb)

# compositions = [comp for comp in countries.composition.to_list()]
# for comp in compositions:
#     if type(comp) == str:
#         if comp not in list_of_countries:
#             list_of_countries.append(comp)

currencies = countries.currency.to_list()
currencies_ = []
for currency in currencies:
    if not currency in currencies_:
        currencies_.append(currency)

def get_capital_from_country(country_name: str)-> str:
    """Returns the capital of country_name according to the countries dataframe
    
    >>> get_capital_from_country("France") == "Paris"
    True
    """ 
    if country_name in abbreviations:
        index = countries[countries.abbreviation == country_name].index[0]
    # elif country_name in compositions:
    #     index = countries[countries.composition == country_name].index[0]
    else:
        index = countries[countries.country == country_name].index[0]
    return countries["capital"][index]

def get_country_from_capital(capital_name: str)-> str:
    """Returns the country whose capital is capital_name

    >>>  get_country_from_capital("Baku") == "Azerbaijan"
    True
    """
    index = countries[countries.capital == capital_name].index[0]
    return countries["country"][index]

def get_currency_from_country(country_name: str)-> str:
    """Returns the currency of country_name

    >>> print(get_currency_from_country("Spain"))
    Euro
    """
    index = countries[countries.country == country_name].index[0]
    return countries["currency"][index]


import pyttsx3
import playsound

def say_capital(country_name):
    text_speech = pyttsx3.init()
    text_speech.setProperty("rate", 140)
    if country_name in abbreviations:
        index = countries[countries.abbreviation == country_name].index[0]
    # elif country_name in compositions:
    #     index = countries[countries.composition == country_name].index[0]
    else:
        index = countries[countries.country == country_name].index[0]
    country = countries["country"][index]
    text_speech.say("The capital of "+ country + " is " + get_capital_from_country(country_name))
    text_speech.runAndWait()

def say_country(capital_name):
    text_speech = pyttsx3.init()
    text_speech.setProperty("rate", 150)
    text_speech.say("The country whose capital is "+ capital_name + "is" + get_country_from_capital(capital_name))
    text_speech.runAndWait()


def say_currency(country_name):
    text_speech = pyttsx3.init()
    text_speech.setProperty("rate", 150)
    text_speech.say("The currency of "+ country_name + " is the " + get_currency_from_country(country_name))
    text_speech.runAndWait()

# list_of_countries = [country.lower() for country in list_of_countries]
# list_of_capitals = [capital.lower() for capital in list_of_capitals]
keywords_1 = ("find", "what")
keywords_2 =("capital")
keywords_3 = ("country")
keyword_4 = ("currency")
