import random

class GameState:
    def __init__(self):
        self.morale = 50
        self.stability = 50
        self.faith = 50
        self.food_stock = 60
        self.month = 1
        self.max_months = 24
        self.game_over_reason = ""

    def display_status(self):
        print(f"\nHónap: {self.month}")
        print(f"Készlet: {self.food_stock}")
        print(f"\nMorál: {self.morale}")
        print(f"️Stabilitás: {self.stability}")
        print(f"Hit: {self.faith}")

    def apply_effects(self, effects):
        for key, value in effects.items():
            if hasattr(self, key):
                setattr(self, key, getattr(self, key) + value)

    def advance_turn(self):
        self.month += 1

    def is_over(self):
        if self.food_stock <= 0:
            self.game_over_reason = "Elfogyott az élelem."
            return True
        if self.stability <= 0:
            self.game_over_reason = "Összeomlott a társadalmi rend."
            return True
        if self.morale <= 0:
            self.game_over_reason = "A felső kaszt fellázadt."
            return True
        if self.faith <= 0:
            self.game_over_reason = "Vallásháború tört ki."
            return True
        if self.month > self.max_months:
            self.game_over_reason = "Túlélted a kor meghatározott végét. A rendszer még áll... de meddig?"
            return True
        return False

def get_random_event():
    events = [
        {
            "description": "Az egyik feldolgozó üzem termelése az utóbbi időben nagyon visszaesett. A kerület egyházi vezetője templommá akarja szentelni az üzemet, szerinte ún. vérvonalak futnak az épület alatt.",
            "choices": [
                {"text": "Tudatlanságodat leplezendő, egyetértesz vele a vérvonalak tekintetében és bezáratod az üzemet.", "effects": {"morale": -10, "stability": -10, "faith": +10, "food_stock": -15}},
                {"text": "Tárgyalást kezdeményezel az üzem vezetőjével. A termelés egy része megmarad, a munkások egy részét kirúgják, és az üzem egyik csarnokából kápolna lesz.", "effects": {"morale": -10, "stability": 0, "faith": +10, "food_stock": -5}}
            ]
        },
        {
            "description": "Egy döntésed komolyan megosztotta a felső kaszt és az egyház tagjait. Magyarázatot követelnek.",
            "choices": [
                {"text": "Kivégzed őket példastatuálásként.", "effects": {"morale": -10, "stability": +10, "faith": -10}},
                {"text": "Elzavarod őket, mondván, hogy te nem tartozol magyarázattal senkinek.", "effects": {"morale": -10, "stability": 0, "faith": 0}}
            ]
        },
        {
            "description": "Egy, a táplálék-kaszthoz tartozó asszony titokban megmentette a gyermekét egy rituális vágástól.",
            "choices": [
                {"text": "A főinkvizítor vezetésével nyilvánosan kivégezteted az egész családot. Senki nem ehet a bűnös húsból. ", "effects": {"morale": -10, "stability": +10, "faith": +10, "food_stock": -15}},
                {"text": "Megpróbálod a szőnyeg alá seperni az ügyet.", "effects": {"morale": 0, "stability": -10, "faith": -10}}
            ]
        },
        {
            "description": "Egy őrült prédikátor tűnik fel az egyik Vágóhíd-templom bejáratánál. Fültépően visító hangjába kolompjának zúgása vegyül. Azt prédikálja, hogy a húsevés csak mítosz. A falakon és a csonthegyeken túl léteznek úgynevezett 'növények', amik ehetőek. Egyre többen kezdenek odagyűlni...",
            "choices": [
                {"text": "Hagyod prédikálni. Később az egyház segítségével beépíted az egészet a hittételek közé, természetesen némileg átfogalmazva.", "effects": {"morale": 0, "stability": +10, "faith": +10}},
                {"text": "Egy túlbuzgó szerzetes megöli őt. A hatóság elviteti a szerzetest és több tiltakozót is.", "effects": {"morale": +10, "stability": -10, "faith": -10}}
            ]
        },
        {
            "description": "A felső kaszt egyik prominens tagjáról kiderül, hogy undorodik a hústól. A hír futótűzként terjed...",
            "choices": [
                {"text": "Egy előre felvett TV-adásban látszólag jóízűen elfogyaszt egy szelet combot.", "effects": {"morale": +10, "stability": -10, "faith": 0}},
                {"text": "Kényszeríted, hogy bevonuljon az egyik legszigorúbb szerzetesrendbe.", "effects": {"morale": -10, "stability": +10, "faith": +10}}
            ]
        },
        {
            "description": "A legnagyobb élelmiszerraktárban romlásnak indul a hús. Pánik tör ki az élelmezési bizottság körében.",
            "choices": [
                {"text": "Önkényesen bevezetsz egy böjtölésen alapuló új ünnepet. Az ünnep időtartama három nap és három éjszaka.", "effects": {"morale": +10, "stability": 0, "faith": -10, "food_stock": -15}},
                {"text": "Ideiglenesen megnöveled a vágási kvótát és kiterjeszted alacsony rangú egyházi személyekre is.", "effects": {"morale": +10, "stability": +10, "faith": -10, "food_stock": +15}}
            ]
        },
    ]
    return random.choice(events)

