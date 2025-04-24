def get_bmi_category(weight, height):
    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5: return "underweight"
    elif 18.5 <= bmi < 25: return "normal"
    elif 25 <= bmi < 30: return "overweight"
    else: return "obese"

def classify_user(age, height, weight, diet, activity):
    # 1. Compute numeric BMI and category string
    bmi = weight / ((height / 100) ** 2)
    category = get_bmi_category(weight, height)

    plan = {}  # Initialize the plan to return

    # 1. Vegan × Underweight
    if diet == "vegan" and category == "underweight" and activity == "low":
        plan = recs["vegan"]["underweight"]["low"]
    elif diet == "vegan" and category == "underweight" and activity == "medium":
        plan = recs["vegan"]["underweight"]["medium"]
    elif diet == "vegan" and category == "underweight" and activity == "high":
        plan = recs["vegan"]["underweight"]["high"]

    # 2. Vegan × Normal
    elif diet == "vegan" and category == "normal" and activity == "low":
        plan = recs["vegan"]["normal"]["low"]
    elif diet == "vegan" and category == "normal" and activity == "medium":
        plan = recs["vegan"]["normal"]["medium"]
    elif diet == "vegan" and category == "normal" and activity == "high":
        plan = recs["vegan"]["normal"]["high"]

    # 3. Vegan × Overweight
    elif diet == "vegan" and category == "overweight" and activity == "low":
        plan = recs["vegan"]["overweight"]["low"]
    elif diet == "vegan" and category == "overweight" and activity == "medium":
        plan = recs["vegan"]["overweight"]["medium"]
    elif diet == "vegan" and category == "overweight" and activity == "high":
        plan = recs["vegan"]["overweight"]["high"]

    # 4. Vegan × Obese
    elif diet == "vegan" and category == "obese" and activity == "low":
        plan = recs["vegan"]["obese"]["low"]
    elif diet == "vegan" and category == "obese" and activity == "medium":
        plan = recs["vegan"]["obese"]["medium"]
    elif diet == "vegan" and category == "obese" and activity == "high":
        plan = recs["vegan"]["obese"]["high"]

    # 5. Vegetarian × Underweight
    elif diet == "vegetarian" and category == "underweight" and activity == "low":
        plan = recs["vegetarian"]["underweight"]["low"]
    elif diet == "vegetarian" and category == "underweight" and activity == "medium":
        plan = recs["vegetarian"]["underweight"]["medium"]
    elif diet == "vegetarian" and category == "underweight" and activity == "high":
        plan = recs["vegetarian"]["underweight"]["high"]

    # 6. Vegetarian × Normal
    elif diet == "vegetarian" and category == "normal" and activity == "low":
        plan = recs["vegetarian"]["normal"]["low"]
    elif diet == "vegetarian" and category == "normal" and activity == "medium":
        plan = recs["vegetarian"]["normal"]["medium"]
    elif diet == "vegetarian" and category == "normal" and activity == "high":
        plan = recs["vegetarian"]["normal"]["high"]

    # 7. Vegetarian × Overweight
    elif diet == "vegetarian" and category == "overweight" and activity == "low":
        plan = recs["vegetarian"]["overweight"]["low"]
    elif diet == "vegetarian" and category == "overweight" and activity == "medium":
        plan = recs["vegetarian"]["overweight"]["medium"]
    elif diet == "vegetarian" and category == "overweight" and activity == "high":
        plan = recs["vegetarian"]["overweight"]["high"]

    # 8. Vegetarian × Obese
    elif diet == "vegetarian" and category == "obese" and activity == "low":
        plan = recs["vegetarian"]["obese"]["low"]
    elif diet == "vegetarian" and category == "obese" and activity == "medium":
        plan = recs["vegetarian"]["obese"]["medium"]
    elif diet == "vegetarian" and category == "obese" and activity == "high":
        plan = recs["vegetarian"]["obese"]["high"]

    # 9. Non‑vegetarian × Underweight
    elif diet == "non-vegetarian" and category == "underweight" and activity == "low":
        plan = recs["non-vegetarian"]["underweight"]["low"]
    elif diet == "non-vegetarian" and category == "underweight" and activity == "medium":
        plan = recs["non-vegetarian"]["underweight"]["medium"]
    elif diet == "non-vegetarian" and category == "underweight" and activity == "high":
        plan = recs["non-vegetarian"]["underweight"]["high"]

    # 10. Non‑vegetarian × Normal
    elif diet == "non-vegetarian" and category == "normal" and activity == "low":
        plan = recs["non-vegetarian"]["normal"]["low"]
    elif diet == "non-vegetarian" and category == "normal" and activity == "medium":
        plan = recs["non-vegetarian"]["normal"]["medium"]
    elif diet == "non-vegetarian" and category == "normal" and activity == "high":
        plan = recs["non-vegetarian"]["normal"]["high"]

    # 11. Non‑vegetarian × Overweight
    elif diet == "non-vegetarian" and category == "overweight" and activity == "low":
        plan = recs["non-vegetarian"]["overweight"]["low"]
    elif diet == "non-vegetarian" and category == "overweight" and activity == "medium":
        plan = recs["non-vegetarian"]["overweight"]["medium"]
    elif diet == "non-vegetarian" and category == "overweight" and activity == "high":
        plan = recs["non-vegetarian"]["overweight"]["high"]

    # 12. Non‑vegetarian × Obese
    elif diet == "non-vegetarian" and category == "obese" and activity == "low":
        plan = recs["non-vegetarian"]["obese"]["low"]
    elif diet == "non-vegetarian" and category == "obese" and activity == "medium":
        plan = recs["non-vegetarian"]["obese"]["medium"]
    elif diet == "non-vegetarian" and category == "obese" and activity == "high":
        plan = recs["non-vegetarian"]["obese"]["high"]

    else:
        # Fallback for invalid inputs
        raise ValueError(f"Invalid combination: diet={diet}, bmi={bmi:.1f}, activity={activity}")
    
    # Return a dictionary that includes all necessary keys
    return {
        "bmi": bmi,
        "category": category,
        "day_plan": plan  # Ensure the day_plan is included
    }




