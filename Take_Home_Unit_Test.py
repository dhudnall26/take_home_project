# Imports python unittest and requests modules to complete python unittests and HTTP requests. Imports "Take_Home", the main app program for testing.
import unittest
import requests
import Take_Home

class TestDates(unittest.TestCase):

# Tests that all expected dates and meal types return an HTTP 200 code.
    def test_200_response_for_expected_dates(self):
        expected_dates = ['2021-02-28', '2021-03-01', '2021-03-02', '2021-03-03', '2021-03-04', '2021-03-05', '2021-03-06', '2021-03-07', '2021-03-08', '2021-03-09', '2021-03-10', '2021-03-11', '2021-03-12', '2021-03-13', '2021-03-14', '2021-03-15', '2021-03-16', '2021-03-17', '2021-03-18', '2021-03-19', '2021-03-20', '2021-03-21', '2021-03-22', '2021-03-23', '2021-03-24', '2021-03-25', '2021-03-26', '2021-03-27'] 
        expected_meal_types = ['MEAL_KIT', 'FRESH_READY', 'PRE_PREPPED']
        for date in expected_dates:
            for meal in expected_meal_types:
                response = requests.get('http://127.0.0.1:8000/menu/' + date + '/' + meal)
                try:
                    assert response.status_code == 200
                except:
                    print("200 code not returned for the following date: " + date + " and the following meal type: " + meal + ".")
                        
# Tests that a sample of unexpected dates with expected meal types return an HTTP 404 code.
    def test_404_response_for_unexpected_dates(self):
        unexpected_dates = ['2020-02-28', '2021-05-01', '202100-03-04', '2021-02-29', '2021-03-00', '1960-03-05', '2021-03-31', '2021-03-28', '2021-0305-08', '2021-03-095', '20210310', '2021_03_11']
        expected_meal_types = ['MEAL_KIT', 'FRESH_READY', 'PRE_PREPPED']
        for date in unexpected_dates:
            for meal in expected_meal_types:
                response = requests.get('http://127.0.0.1:8000/menu/' + date + '/' + meal)
                try:
                    assert response.status_code == 404
                except:
                    print("404 code not returned for the following unexpected date: " + date + " and the following meal type: " + meal + ".")

# Tests that a sample of expected dates with unexpected meal types return an HTTP 404 code.
    def test_404_response_for_unexpected_meal_types(self):
        expected_dates = ['2021-02-28', '2021-03-01', '2021-03-02', '2021-03-03', '2021-03-04', '2021-03-05']
        unexpected_meal_types = ['MEAL-KIT', 'FRES_READY', 'CATS']
        for date in expected_dates:
            for meal in unexpected_meal_types:
                response = requests.get('http://127.0.0.1:8000/menu/' + date + '/' + meal)
                try:
                    assert response.status_code == 404
                except:
                    print("404 code not returned for the following date: " + date + " and the following unexpected meal type: " + meal + ".")

# Tests that a sample valid date and meal type input return a JSON format response.
    def test_response_type_is_json(self):
        response = requests.get("http://127.0.0.1:8000/menu/2021-03-20/FRESH_READY")
        try:
            assert response.headers["Content-Type"] == "application/json"
        except:
            print("The responses are not in JSON format.")
            