def run_game():
    game = GameState()

    print("""

                                                                     
     _____       _    _____       _ _            _____                   
    | __  |___ _| |  |   __|___ _| |_|___ ___   |   __|___ _____ ___ ___ 
    | __ -| .'| . |  |   __|   | . | |   | . |  |  |  | .'|     | -_|_ -|
    |_____|__,|___|  |_____|_|_|___|_|_|_|_  |  |_____|__,|_|_|_|___|___|
                                         |___|                           
                                                                       
    """)


    print("Eat Thy Neighbour – Kannibalisztikus társadalmi szimulátor\n")

    print("=======================================================================================================\n")

    lore = """...egyszerre tért vissza a világ összes hangja. Először szörnyű kakofóniának tűnt, mintha háború tört volna ki.
    De az érzékeim megcsaltak - kitörő öröm és ünnepség hangjai voltak. Ekkor vettem észre, hogy szabályosan
    ömlik rólam a vér. Egy pillanatnyi ijedelem után konstatáltam, hogy nem a sajátom. A tenyereimet nyomó súly
    csak ezután tudatosult bennem. Egy emberi szivet tartottam kezeimben. Egy csapásra eszembe jutott minden:
    Legfőbb Vezetőnk és Bíborosunk, Johannes Witt, átverte és meglopta saját népét... büntetést érdemelt.
    A szétmarcangolást követő játékokban hozzám került a szíve. Megnyertem a játékokat. Én vagyok a vezető...\n"""

    print(lore)

    print("=======================================================================================================\n")

    description = """Egy kizárólag emberhúson élő társadalom vezetőjeként fent kell tartanod a kényes egyensúlyt
    a vezető kaszt és a táplálék-munkás kaszt között. Minden döntésnek komoly következményei vannak...\n
    """

    print(description)

    print("=======================================================================================================\n")

    while not game.is_over():
        game.display_status()
        event = get_random_event()
        print(f"\nEsemény: {event['description']}\n")
        for i, choice in enumerate(event['choices']):
            print(f"{i+1}. {choice['text']}")

        valid_input = False
        while not valid_input:
            try:
                selection = int(input("\n➤ Választásod (1/2): ")) - 1
                if selection in range(len(event['choices'])):
                    valid_input = True
                else:
                    print("Hibás választás. Próbáld újra.")
            except ValueError:
                print("Kérlek számot adj meg (1 vagy 2).")

        game.apply_effects(event['choices'][selection]['effects'])
        game.advance_turn()

    print(f"\nJáték vége: {game.game_over_reason}")
    print(f"Eddig jutottál: {game.month - 1} hónap")

if __name__ == "__main__":
    run_game()
