"""Pre-built menuitems and dishes for users to use."""
import json
from pathlib import Path

from db import Dish, Menuitem, Mealplan, db

DATA_FILE = Path(__file__).with_name("seed_data.json")


def seed_database():
    data = json.loads(DATA_FILE.read_text())

    menuitems_by_dish_name = {}
    for row in data["dishes"]:
        dish = db.session.scalar(db.select(Dish).filter_by(name=row["name"]))
        if dish is None:
            dish = Dish(**row)
            db.session.add(dish)
        else:
            for key, value in row.items():
                setattr(dish, key, value)

        # One menu item per dish for now (menu_id comes later)
        if dish.menuitems:
            item = dish.menuitems[0]
        else:
            item = Menuitem()
            dish.menuitems.append(item)
        menuitems_by_dish_name[dish.name] = item

    for row in data.get("mealplans", []):
        plan = db.session.scalar(db.select(Mealplan).filter_by(name=row["name"]))
        if plan is None:
            plan = Mealplan(name=row["name"], description=row.get("description", ""))
            db.session.add(plan)
        plan.menuitems = [menuitems_by_dish_name[n] for n in row["foods"]]

    db.session.commit()