recs = {
    "vegan": {
        "underweight": {
            "low": {
                "breakfast": [
                    "Peanut Butter Toast",
                    "Banana‑Soy Smoothie",
                    "Chia Seed Pudding",
                    "Mixed Nuts & Raisins"
                ],
                "lunch": [
                    "Tofu Curry with Brown Rice",
                    "Chickpea Rice Pilaf",
                    "Rajma Masala",
                    "Quinoa Khichdi"
                ],
                "snacks": [
                    "Dried Banana Chips",
                    "Roasted Pumpkin Seeds",
                    "Energy Bites (dates+nuts)",
                    "Trail Mix"
                ],
                "dinner": [
                    "Masala Dosa with Coconut Chutney",
                    "Vegan Korma with Roti",
                    "Baingan Bharta",
                    "Mixed Vegetable Pulao"
                ]
            },
            "medium": {
                "breakfast": [
                    "Oats Upma",
                    "Almond Milk Smoothie",
                    "Moong Dal Cheela",
                    "Fruit & Nut Muesli"
                ],
                "lunch": [
                    "Vegetable Biryani",
                    "Tofu Bhurji Wrap",
                    "Lentil Dahl with Roti",
                    "Stir‑Fried Veggies & Quinoa"
                ],
                "snacks": [
                    "Roasted Chickpeas",
                    "Cucumber Sticks & Hummus",
                    "Apple Slices with Almond Butter",
                    "Coconut Water"
                ],
                "dinner": [
                    "Grilled Tofu Skewers",
                    "Steamed Broccoli & Mushrooms",
                    "Low‑Oil Mixed Veg Curry",
                    "Cauliflower Rice"
                ]
            },
            "high": {
                "breakfast": [
                    "Protein‑Packed Smoothie",
                    "Soybean Chilla",
                    "Quinoa Porridge",
                    "Spinach & Tomato Toast"
                ],
                "lunch": [
                    "High‑Protein Vegan Curry",
                    "Lentil & Peanut Salad",
                    "Tempeh Stir‑Fry",
                    "Buckwheat Roti & Chutney"
                ],
                "snacks": [
                    "Edamame",
                    "Sprouted Lentil Salad",
                    "Protein Bars (vegan)",
                    "Dates & Walnuts"
                ],
                "dinner": [
                    "Tofu & Vegetable Kebabs",
                    "Kale & Chickpea Salad",
                    "Zucchini Noodles with Pesto",
                    "Mushroom Soup"
                ]
            }
        },
        "normal": {
            "low": {
                "breakfast": [
                    "Vegetable Poha",
                    "Green Tea with Nuts",
                    "Steamed Idli & Sambar",
                    "Fruit Salad"
                ],
                "lunch": [
                    "Rajma Chawal",
                    "Palak Tofu Curry",
                    "Multi‑Grain Roti",
                    "Cabbage Sabzi"
                ],
                "snacks": [
                    "Carrot & Cucumber Sticks",
                    "Roasted Foxnuts (Makhana)",
                    "Homemade Popcorn",
                    "Herbal Tea"
                ],
                "dinner": [
                    "Khichdi",
                    "Steamed Mixed Veggies",
                    "Tomato Dal",
                    "Beetroot Soup"
                ]
            },
            "medium": {
                "breakfast": [
                    "Upma with Peanuts",
                    "Idli Upma",
                    "Masala Oats",
                    "Banana‑Spinach Smoothie"
                ],
                "lunch": [
                    "Mixed Veg Curry & Rice",
                    "Baingan Bharta & Roti",
                    "Dal Tadka",
                    "Vegetable Khichdi"
                ],
                "snacks": [
                    "Sprouts Chaat",
                    "Buttermilk",
                    "Sliced Pear",
                    "Roasted Almonds"
                ],
                "dinner": [
                    "Lauki Soup",
                    "Steamed Spinach & Mushroom",
                    "Chapati with Low‑Oil Sabzi",
                    "Vegetable Dalia"
                ]
            },
            "high": {
                "breakfast": [
                    "High‑Protein Vegan Smoothie",
                    "Soybean & Spinach Toast",
                    "Quinoa & Berry Bowl",
                    "Tofu Scramble"
                ],
                "lunch": [
                    "Black Bean Salad",
                    "Tempeh & Veggie Stir‑Fry",
                    "Buckwheat Pulao",
                    "Mixed Dal Salad"
                ],
                "snacks": [
                    "Protein Cookies (vegan)",
                    "Mixed Seeds & Raisins",
                    "Fresh Orange Juice",
                    "Roasted Chana"
                ],
                "dinner": [
                    "Grilled Tofu & Veggie Platter",
                    "Zucchini & Tomato Bake",
                    "Low‑Calorie Soup",
                    "Steamed Bok Choy"
                ]
            }
        },
        "overweight": {
            "low": {
                "breakfast": [
                    "Steamed Idli with Chutney",
                    "Herbal Tea",
                    "Fruit Bowl",
                    "Ragi Dosa"
                ],
                "lunch": [
                    "Cucumber & Tomato Salad",
                    "Bottle Gourd Curry",
                    "Brown Rice Khichdi",
                    "Cabbage & Peas Sabzi"
                ],
                "snacks": [
                    "Apple Slices",
                    "Mint‑Lemon Water",
                    "Roasted Makhana",
                    "Green Tea"
                ],
                "dinner": [
                    "Tomato Soup",
                    "Steamed Broccoli",
                    "Zucchini Stir‑Fry",
                    "Carrot‑Beet Salad"
                ]
            },
            "medium": {
                "breakfast": [
                    "Vegetable Dalia",
                    "Green Smoothie",
                    "Upma with Veggies",
                    "Fruit & Nut Bowl"
                ],
                "lunch": [
                    "Spinach Soup",
                    "Sprouts & Veg Salad",
                    "Quinoa Salad",
                    "Lauki‑Coconut Curry"
                ],
                "snacks": [
                    "Cucumber Juice",
                    "Buttermilk",
                    "Carrot Sticks",
                    "Roasted Seeds"
                ],
                "dinner": [
                    "Steamed Greens",
                    "Cauliflower Curry",
                    "Multigrain Roti",
                    "Low‑Oil Bhindi"
                ]
            },
            "high": {
                "breakfast": [
                    "Fruit Smoothie",
                    "Oats‑Upma Hybrid",
                    "Protein Pancakes (vegan)",
                    "Chia‑Pudding"
                ],
                "lunch": [
                    "Sprouted Lentil Salad",
                    "Karela‑Apple Salad",
                    "Grilled Tofu Skewers",
                    "Bhindi Stir‑Fry"
                ],
                "snacks": [
                    "Papaya",
                    "Tender Coconut Water",
                    "Cucumber‑Lemon Slices",
                    "Mixed Nuts (small handful)"
                ],
                "dinner": [
                    "Zucchini Noodles",
                    "Vegetable Clear Soup",
                    "Steamed Corn",
                    "Roasted Cauliflower"
                ]
            }
        },
        "obese": {
            "low": {
                "breakfast": [
                    "Moong Dal Cheela (no oil)",
                    "Almond Yogurt",
                    "Cinnamon Oats",
                    "Cucumber Smoothie"
                ],
                "lunch": [
                    "Cabbage Soup",
                    "Carrot‑Beet Salad",
                    "Barley Khichdi",
                    "Steamed Spinach"
                ],
                "snacks": [
                    "Lemon Water",
                    "Roasted Makhana",
                    "Mint Tea",
                    "Chamomile Tea"
                ],
                "dinner": [
                    "Grilled Tofu Salad",
                    "Vegetable Soup",
                    "Steamed Asparagus",
                    "Multigrain Chapati"
                ]
            },
            "medium": {
                "breakfast": [
                    "Green Smoothie",
                    "Ragi Porridge",
                    "Chia‑Seeds in Almond Milk",
                    "Fruit Salad"
                ],
                "lunch": [
                    "Quinoa Veg Bowl",
                    "Lauki Soup",
                    "Palak Soup",
                    "Sprouts Salad"
                ],
                "snacks": [
                    "Lemon‑Ginger Tea",
                    "Carrot Sticks",
                    "Coconut Water",
                    "Roasted Seeds"
                ],
                "dinner": [
                    "Light Stir‑Fry Veggies",
                    "Zucchini Soup",
                    "Steamed Broccoli",
                    "Multigrain Chapati"
                ]
            },
            "high": {
                "breakfast": [
                    "Detox Smoothie",
                    "Spinach & Apple Juice",
                    "Oats Muesli",
                    "Fruit Platter"
                ],
                "lunch": [
                    "Lemon Quinoa",
                    "Grilled Veg Skewers",
                    "Kale & Chickpea Salad",
                    "Broth Soup"
                ],
                "snacks": [
                    "Cucumber‑Mint Water",
                    "Fresh Coconut",
                    "Herbal Tea",
                    "Apple Slices"
                ],
                "dinner": [
                    "Steamed Veg Bowl",
                    "Tomato Broth",
                    "Cauliflower Rice",
                    "Chamomile Tea"
                ]
            }
        }
    },
    "vegetarian": {
        "underweight": {
            "low": {
                "breakfast": [
                    "Paneer‑Stuffed Paratha",
                    "Banana‑Almond Smoothie",
                    "Chia Pudding with Yogurt",
                    "Mixed Nuts & Raisins"
                ],
                "lunch": [
                    "Paneer Butter Masala with Brown Rice",
                    "Chole Rice Pilaf",
                    "Rajma Masala",
                    "Vegetable Khichdi"
                ],
                "snacks": [
                    "Roasted Foxnuts (Makhana)",
                    "Grilled Corn",
                    "Energy Bites (dates+nuts)",
                    "Fruit Bowl"
                ],
                "dinner": [
                    "Palak Paneer with Roti",
                    "Mixed Vegetable Korma",
                    "Baingan Bharta",
                    "Multi‑Grain Chapati"
                ]
            },
            "medium": {
                "breakfast": [
                    "Vegetable Upma with Ghee",
                    "Masala Omelette",
                    "Fruit & Nut Muesli",
                    "Paneer‑Spinach Wrap"
                ],
                "lunch": [
                    "Dal Tadka with Rice",
                    "Methi Paratha & Curd",
                    "Mixed Veg Curry",
                    "Curd Rice"
                ],
                "snacks": [
                    "Sliced Apple with Peanut Butter",
                    "Buttermilk",
                    "Roasted Chickpeas",
                    "Herbal Tea"
                ],
                "dinner": [
                    "Paneer Tikka",
                    "Vegetable Soup",
                    "Steamed Greens",
                    "Chapati"
                ]
            },
            "high": {
                "breakfast": [
                    "Protein‑Rich Greek Yogurt Bowl",
                    "Egg White Omelette",
                    "Oats Pancakes with Honey",
                    "Fruit Smoothie"
                ],
                "lunch": [
                    "Egg Curry with Roti",
                    "Vegetable Salad with Boiled Eggs",
                    "Paneer Bhurji Wrap",
                    "Lentil & Rice Bowl"
                ],
                "snacks": [
                    "Boiled Egg",
                    "Mixed Seeds & Raisins",
                    "Cheese Cubes",
                    "Fruit Juice"
                ],
                "dinner": [
                    "Grilled Paneer Skewers",
                    "Mixed Veg Stir‑Fry",
                    "Broccoli Soup",
                    "Quinoa Pilaf"
                ]
            }
        },
        "normal": {
            "low": {
                "breakfast": [
                    "Steamed Idli & Sambar",
                    "Fruit Salad",
                    "Paneer Paratha (light oil)",
                    "Green Tea"
                ],
                "lunch": [
                    "Rajma Chawal",
                    "Palak Paneer",
                    "Multi‑Grain Roti",
                    "Cucumber Raita"
                ],
                "snacks": [
                    "Carrot Sticks & Hummus",
                    "Buttermilk",
                    "Roasted Almonds",
                    "Herbal Tea"
                ],
                "dinner": [
                    "Khichdi",
                    "Mixed Veg Sabzi",
                    "Beetroot Soup",
                    "Chapati"
                ]
            },
            "medium": {
                "breakfast": [
                    "Vegetable Upma",
                    "Masala Omelette",
                    "Milk & Muesli",
                    "Fruit Smoothie"
                ],
                "lunch": [
                    "Mixed Dal & Rice",
                    "Paneer Tikka Wrap",
                    "Vegetable Stir‑Fry",
                    "Curd"
                ],
                "snacks": [
                    "Sliced Pear",
                    "Roasted Chana",
                    "Buttermilk",
                    "Fruit Juice"
                ],
                "dinner": [
                    "Veg Manchow Soup",
                    "Paneer Bhurji",
                    "Steamed Spinach",
                    "Chapati"
                ]
            },
            "high": {
                "breakfast": [
                    "High‑Protein Yogurt Bowl",
                    "Oats Pancakes",
                    "Egg & Veggie Wrap",
                    "Fruit Smoothie"
                ],
                "lunch": [
                    "Egg Fried Rice",
                    "Mixed Bean Salad",
                    "Palak Paneer",
                    "Multi‑Grain Roti"
                ],
                "snacks": [
                    "Protein Bar",
                    "Mixed Nuts",
                    "Fruit Juice",
                    "Boiled Egg"
                ],
                "dinner": [
                    "Grilled Vegetable & Paneer Salad",
                    "Broth Soup",
                    "Quinoa",
                    "Chapati"
                ]
            }
        },
        "overweight": {
            "low": {
                "breakfast": [
                    "Steamed Idli",
                    "Vegetable Upma",
                    "Herbal Tea",
                    "Fruit Bowl"
                ],
                "lunch": [
                    "Cucumber Salad",
                    "Bottle Gourd Curry",
                    "Brown Rice Khichdi",
                    "Curd"
                ],
                "snacks": [
                    "Apple Slices",
                    "Mint Lemon Water",
                    "Roasted Makhana",
                    "Green Tea"
                ],
                "dinner": [
                    "Tomato Soup",
                    "Steamed Broccoli",
                    "Chapati (light oil)",
                    "Mixed Salad"
                ]
            },
            "medium": {
                "breakfast": [
                    "Vegetable Dalia",
                    "Oats Porridge",
                    "Buttermilk",
                    "Fruit Bowl"
                ],
                "lunch": [
                    "Spinach Soup",
                    "Sprouts Salad",
                    "Quinoa Salad",
                    "Mixed Dal"
                ],
                "snacks": [
                    "Coconut Water",
                    "Carrot Sticks",
                    "Roasted Seeds",
                    "Herbal Tea"
                ],
                "dinner": [
                    "Grilled Paneer with Veggies",
                    "Steamed Greens",
                    "Chapati",
                    "Vegetable Soup"
                ]
            },
            "high": {
                "breakfast": [
                    "Oats Upma",
                    "Fruit Smoothie",
                    "Boiled Egg",
                    "Green Tea"
                ],
                "lunch": [
                    "Sprouts Chaat",
                    "Grilled Veg Skewers",
                    "Mixed Bean Salad",
                    "Chapati"
                ],
                "snacks": [
                    "Tender Coconut Water",
                    "Apple Slices",
                    "Roasted Chickpeas",
                    "Buttermilk"
                ],
                "dinner": [
                    "Broccoli Soup",
                    "Zucchini Stir‑Fry",
                    "Quinoa",
                    "Chapati"
                ]
            }
        },
        "obese": {
            "low": {
                "breakfast": [
                    "Moong Dal Cheela (no oil)",
                    "Cinnamon Oats",
                    "Almond Yogurt",
                    "Herbal Tea"
                ],
                "lunch": [
                    "Cabbage Soup",
                    "Carrot Salad",
                    "Barley Khichdi",
                    "Curd"
                ],
                "snacks": [
                    "Lemon Water",
                    "Roasted Makhana",
                    "Mint Tea",
                    "Apple Slices"
                ],
                "dinner": [
                    "Steamed Paneer Salad",
                    "Vegetable Soup",
                    "Steamed Asparagus",
                    "Chapati"
                ]
            },
            "medium": {
                "breakfast": [
                    "Ragi Porridge",
                    "Chia Seeds in Almond Milk",
                    "Fruit Salad",
                    "Herbal Tea"
                ],
                "lunch": [
                    "Quinoa Veg Bowl",
                    "Palak Soup",
                    "Sprouts Salad",
                    "Chapati"
                ],
                "snacks": [
                    "Carrot Sticks",
                    "Coconut Water",
                    "Roasted Seeds",
                    "Mint Infusion"
                ],
                "dinner": [
                    "Grilled Veg Salad",
                    "Tomato Broth",
                    "Multigrain Chapati",
                    "Chamomile Tea"
                ]
            },
            "high": {
                "breakfast": [
                    "Detox Smoothie",
                    "Spinach & Apple Juice",
                    "Oats Muesli",
                    "Fruit Platter"
                ],
                "lunch": [
                    "Lemon Quinoa",
                    "Grilled Veg Skewers",
                    "Kale Salad",
                    "Broth Soup"
                ],
                "snacks": [
                    "Fresh Coconut",
                    "Herbal Tea",
                    "Apple Slices",
                    "Vegetable Sticks"
                ],
                "dinner": [
                    "Steamed Veg Bowl",
                    "Cauliflower Rice",
                    "Chapati",
                    "Chamomile Tea"
                ]
            }
        }
    },
    "non-vegetarian": {
        "underweight": {
            "low": {
                "breakfast": [
                    "Egg Bhurji with Whole Wheat Toast",
                    "Banana‑Protein Smoothie",
                    "Greek Yogurt with Berries",
                    "Mixed Nuts"
                ],
                "lunch": [
                    "Grilled Chicken Curry with Brown Rice",
                    "Fish Curry with Quinoa",
                    "Egg Curry with Roti",
                    "Dal Tadka"
                ],
                "snacks": [
                    "Boiled Egg",
                    "Roasted Chickpeas",
                    "Protein Shake",
                    "Fresh Fruit Bowl"
                ],
                "dinner": [
                    "Grilled Fish with Veggies",
                    "Chicken Stir‑Fry",
                    "Egg White Omelette",
                    "Mixed Salad"
                ]
            },
            "medium": {
                "breakfast": [
                    "Masala Omelette",
                    "Milk & Muesli",
                    "Fruit Smoothie",
                    "Mixed Nuts"
                ],
                "lunch": [
                    "Chicken Biryani (light oil)",
                    "Fish Tikka",
                    "Egg Fried Rice",
                    "Curd"
                ],
                "snacks": [
                    "Greek Yogurt",
                    "Boiled Egg",
                    "Fruit Juice",
                    "Protein Bar"
                ],
                "dinner": [
                    "Grilled Prawns Salad",
                    "Chicken Soup",
                    "Steamed Greens",
                    "Chapati"
                ]
            },
            "high": {
                "breakfast": [
                    "Protein Pancakes with Egg",
                    "Banana‑Almond Smoothie",
                    "Greek Yogurt Bowl",
                    "Fruit Platter"
                ],
                "lunch": [
                    "Grilled Chicken Salad",
                    "Fish & Veg Stir‑Fry",
                    "Egg Salad Wrap",
                    "Quinoa"
                ],
                "snacks": [
                    "Protein Shake",
                    "Boiled Egg",
                    "Mixed Nuts",
                    "Fruit Juice"
                ],
                "dinner": [
                    "Tandoori Chicken",
                    "Grilled Fish",
                    "Mixed Veg Soup",
                    "Chapati"
                ]
            }
        },
        "normal": {
            "low": {
                "breakfast": [
                    "Boiled Eggs & Avocado Toast",
                    "Herbal Tea",
                    "Fruit Salad",
                    "Mixed Nuts"
                ],
                "lunch": [
                    "Chicken Curry with Rice",
                    "Fish Fry with Salad",
                    "Egg & Veggie Stir‑Fry",
                    "Curd"
                ],
                "snacks": [
                    "Boiled Egg",
                    "Greek Yogurt",
                    "Fruit Juice",
                    "Roasted Chickpeas"
                ],
                "dinner": [
                    "Grilled Fish",
                    "Chicken Soup",
                    "Steamed Veggies",
                    "Chapati"
                ]
            },
            "medium": {
                "breakfast": [
                    "Scrambled Eggs",
                    "Oats Porridge",
                    "Fruit Smoothie",
                    "Mixed Nuts"
                ],
                "lunch": [
                    "Grilled Chicken Bowl",
                    "Fish Curry",
                    "Egg Salad",
                    "Rice"
                ],
                "snacks": [
                    "Protein Bar",
                    "Boiled Egg",
                    "Fruit Juice",
                    "Mixed Seeds"
                ],
                "dinner": [
                    "Chicken Stir‑Fry",
                    "Mixed Veg Soup",
                    "Chapati",
                    "Herbal Tea"
                ]
            },
            "high": {
                "breakfast": [
                    "Egg & Veggie Omelette",
                    "Protein Shake",
                    "Fruit Platter",
                    "Mixed Nuts"
                ],
                "lunch": [
                    "Grilled Fish Salad",
                    "Chicken & Quinoa Bowl",
                    "Egg Wrap",
                    "Steamed Veggies"
                ],
                "snacks": [
                    "Greek Yogurt",
                    "Boiled Egg",
                    "Protein Bar",
                    "Fruit Juice"
                ],
                "dinner": [
                    "Tandoori Fish",
                    "Chicken Soup",
                    "Salad",
                    "Chapati"
                ]
            }
        },
        "overweight": {
            "low": {
                "breakfast": [
                    "Egg White Omelette",
                    "Herbal Tea",
                    "Fruit Bowl",
                    "Mixed Seeds"
                ],
                "lunch": [
                    "Grilled Fish with Salad",
                    "Chicken Soup",
                    "Steamed Veggies",
                    "Curd"
                ],
                "snacks": [
                    "Boiled Egg",
                    "Greek Yogurt",
                    "Mint‑Lemon Water",
                    "Roasted Seeds"
                ],
                "dinner": [
                    "Fish Soup",
                    "Grilled Chicken Salad",
                    "Chapati",
                    "Green Tea"
                ]
            },
            "medium": {
                "breakfast": [
                    "Scrambled Eggs",
                    "Oats Porridge",
                    "Fruit Smoothie",
                    "Mixed Nuts"
                ],
                "lunch": [
                    "Chicken & Vegetable Stir‑Fry",
                    "Fish Curry (light oil)",
                    "Quinoa",
                    "Curd"
                ],
                "snacks": [
                    "Protein Shake",
                    "Boiled Egg",
                    "Fruit Juice",
                    "Roasted Chickpeas"
                ],
                "dinner": [
                    "Grilled Prawns",
                    "Vegetable Soup",
                    "Chapati",
                    "Herbal Tea"
                ]
            },
            "high": {
                "breakfast": [
                    "Protein Pancakes with Egg",
                    "Fruit Smoothie",
                    "Greek Yogurt",
                    "Mixed Nuts"
                ],
                "lunch": [
                    "Grilled Chicken Breast",
                    "Fish & Veg Stir‑Fry",
                    "Quinoa",
                    "Green Salad"
                ],
                "snacks": [
                    "Boiled Egg",
                    "Protein Shake",
                    "Fruit Juice",
                    "Mixed Seeds"
                ],
                "dinner": [
                    "Tandoori Chicken",
                    "Mixed Veg Soup",
                    "Chapati",
                    "Chamomile Tea"
                ]
            }
        },
        "obese": {
            "low": {
                "breakfast": [
                    "Egg White Omelette",
                    "Cinnamon Oats",
                    "Green Tea",
                    "Fruit Bowl"
                ],
                "lunch": [
                    "Grilled Fish Salad",
                    "Vegetable Soup",
                    "Curd",
                    "Chapati"
                ],
                "snacks": [
                    "Boiled Egg",
                    "Mint Tea",
                    "Roasted Makhana",
                    "Apple Slices"
                ],
                "dinner": [
                    "Fish Broth",
                    "Steamed Veg Bowl",
                    "Chapati",
                    "Chamomile Tea"
                ]
            },
            "medium": {
                "breakfast": [
                    "Scrambled Eggs",
                    "Oats Porridge",
                    "Fruit Smoothie",
                    "Mixed Nuts"
                ],
                "lunch": [
                    "Chicken & Quinoa Salad",
                    "Fish Soup",
                    "Chapati",
                    "Buttermilk"
                ],
                "snacks": [
                    "Protein Shake",
                    "Boiled Egg",
                    "Fruit Juice",
                    "Mixed Seeds"
                ],
                "dinner": [
                    "Grilled Prawns & Veggies",
                    "Tomato Broth",
                    "Chapati",
                    "Herbal Tea"
                ]
            },
            "high": {
                "breakfast": [
                    "Protein Pancakes",
                    "Greek Yogurt",
                    "Food Platter",
                    "Mixed Nuts"
                ],
                "lunch": [
                    "Tandoori Chicken Salad",
                    "Fish Curry (light)",
                    "Quinoa",
                    "Green Salad"
                ],
                "snacks": [
                    "Boiled Egg",
                    "Protein Shake",
                    "Fruit Juice",
                    "Mixed Seeds"
                ],
                "dinner": [
                    "Grilled Fish",
                    "Steamed Broccoli",
                    "Chapati",
                    "Chamomile Tea"
                ]
            }
        }
       
    }
    
}