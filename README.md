iOS menu browser and macros tracker for Cornell University students.

## CampusMacros API Design
![apidesign](https://github.com/user-attachments/assets/b7dd0353-aba0-4bfe-b1ab-cd36097763d4)

### Database models
- **`DiningHall`** stores a Cornell dining hall's name, location, and Eatery ID.
- **`Menu`** stores one meal service at a hall on a specific date. It includes the meal period and service times when available.
- **`MenuItem`** records that a dish is being served on a particular menu. It links to both `Menu` and `Dish` and can store a station.
- **`Dish`** stores the dish name, serving size, nutrition source, and estimated ranges for calories, protein, carbs, and fat when available. The same dish record can be reused across menus.
- **`MealPlan`** stores the user's goals and optional original prompt. Its `snapshot` saves the recommended portions and estimated totals as they were shown at the time.
### How the models connect
- **One-to-many.** A hall can have many menus, a menu can have many items, and a dish can appear as many menu items.
- **Many-to-many.** A meal plan can contain several menu items, and the same item can appear in several plans.
### Planned API endpoints
- `GET /v1/halls` lists the Cornell dining halls and their hours.
- `GET /v1/halls/{id}/menu?meal=lunch` returns the dishes, stations, and available nutrition for a hall’s lunch menu.
- `POST /v1/meal-plans` takes the user's goals, generates and saves a plan, and returns the plan ID.
- `DELETE /v1/meal-plans/{id}` removes a saved meal plan by ID.
- `POST /v1/chat` takes a message and returns an answer or an updated plate suggestion.