# Tests every date and meal type with an expected response (200 code) to ensure the expected response is received.
    def test_get_response(self):
        expected_dates = ['2021-02-28', '2021-03-01', '2021-03-02', '2021-03-03', '2021-03-04', '2021-03-05', '2021-03-06', '2021-03-07', '2021-03-08', '2021-03-09', '2021-03-10', '2021-03-11', '2021-03-12', '2021-03-13', '2021-03-14', '2021-03-15', '2021-03-16', '2021-03-17', '2021-03-18', '2021-03-19', '2021-03-20', '2021-03-21', '2021-03-22', '2021-03-23', '2021-03-24', '2021-03-25', '2021-03-26', '2021-03-27'] 
        expected_meal_types = ['MEAL_KIT', 'FRESH_READY', 'PRE_PREPPED']
        expected_responses = {'2021-02-28MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Mediterranean braise with zucchini, new potatoes, and capers', 'Catalan chicken with green romesco and Spanish green beans',
                                                     'Chipotle chilaquiles with black beans and fried eggs', 'Moroccan chicken with carrots, snap peas, and spicy green harissa'],
                              '2021-02-28FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Jambalaya with chicken and andouille sausage'],
                              '2021-02-28PRE_PREPPED': ['Mojo tacos with shredded cabbage, pickled onions, and salsa verde'],
                              '2021-03-01MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Mediterranean braise with zucchini, new potatoes, and capers', 'Catalan chicken with green romesco and Spanish green beans',
                                                     'Chipotle chilaquiles with black beans and fried eggs', 'Moroccan chicken with carrots, snap peas, and spicy green harissa'],
                              '2021-03-01FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-01PRE_PREPPED': ['Mojo tacos with shredded cabbage, pickled onions, and salsa verde'],
                              '2021-03-02MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Mediterranean braise with zucchini, new potatoes, and capers', 'Catalan chicken with green romesco and Spanish green beans',
                                                     'Chipotle chilaquiles with black beans and fried eggs', 'Moroccan chicken with carrots, snap peas, and spicy green harissa'],
                              '2021-03-02FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-02PRE_PREPPED': ['Mojo tacos with shredded cabbage, pickled onions, and salsa verde'],
                              '2021-03-03MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Mediterranean braise with zucchini, new potatoes, and capers', 'Catalan chicken with green romesco and Spanish green beans',
                                                     'Chipotle chilaquiles with black beans and fried eggs', 'Moroccan chicken with carrots, snap peas, and spicy green harissa'],
                              '2021-03-03FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-03PRE_PREPPED': ['Mojo tacos with shredded cabbage, pickled onions, and salsa verde'],
                              '2021-03-04MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Mediterranean braise with zucchini, new potatoes, and capers', 'Catalan chicken with green romesco and Spanish green beans',
                                                     'Chipotle chilaquiles with black beans and fried eggs', 'Moroccan chicken with carrots, snap peas, and spicy green harissa'],
                              '2021-03-04FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-04PRE_PREPPED': ['Mojo tacos with shredded cabbage, pickled onions, and salsa verde'],
                              '2021-03-05MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Mediterranean braise with zucchini, new potatoes, and capers', 'Catalan chicken with green romesco and Spanish green beans',
                                                     'Chipotle chilaquiles with black beans and fried eggs', 'Moroccan chicken with carrots, snap peas, and spicy green harissa'],
                              '2021-03-05FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-05PRE_PREPPED': ['Mojo tacos with shredded cabbage, pickled onions, and salsa verde'],
                              '2021-03-06MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Mediterranean braise with zucchini, new potatoes, and capers', 'Catalan chicken with green romesco and Spanish green beans',
                                                     'Chipotle chilaquiles with black beans and fried eggs', 'Moroccan chicken with carrots, snap peas, and spicy green harissa'],
                              '2021-03-06FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-06PRE_PREPPED': ['Mojo tacos with shredded cabbage, pickled onions, and salsa verde'],
                              '2021-03-07MEAL_KIT': ['Catalan chicken with green romesco and Spanish green beans', 'Turkey meatballs and wilted greens in lemongrass broth',
                                                     'Moroccan chicken with carrots, snap peas, and spicy green harissa', 'Sesame-crusted fish nuggets with orange-glazed vegetables'],
                              '2021-03-07FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken cacciatore with spaghetti',
                                                        'Chicken tikka masala with basmati rice pilaf'],
                              '2021-03-07PRE_PREPPED': ['Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-08MEAL_KIT': ['Catalan chicken with green romesco and Spanish green beans', 'Turkey meatballs and wilted greens in lemongrass broth',
                                                     'Moroccan chicken with carrots, snap peas, and spicy green harissa', 'Sesame-crusted fish nuggets with orange-glazed vegetables'],
                              '2021-03-08FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken cacciatore with spaghetti',
                                                        'Chicken tikka masala with basmati rice pilaf'],
                              '2021-03-08PRE_PREPPED': ['Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-09MEAL_KIT': ['Catalan chicken with green romesco and Spanish green beans', 'Turkey meatballs and wilted greens in lemongrass broth',
                                                     'Moroccan chicken with carrots, snap peas, and spicy green harissa', 'Sesame-crusted fish nuggets with orange-glazed vegetables'],
                              '2021-03-09FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken cacciatore with spaghetti',
                                                        'Chicken tikka masala with basmati rice pilaf'],
                              '2021-03-09PRE_PREPPED': ['Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-10MEAL_KIT': ['Catalan chicken with green romesco and Spanish green beans', 'Turkey meatballs and wilted greens in lemongrass broth',
                                                     'Moroccan chicken with carrots, snap peas, and spicy green harissa', 'Sesame-crusted fish nuggets with orange-glazed vegetables'],
                              '2021-03-10FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken cacciatore with spaghetti',
                                                        'Chicken tikka masala with basmati rice pilaf'],
                              '2021-03-10PRE_PREPPED': ['Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-11MEAL_KIT': ['Catalan chicken with green romesco and Spanish green beans', 'Turkey meatballs and wilted greens in lemongrass broth',
                                                     'Moroccan chicken with carrots, snap peas, and spicy green harissa', 'Sesame-crusted fish nuggets with orange-glazed vegetables'],
                              '2021-03-11FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken cacciatore with spaghetti',
                                                        'Chicken tikka masala with basmati rice pilaf'],
                              '2021-03-11PRE_PREPPED': ['Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-12MEAL_KIT': ['Catalan chicken with green romesco and Spanish green beans', 'Turkey meatballs and wilted greens in lemongrass broth',
                                                     'Moroccan chicken with carrots, snap peas, and spicy green harissa', 'Sesame-crusted fish nuggets with orange-glazed vegetables'],
                              '2021-03-12FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken cacciatore with spaghetti',
                                                        'Chicken tikka masala with basmati rice pilaf'],
                              '2021-03-12PRE_PREPPED': ['Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-13MEAL_KIT': ['Catalan chicken with green romesco and Spanish green beans', 'Turkey meatballs and wilted greens in lemongrass broth',
                                                     'Moroccan chicken with carrots, snap peas, and spicy green harissa', 'Sesame-crusted fish nuggets with orange-glazed vegetables'],
                              '2021-03-13FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken cacciatore with spaghetti',
                                                        'Chicken tikka masala with basmati rice pilaf'],
                              '2021-03-13PRE_PREPPED': ['Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-14MEAL_KIT': ['Peruvian-style halibut with lime and sweet potato', 'Mediterranean braise with zucchini, new potatoes, and capers',
                                                     'Catalan chicken with green romesco and Spanish green beans', 'Chipotle chilaquiles with black beans and fried eggs'],
                              '2021-03-14FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken tikka masala with basmati rice pilaf',
                                                        'Jambalaya with chicken and andouille sausage'],
                              '2021-03-14PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette', 'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-15MEAL_KIT': ['Peruvian-style halibut with lime and sweet potato', 'Mediterranean braise with zucchini, new potatoes, and capers',
                                                     'Catalan chicken with green romesco and Spanish green beans', 'Chipotle chilaquiles with black beans and fried eggs'],
                              '2021-03-15FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken tikka masala with basmati rice pilaf',
                                                        'Jambalaya with chicken and andouille sausage'],
                              '2021-03-15PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette', 'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-16MEAL_KIT': ['Peruvian-style halibut with lime and sweet potato', 'Mediterranean braise with zucchini, new potatoes, and capers',
                                                     'Catalan chicken with green romesco and Spanish green beans', 'Chipotle chilaquiles with black beans and fried eggs'],
                              '2021-03-16FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken tikka masala with basmati rice pilaf',
                                                        'Jambalaya with chicken and andouille sausage'],
                              '2021-03-16PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette', 'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-17MEAL_KIT': ['Peruvian-style halibut with lime and sweet potato', 'Mediterranean braise with zucchini, new potatoes, and capers',
                                                     'Catalan chicken with green romesco and Spanish green beans', 'Chipotle chilaquiles with black beans and fried eggs'],
                              '2021-03-17FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken tikka masala with basmati rice pilaf',
                                                        'Jambalaya with chicken and andouille sausage'],
                              '2021-03-17PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette', 'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-18MEAL_KIT': ['Peruvian-style halibut with lime and sweet potato', 'Mediterranean braise with zucchini, new potatoes, and capers',
                                                     'Catalan chicken with green romesco and Spanish green beans', 'Chipotle chilaquiles with black beans and fried eggs'],
                              '2021-03-18FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken tikka masala with basmati rice pilaf',
                                                        'Jambalaya with chicken and andouille sausage'],
                              '2021-03-18PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette', 'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-19MEAL_KIT': ['Peruvian-style halibut with lime and sweet potato', 'Mediterranean braise with zucchini, new potatoes, and capers',
                                                     'Catalan chicken with green romesco and Spanish green beans', 'Chipotle chilaquiles with black beans and fried eggs'],
                              '2021-03-19FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken tikka masala with basmati rice pilaf',
                                                        'Jambalaya with chicken and andouille sausage'],
                              '2021-03-19PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette', 'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-20MEAL_KIT': ['Peruvian-style halibut with lime and sweet potato', 'Mediterranean braise with zucchini, new potatoes, and capers',
                                                     'Catalan chicken with green romesco and Spanish green beans', 'Chipotle chilaquiles with black beans and fried eggs'],
                              '2021-03-20FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Chicken tikka masala with basmati rice pilaf',
                                                        'Jambalaya with chicken and andouille sausage'],
                              '2021-03-20PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette',
                                                        'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-21MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Turkey meatballs and wilted greens in lemongrass broth', 'Moroccan chicken with carrots, snap peas, and spicy green harissa',
                                                     'Sesame-crusted fish nuggets with orange-glazed vegetables', 'Ginger-scallion skewers with apple-cabbage slaw'],
                              '2021-03-21FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Spicy Southwestern turkey and sweet potato skillet',
                                                        'Chicken cacciatore with spaghetti', 'Chicken tikka masala with basmati rice pilaf', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-21PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette',
                                                        'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-22MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Turkey meatballs and wilted greens in lemongrass broth', 'Moroccan chicken with carrots, snap peas, and spicy green harissa',
                                                     'Sesame-crusted fish nuggets with orange-glazed vegetables', 'Ginger-scallion skewers with apple-cabbage slaw'],
                              '2021-03-22FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Spicy Southwestern turkey and sweet potato skillet',
                                                        'Chicken cacciatore with spaghetti', 'Chicken tikka masala with basmati rice pilaf', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-22PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette',
                                                        'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-23MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Turkey meatballs and wilted greens in lemongrass broth', 'Moroccan chicken with carrots, snap peas, and spicy green harissa',
                                                     'Sesame-crusted fish nuggets with orange-glazed vegetables', 'Ginger-scallion skewers with apple-cabbage slaw'],
                              '2021-03-23FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Spicy Southwestern turkey and sweet potato skillet',
                                                        'Chicken cacciatore with spaghetti', 'Chicken tikka masala with basmati rice pilaf', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-23PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette',
                                                        'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-24MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Turkey meatballs and wilted greens in lemongrass broth', 'Moroccan chicken with carrots, snap peas, and spicy green harissa',
                                                     'Sesame-crusted fish nuggets with orange-glazed vegetables', 'Ginger-scallion skewers with apple-cabbage slaw'],
                              '2021-03-24FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Spicy Southwestern turkey and sweet potato skillet',
                                                        'Chicken cacciatore with spaghetti', 'Chicken tikka masala with basmati rice pilaf', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-24PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette',
                                                        'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-25MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Turkey meatballs and wilted greens in lemongrass broth', 'Moroccan chicken with carrots, snap peas, and spicy green harissa',
                                                     'Sesame-crusted fish nuggets with orange-glazed vegetables', 'Ginger-scallion skewers with apple-cabbage slaw'],
                              '2021-03-25FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Spicy Southwestern turkey and sweet potato skillet',
                                                        'Chicken cacciatore with spaghetti', 'Chicken tikka masala with basmati rice pilaf', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-25PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette',
                                                        'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-26MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Turkey meatballs and wilted greens in lemongrass broth', 'Moroccan chicken with carrots, snap peas, and spicy green harissa',
                                                     'Sesame-crusted fish nuggets with orange-glazed vegetables', 'Ginger-scallion skewers with apple-cabbage slaw'],
                              '2021-03-26FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Spicy Southwestern turkey and sweet potato skillet',
                                                        'Chicken cacciatore with spaghetti', 'Chicken tikka masala with basmati rice pilaf', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-26PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette',
                                                        'Farro bowls with spinach, apricots, and green goddess dressing'],
                              '2021-03-27MEAL_KIT': ['Tomato-braised chicken with sweet potato and chard', 'Miso-ginger ground pork and summer squash donburi',
                                                     'Turkey meatballs and wilted greens in lemongrass broth', 'Moroccan chicken with carrots, snap peas, and spicy green harissa',
                                                     'Sesame-crusted fish nuggets with orange-glazed vegetables', 'Ginger-scallion skewers with apple-cabbage slaw'],
                              '2021-03-27FRESH_READY': ['Spicy Southwestern turkey and sweet potato skillet', 'Spicy Southwestern turkey and sweet potato skillet',
                                                        'Chicken cacciatore with spaghetti', 'Chicken tikka masala with basmati rice pilaf', 'Jambalaya with chicken and andouille sausage'],
                              '2021-03-27PRE_PREPPED': ['Baby broccoli, artichokes, and olives with Mediterranean vinaigrette',
                                                        'Farro bowls with spinach, apricots, and green goddess dressing']}
                              
        for date in expected_dates:
            for meal in expected_meal_types:
                response = requests.get('http://127.0.0.1:8000/menu/' + date + '/' + meal)
                response_body = response.json()
                try:
                    assert response_body[0:] == expected_responses[date+meal]
                except:
                    print("Expected response not returned for the following date: " + date + " and the following meal type: " + meal + ".")
