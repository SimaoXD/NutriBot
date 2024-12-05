erDiagram
    User ||--o{ DietPlan : "possui"
    User ||--o{ MealEntry : "registra"
    User ||--o{ WeightHistory : "possui"
    User ||--o{ Reminder : "configura"
    User ||--o{ Report : "recebe"

    User {
        int id PK
        string telegram_id
        string name
        string sex
        int age
        float height_cm
        float weight_kg
        boolean has_diabetes
        string goal
    }

    DietPlan {
        int id PK
        int user_id FK
        datetime created_at
        text plan_details
    }

    MealEntry {
        int id PK
        int user_id FK
        datetime timestamp
        string meal_description
        string image_path
        float calories
        float carbs
        float proteins
        float fats
    }

    WeightHistory {
        int id PK
        int user_id FK
        datetime date
        float weight_kg
    }

    Reminder {
        int id PK
        int user_id FK
        string message
        datetime scheduled_time
        boolean is_recurring
    }

    Report {
        int id PK
        int user_id FK
        datetime date
        text content
    }
