from nutrition.food_data import food_data

def evaluate_menu(detected_items, user):
    total_cal = 0
    total_protein = 0
    total_carb = 0
    total_fat = 0

    for food, qty in detected_items.items():
        if food in food_data:
            total_cal += food_data[food]["cal"] * qty
            total_protein += food_data[food]["protein"] * qty
            total_carb += food_data[food]["carb"] * qty
            total_fat += food_data[food]["fat"] * qty

    if user.daily_calories == 0:
        return "⚠️ Ingresa tu perfil para recibir recomendaciones."

    ratio = total_cal / user.daily_calories

    # Clasificación principal
    if ratio < 0.3:
        level = "🟡 Comida ligera"
        msg = "Aporte calórico bajo para tu perfil."
    elif ratio <= 0.6:
        level = "🟢 Comida adecuada"
        msg = "Buen equilibrio según tus datos."
    else:
        level = "🔴 Comida excesiva"
        msg = "Este menú es alto para una sola comida."

    # Ajuste especial peleador
    if user.type == "fighter" and ratio > 0.5:
        msg += " No es recomendable durante un corte de peso."

    # Mensaje final PLN
    return (
        f"{level}\n"
        f"Calorías estimadas: {int(total_cal)} kcal\n"
        f"Proteína: {int(total_protein)} g | "
        f"Carbohidratos: {int(total_carb)} g | "
        f"Grasas: {int(total_fat)} g\n"
        f"{msg}"
    )
